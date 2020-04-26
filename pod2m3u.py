import sys, os, urllib, podcastparser
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf8')


# Get feed of podcast else set default
try:
    print("Podcast Feed: " + sys.argv[1])
    feedurl = sys.argv[1]
except IndexError as e:
    # Skynews Daily Podcast by Default
    feedurl = "https://www.spreaker.com/show/3287246/episodes/feed"
    
# Get name of podcast else set default
try:
    print("Podcast Playlist Name: podcast_" + sys.argv[2])
    pod_name = sys.argv[2]
except IndexError as e:
    pod_name = "default"    


# Get name of podcast else set default
try:
    print("Podcast Episodes: " + sys.argv[3])
    pod_items = sys.argv[3]
except IndexError as e:
    pod_items = 5


    

    
    
    
data            = podcastparser.parse(feedurl, urllib.urlopen(feedurl), int(pod_items))
pod_title       = data["title"]
pod_timeformat  = "%m/%d/%Y"
pod_m3u         = "#EXTM3U\n"



# Let's do this, metaverse from podcastparser.py ...
# total_time,
# description
# payment_url
# link
# guid
# enclosures:
#    url
#    mime_type,
#    file_size
#    file_size
# description_html
# title
# published
# episode_art_url


for s in data["episodes"]:
    
    pod_date    = datetime.fromtimestamp(s["published"])
    pod_m3u     = pod_m3u + "#EXTINF:"+ str(s["total_time"])+ "," + pod_title + " - " + pod_date.strftime(pod_timeformat) + " - " + s["title"] + "\n"
    
    for e in s["enclosures"]:
        pod_m3u = pod_m3u + e["url"] + "\n\n"
        
os.system("sudo touch podcast_"+pod_name+".m3u")
os.system("sudo chmod 777 podcast_"+pod_name+".m3u")
with open("podcast_"+pod_name+".m3u", "w") as f_m3u:
    f_m3u.write(pod_m3u)
    
    
#os.system("sudo mv -f *.m3u /var/lib/mpd/playlists/")
#os.system("mpc clear; mpc load podcast_"+pod_name+"; mpc play")