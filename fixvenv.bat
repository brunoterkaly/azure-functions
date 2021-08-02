call venv/scripts/deactivate
rd venv /s
python -m venv venv
echo "pip install -r batch_manager/requirements.txt"
call venv/scripts/activate
call pip install -r batch_manager/requirements.txt
