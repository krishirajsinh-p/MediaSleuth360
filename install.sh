#!/bin/bash

# Install the required packages
cat packages.txt | xargs sudo apt install -y

# Install the required Python packages
pip install -r requirements.txt

# Make secrets file
mkdir -p ./.streamlit
echo -e 'GROQ_API_KEY=""\nGOOGLE_API_KEY=""' > ./.streamlit/secrets.toml