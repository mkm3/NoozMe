#File that runs env, secrets.sh, and server automatically"""

source env/bin/activate
source secrets.sh
python3 server.py

#executes rights/permissions for all of <file>
#1-time command line
#chmod +x run.sh

#syntax for command line each time
#./run.sh 
