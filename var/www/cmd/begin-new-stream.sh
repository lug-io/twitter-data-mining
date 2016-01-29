#!/bin/bash

### SCHEDULED: Nightly, at midnight
#--
#-- Stops previous screen command that is pulling from Twitter's STREAM API
#-- Then kicks up a new process that creates and saves the pulled data into a new
#-- file with the day's date as a name.
#--
###

# Colors:  http://stackoverflow.com/questions/5947742/how-to-change-the-output-color-of-echo-in-linux
GRN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

## Kill all screen sessions
echo -e "\n${GRN}~~ Kill all existing screen sessions${NC}"
screen -ls | grep Detached | awk '{print $1}' | cut -f1 -d'.' | while read in; do screen -X -S $in quit; done
screen -ls


## Build output location string
#echo -e "${GRN}~~ Build output location string${NC}"
#OUTPUTDIR="/var/www/html/content/data/"
#OUTPUTDATE=$(date +%Y%m%d)
#OUTPUTFILENAME="$OUTPUTDIR$OUTPUTDATE.txt"
#touch $OUTPUTFILENAME
#echo -e "${RED}$OUTPUTFILENAME${NC}"


## Start screen
echo -e "\n${GRN}~~ Start data-mining screen${NC}"
screen -d -m -S data-miner
screen -S data-miner -X stuff "python /var/www/cmd/twitter-streaming.py"$(echo -ne '\015') # > $OUTPUTFILENAME"
screen -ls
echo -e '\n'
