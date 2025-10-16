#!/bin/bash
set -e

echo "🛠 Creating tables..."
python /app/app/tables_create.py

echo "📂 Loading CSV data..."
python /app/app/db_loader.py

echo "✅ Setup completed!"

echo "🔄 Starting auto-insert..."
python /app/app/auto_insert.py
