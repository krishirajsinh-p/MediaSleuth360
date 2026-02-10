#!/bin/bash

# Install the required packages
cat packages.txt | xargs sudo apt install -y

# Create virtual environment and install Python dependencies
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

./.venv/bin/pip install --upgrade pip
./.venv/bin/pip install -r requirements.txt
source .venv/bin/activate

# Make secrets file
mkdir -p ./.streamlit
echo -e 'GROQ_API_KEY=""\nGOOGLE_API_KEY=""' > ./.streamlit/secrets.toml