cd $(pwd)

python3 -m venv venv
. ./venv/bin/acticate

pip install -r requirements.txt

python3 main.py