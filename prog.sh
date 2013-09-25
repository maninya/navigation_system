#!/bin/bash 
WIRE_LOC="$(python find_loc.py)"
UNKNOWN="Location unknown, maybe the ground floor, please ask a human for help"
UNRECOG="I cannot recognise what is in front of me"
if test "$WIRE_LOC" = "$UNKNOWN" 
then
    echo $UNKNOWN | festival --tts
    exit 
fi
echo "Nearest known location is" $WIRE_LOC | festival --tts
streamer -t 2 -r 1 -o test0.jpeg
match="$(python img.py test1.jpeg $WIRE_LOC)"
echo $match | festival --tts
#sudo gksu service network-manager restart
#sleep 15
