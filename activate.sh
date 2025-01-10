#!/bin/bash

# Check if the virtual environment directory exists
if [ ! -d "venv" ]; then
  echo "Virtual environment not found. Creating one..."
  # Create the virtual environment
  python3 -m venv venv
else
  echo "Virtual environment already exists."
fi

# Activate the virtual environment
if [ -f "venv/bin/activate" ]; then
  echo "Activating the virtual environment..."
  source venv/bin/activate
else
  echo "Error: Unable to activate the virtual environment. Check if 'venv' was created properly."
  exit 1
fi

# Install the requirements if requirements.txt exists
if [ -f "requirements.txt" ]; then
  echo "Installing requirements from requirements.txt..."
  pip install --upgrade pip  # Always upgrade pip to the latest version
  pip install -r requirements.txt
else
  echo "No requirements.txt found. Skipping dependency installation."
fi

echo "Setup complete."

export PYTHONPATH="$PYTHONPATH:$(pwd)/src"
export PYTHONPATH="$PYTHONPATH:$(pwd)/test"
