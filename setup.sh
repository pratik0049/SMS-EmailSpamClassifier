#!/bin/bash

# ================================
# setup.sh - Setup environment for Spam Classifier
# ================================

# 1️⃣ Create virtual environment (if not exists)
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# 2️⃣ Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# 3️⃣ Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# 4️⃣ Install required packages
echo "Installing required packages..."
pip install --upgrade \
    numpy \
    pandas \
    scikit-learn \
    nltk \
    streamlit \
    pickle-mixin

# 5️⃣ Download NLTK resources
mkdir -p ~/.nltk_data
python -m nltk.downloader punkt stopwords -d ~/.nltk_data

# 6️⃣ Setup complete
echo "Setup complete! Virtual environment activated."
echo "To activate later, run: source .venv/bin/activate"
