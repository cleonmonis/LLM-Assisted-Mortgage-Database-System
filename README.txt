## README file
-------------------------
# LLM-Assisted Mortgage Database System

This project integrates a PostgreSQL mortgage application database with a locally hosted Large Language Model (LLM) to support natural language queries. It enables analysis of loan approvals, demographic patterns, and geographic trends using both structured SQL and unstructured queries.

## Team Members

- Harsh Borkhetaria — ilab script, Postgres connection, SSH tunneling  
- Cleon Monis — LLM integration, orchestration, testing, video demo  
- Sameel Arif — Schema design, query refinement  
- Saanvi Pandey — Database creation script, test queries, query tuning

## Features

- Structured relational database for mortgage data with normalized schema
- Integration with a local LLM to interpret and execute natural language queries
- Python scripts to manage SSH tunneling and interact with the database
- Sample dataset and SQL schema included for testing and demonstration

## Technologies

- PostgreSQL  
- Python  
- Large Language Model (local)  
- SSH tunneling (via iLab)

## Setup and Usage

1. Run `create_database.sql` to build the schema and populate tables with sample data.
2. Use `ilab_script.py` to establish an SSH tunnel with the remote Postgres server.
3. Run `database_llm.py` to interact with the database via LLM-driven queries.

## Insights Enabled

- Loan approval rates by agency, income level, or geography  
- Common reasons for loan denial across counties  
- Demographic breakdown of applicants and approval likelihood  
- Natural language exploration of patterns without writing SQL

## Notes

- Minor issues were encountered in edge cases around null applicant fields.
- Queries work best when schema context is provided clearly to the LLM.
