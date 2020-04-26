# pod2m3u
Python Script to convert a podcast.xml file to an M3U file using Podcastparser.py

Clone this repo in home folder

```
$ pip install podcastparser
$ cd /home/pi
$ git clone https://github.com/duracell80/pod2m3u.git
$ cd /home/pi/pod2m3u
$ python pod2m3u.py http://static.aboveandbeyond.nu/grouptherapy/podcast.xml abovebeyond 10
$ sudo cp *.m3u /var/lib/mpd/playlists/
$ mpc clear; mpc load podcast_abovebeyond; mpc play
```
It takes three params ... 
1) The xml feed 
2) A name to append to the m3u file
3) Number of episodes to return
