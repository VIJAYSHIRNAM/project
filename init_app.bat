# Create virtual environment
python -m venv venv

# Activate virtual environment
./venv/Scripts/activate

# Install the dependencies that are listed in ams_app_req.txt
pip install -r ams_app_req.txt

# Display python version
python --version

# Display Log message
echo 'Run start_app.bat file to start app'