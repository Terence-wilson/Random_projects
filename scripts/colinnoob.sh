#!/bin/bash

#This script gives colin the ability to use linux

mkdir ~/noobscripts
touch ~/noobscripts/please
touch ~/noobscripts/what

#construct please
echo '#!/bin/bash' >> ~/noobscripts/please
echo ' ' >> ~/noobscripts/please
echo '#This script will allow colin to actually use the command please' >> ~/noobscripts/please
echo ' ' >> ~/noobscripts/please
echo 'case $1 in' >> ~/noobscripts/please
echo '   download)' >> ~/noobscripts/please
echo '      apt install $2' >> ~/noobscripts/please
echo '      ;;' >> ~/noobscripts/please
echo '   *)' >> ~/noobscripts/please
echo '      echo "I dont know how to do that yet... Teach me! UwU"' >> ~/noobscripts/please
echo '      ;;' >> ~/noobscripts/please
echo 'esac' >> ~/noobscripts/please


#construct what
echo '#!/bin/bash' >> ~/noobscripts/what
echo '' >> ~/noobscripts/what
echo 'response=$(( $(date +%s) % 10 ))' >> ~/noobscripts/what
echo 'case $response in' >> ~/noobscripts/what
echo '   1)' >> ~/noobscripts/what
echo '      echo "U WOT M8"' >> ~/noobscripts/what
echo '      ;;' >> ~/noobscripts/what
echo '   2)' >> ~/noobscripts/what
echo '      echo "SAY WHAT ONE MORE TIME"' >> ~/noobscripts/what
echo '      ;;' >> ~/noobscripts/what
echo '   3)' >> ~/noobscripts/what
echo '      echo "You son of a bitch. You fucking piece of shit. You goddamn fucker"' >> ~/noobscripts/what
echo '      ;;' >> ~/noobscripts/what
echo '   4)' >> ~/noobscripts/what
echo '      echo "Its ok hon, you will figure it out!"' >> ~/noobscripts/what
echo '      ;;' >> ~/noobscripts/what
echo '   5)' >> ~/noobscripts/what
echo '      echo "what"' >> ~/noobscripts/what
echo '      ;;' >> ~/noobscripts/what

echo '   6)' >> ~/noobscripts/what
echo '      echo "Try doing sudo reboot"' >> ~/noobscripts/what
echo '      ;;' >> ~/noobscripts/what
echo '   7)' >> ~/noobscripts/what
echo '      echo "If you stop doing this to me I will do what oyu want"' >> ~/noobscripts/what
echo '      ;;' >> ~/noobscripts/what
echo '   8)' >> ~/noobscripts/what
echo '      echo "what"' >> ~/noobscripts/what
echo '      ;;' >> ~/noobscripts/what
echo '   9)' >> ~/noobscripts/what
echo '      echo "TBH i have no idea what to do"' >> ~/noobscripts/what
echo '      ;;' >> ~/noobscripts/what
echo '   0)' >> ~/noobscripts/what
echo '      echo "what"' >> ~/noobscripts/what
echo '      ;;' >> ~/noobscripts/what
echo 'esac' >> ~/noobscripts/what

chmod +x ~/noobscripts/what
chmod +x ~/noobscripts/please

echo export PATH="~/noobscripts:$PATH" >> ~/.bashrc

reboot





