echo "Cloning Repo, Please Wait..."
git clone -b main https://github.com/Naveen-TG/MasterolicTG.git /MasterolicTG
cd /MasterolicTG
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 tigershroff.py
