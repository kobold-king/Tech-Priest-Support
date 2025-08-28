VENV_DIR="venv"
REQUIREMENTS_FILE="requirements.txt"

# Check if the virtual environment directory exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment '$VENV_DIR' not found. Creating..."
    python3 -m venv "$VENV_DIR"
    echo "Virtual environment created."
else
    echo "Virtual environment '$VENV_DIR' already exists."
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install required packages if requirements.txt exists
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Installing required packages from $REQUIREMENTS_FILE..."
    pip install -r "$REQUIREMENTS_FILE"
else
    echo "No $REQUIREMENTS_FILE found. Skipping package installation."
fi
