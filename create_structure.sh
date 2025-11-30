#!/bin/bash

echo "🚀 Creating Project Structure"
echo "=============================="


# DBT folders
mkdir -p dbt_project/models/staging
mkdir -p dbt_project/models/intermediate
mkdir -p dbt_project/models/marts
mkdir -p dbt_project/seeds
mkdir -p dbt_project/tests
mkdir -p dbt_project/macros
mkdir -p dbt_project/analysis

# Other folders
mkdir -p data
mkdir -p src
mkdir -p models
mkdir -p app
mkdir -p reports/figures
mkdir -p reports/summaries

# Create empty files
touch requirements.txt
touch README.md
touch .gitignore

# DBT files
touch dbt_project/dbt_project.yml
touch dbt_project/profiles.yml

# DBT model files
touch dbt_project/models/staging/stg_customers.sql
touch dbt_project/models/intermediate/int_customer_features.sql
touch dbt_project/models/marts/fct_customer_churn.sql

# Python files
touch src/convert_excel_to_csv.py
touch src/train_model.py
touch src/create_scaler.py

# Notebooks
touch notebooks/01_explore_duckdb.ipynb
touch notebooks/02_train_model.ipynb

# App
touch app/streamlit_app.py

echo ""
echo "✅ Structure Created!"
echo ""
echo "📁 Project structure:"
tree -L 3 -I '__pycache__|*.pyc|target' . || ls -R

echo ""
echo "✅ Done! Now you can add code to the files."