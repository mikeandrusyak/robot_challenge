#!/bin/bash

# config
IP_ADDRESS="192.168.0.47"
BRANCH="main"
REMOTE_DIR="/home/pi/Dashboard/user/Robo_challenge/My_Projects/Jupyter"
USER="pi"

if [ -z "$IP_ADDRESS" ] || [ -z "$BRANCH" ]; then
    echo "Usage: ./deploy_to_zumi.sh <IP_ADDRESS> <BRANCH>"
    exit 1
fi

echo "🚀 Connecting to Zumi at $IP_ADDRESS and deploying branch '$BRANCH'..."

# Connect to Zumi
sshpass -p "pi" ssh $USER@$IP_ADDRESS << EOF
cd $REMOTE_DIR
git fetch
git checkout $BRANCH
git pull origin $BRANCH

# Check the start position
# python3 src/check_start.py

# Запускаємо перевірку коду
python3 src/main.py
EOF

# Load csv file
# scp "$USER@$IP_ADDRESS:~/robot_challenge/result.csv" "./result_$(date +%Y-%m-%d_%H-%M).csv"

# echo "✅ CSV file successfully loaded (result.csv)."