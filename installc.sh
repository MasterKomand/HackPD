#!/usr/bin/bash
pathFile="HackPD" 
pkg install python
cd ~/../usr/bin 
# команда
touch HackPD
echo "cd ~/$pathFile/ && python HackPD.py" >  HackPD
chmod +x HackPD
cd ~/
#конец