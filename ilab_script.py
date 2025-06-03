#!/usr/bin/env python3
import sys
import psycopg2
import pandas as pd
from tabulate import tabulate

def execute_query(query):
    try:
        print("Connecting to postgres database...")
        conn = psycopg2.connect(
            host="postgres.cs.rutgers.edu",
            database="group1", 
            user="cvm53",       
            password=""         
        )
        
        print("Running query...")
        df = pd.read_sql_query(query, conn)
        
        if not df.empty:
            formatted_table = tabulate(df, headers='keys', tablefmt='psql', showindex=False)
            print("===RESULTS_BEGIN===")
            print(formatted_table)
            print("===RESULTS_END===")
        else:
            print("===RESULTS_BEGIN===")
            print("Query returned no results.")
            print("===RESULTS_END===")
            
    except Exception as e:
        print("===RESULTS_BEGIN===")
        print(f"Error executing query: {e}")
        print("===RESULTS_END===")
    finally:
        if 'conn' in locals() and conn:
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = sys.argv[1]
        execute_query(query)
    else:
        query = sys.stdin.read().strip()
        if query:
            execute_query(query)
        else:
            print("No query provided.")
