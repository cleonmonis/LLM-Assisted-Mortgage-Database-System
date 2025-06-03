#!/usr/bin/env python3
"""
Natural Language to SQL Query Converter for Mortgage Database
Project 2 - CS 336: Principles of Information and Data Management
"""
import os
import subprocess
import sys
import paramiko
from getpass import getpass
from llama_cpp import Llama

ssh_host = "butter.cs.rutgers.edu"
ssh_username = "cvm53"

model_path = os.path.expanduser("~/Downloads/Phi-3.5-mini-instruct-Q4_K_M.gguf")

def load_schema():
    """Load the SQL schema file for context"""
    try:
        with open('./schema.sql', 'r') as content_file:
            return content_file.read()
    except FileNotFoundError:
        print("Error: schema.sql file not found in the current directory.")
        print("Please make sure the schema.sql file is in the same directory as this script.")
        sys.exit(1)

def get_llm_answer(question, llm, schema):
    """Generate SQL query using the LLM"""
    input_text = f"""You are an expert SQL query writer. Generate a valid SQL SELECT query to answer the given question based on the database schema provided.
    
DATABASE SCHEMA:
{schema}

IMPORTANT NOTES:
1. The database contains mortgage loan application data for New Jersey.
2. The tables have the following structure and relationships:
   - loan_details: Contains loan amount, type, purpose, etc.
   - applicants: Contains applicant demographics and income
   - applications: Links loan_details, applicants, agencies, and geographic_data
   - geographic_data: Contains location information
   - agencies: Contains information about lending agencies
3. For queries comparing loan amounts and income, note that both are stored in thousands of dollars.
4. Use direct table queries rather than complex joins whenever possible.

USER QUESTION: {question}

Respond with ONLY the SQL query that answers the question. The query must be valid PostgreSQL syntax.
"""
    
    output = llm(
        input_text,
        max_tokens=200,
        echo=False,
        temperature=0.1  
    )
    return output["choices"][0]["text"]

def extract_sql_query(llm_response):
    """Extract just the SQL query from the LLM's response"""
    if llm_response.strip().upper().startswith("SELECT"):
        return llm_response.strip()
    
    if "```sql" in llm_response and "```" in llm_response.split("```sql", 1)[1]:
        query = llm_response.split("```sql", 1)[1].split("```", 1)[0].strip()
        return query
    
    if "```" in llm_response and "```" in llm_response.split("```", 1)[1]:
        query = llm_response.split("```", 1)[1].split("```", 1)[0].strip()
        if query.upper().startswith("SELECT"):
            return query
    
    if "SELECT" in llm_response.upper():
        lines = llm_response.split('\n')
        sql_lines = []
        capture = False
        
        for line in lines:
            if "SELECT" in line.upper() and not capture:
                capture = True
                sql_lines.append(line)
            elif capture and line.strip():
                sql_lines.append(line)
                if ";" in line:
                    break
        
        return '\n'.join(sql_lines).strip()
    
    return llm_response.strip()

def run_ssh_command(username, password, query):
    """Run the SQL query on the iLab server"""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    ilab_script_path = "/common/home/cvm53/Prin Info/Project 2/ilab_script.py"
    
    try:
        print(f"Connecting to {ssh_host}...")
        ssh.connect(ssh_host, username=username, password=password)
        print("Connected to SSH server.")
        
        script_content = """#!/usr/bin/env python3
import sys
import psycopg2
import pandas as pd
from tabulate import tabulate

def execute_query(query):
    try:
        # Connect to the 'group1' database
        conn = psycopg2.connect(
            host="postgres.cs.rutgers.edu",
            database="group1",  # Use group1 as the database
            user="cvm53",       # Your NetID
            password=""         # No password needed with GSSAPI authentication
        )
        
        # Execute query and fetch results
        df = pd.read_sql_query(query, conn)
        
        # Format results as a table
        if not df.empty:
            print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
        else:
            print("Query returned no results.")
            
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        if 'conn' in locals() and conn:
            conn.close()

if __name__ == "__main__":
    # If an argument is provided, use it as the query
    if len(sys.argv) > 1:
        query = sys.argv[1]
        execute_query(query)
    else:
        # Read from stdin if no argument is provided
        query = sys.stdin.read().strip()
        if query:
            execute_query(query)
        else:
            print("No query provided.")
"""
        dir_path = os.path.dirname(ilab_script_path)
        ssh.exec_command(f"mkdir -p '{dir_path}'")
        
        stdin, stdout, stderr = ssh.exec_command(f"cat > {ilab_script_path} << 'EOL'\n{script_content}\nEOL")
        stdout.read() 
        
        ssh.exec_command(f"chmod +x {ilab_script_path}")
        print(f"Created ilab_script.py at {ilab_script_path}")
        
        escaped_query = query.replace("'", "'\\''")
        postgres_cmd = f"""psql -h postgres.cs.rutgers.edu -d group1 -c '{escaped_query}' """
        print(f"Running command: {postgres_cmd}")
        stdin, stdout, stderr = ssh.exec_command(postgres_cmd)
        
        result = stdout.read().decode()
        errors = stderr.read().decode()
        
        if errors and "psql: warning:" not in errors: 
            print(f"Errors: {errors}")
            return None
        
        return result
            
    except Exception as e:
        print(f"SSH connection error: {e}")
        return None
    finally:
        ssh.close()

def main():
    """Main function to run the application"""
    print("\n" + "="*50)
    print("MORTGAGE DATABASE NATURAL LANGUAGE QUERY SYSTEM")
    print("="*50)
    print("This system allows you to query the mortgage database using natural language.")
    print("Your questions will be converted to SQL and executed on the database.")
    print("="*50 + "\n")
    
    if not os.path.exists(model_path):
        print(f"Error: Model file not found at {model_path}")
        print("Please make sure the Phi-3.5-mini model file is in your Downloads folder.")
        print("You can download it from: https://huggingface.co/bartowski/Phi-3.5-mini-instruct-GGUF/blob/main/Phi-3.5-mini-instruct-Q4_K_M.gguf")
        sys.exit(1)
    
    schema = load_schema()
    print("Database schema loaded successfully.")
    
    print("Initializing LLM (this may take a moment)...")
    try:
        llm = Llama(
            model_path=model_path,
            n_ctx = 4096, 
            n_gpu_layers=0,
            verbose=False 
        )
        print("LLM initialized successfully.")
    except Exception as e:
        print(f"Error initializing LLM: {e}")
        sys.exit(1)
    
    if ssh_username == "cvm53":
        username = input(f"Enter your Rutgers NetID [{ssh_username}]: ") or ssh_username
    else:
        username = ssh_username
    
    password = getpass("Enter your Rutgers password: ")
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print(f"Testing SSH connection to {ssh_host}...")
        ssh.connect(ssh_host, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command("echo 'SSH connection successful'")
        result = stdout.read().decode().strip()
        print(result)
        ssh.close()
    except Exception as e:
        print(f"SSH connection failed: {e}")
        sys.exit(1)
    
    print("\nMortgage Database NL Query System")
    print("Type 'exit' to quit\n")
    
    while True:
        question = input("\nEnter your question (or 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        
        print("Generating SQL query...")
        llm_response = get_llm_answer(question, llm, schema)
        
        sql_query = extract_sql_query(llm_response)
        print(f"\nGenerated SQL query:\n{sql_query}\n")
        
        print("Executing query on database...")
        result = run_ssh_command(username, password, sql_query)
        
        if result:
            print("\nQuery Results:")
            print(result)
        else:
            print("\nNo results returned or an error occurred.")

if __name__ == "__main__":
    main()