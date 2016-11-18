python ring.py
videotag=$(sed '/loadVideo: true" src="/!d;s//&\n/;s/.*\n//;:a;/<\/video>/bb;$!{n;ba};:b;s//\n&/;P;D' ring.html)
rm ring.html
videourl=$(echo $videotag | sed -s 's|" /> Your browser does not support the video tag.||g')
videourl=$(echo $videourl | sed -s 's|amp\;||g')
clear
echo $videourl
wget -c -O video.mp4 $videourl
