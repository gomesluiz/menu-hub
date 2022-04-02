# setup git devoloper settings.
git config --global user.email gomes.luiz@gmail.com
git config --global user.name "Luiz Gomes"

# setup python virtual enviroments.
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
