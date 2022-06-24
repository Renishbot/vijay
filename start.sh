echo "Cloning Repo, Please Wait..."
git clone -b main https://github.com/Naveen-TG/VijayFilter-TG.git /VijayFilter-TG
cd /VijayFilter-TG
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 tigershroff.py
