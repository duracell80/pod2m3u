import sys, os, urllib, urllib2, requests, json, podcastparser
from datetime import datetime



reload(sys)
sys.setdefaultencoding('utf8')






# GET feed of podcast else set default
try:
    feedurl = sys.argv[1]
except IndexError as e:
    # Skynews Daily Podcast by Default
    feedurl = "https://www.spreaker.com/show/3287246/episodes/feed"
else:
    r = requests.get(feedurl)
    feedstatus = str(r.status_code)

# CHECK ALL IS OK WITHOUT 404
if "404" in feedstatus:
    print("Feed not found")
    sys.exit()
else:    
    
    
    
    
    
    
    # GET name of podcast else set default
    try:
        pod_name = sys.argv[2]
    except IndexError as e:
        pod_name = "default"    


    # GET name of podcast else set default
    try:
        pod_items = sys.argv[3]
    except IndexError as e:
        pod_items = 5
    
    # SET a user agent string because some podcast sites throw a 403 forbidden, if no UA set
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    feedrequest = urllib2.Request(feedurl, headers=hdr)

    # GET the dictonary object from Podcastparser    
    try:
        data = podcastparser.parse(feedurl, urllib2.urlopen(feedrequest), int(pod_items))
    except podcastparser.FeedParseError:
        print("Podcast Parser Error: Please file a bug report at github.com/gpodder/podcastparser")
        sys.exit()
    
pod_title       = data["title"]
pod_timeformat  = "%m/%d/%Y"
pod_m3u         = "#EXTM3U\n"

sys.exit()

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


# CHECK for cover art
    if "http" in data["cover_url"]:
        pod_art = data["cover_url"]
    
    
    pod_date    = datetime.fromtimestamp(s["published"])
    pod_m3u     = pod_m3u + "#EXTINF:"+ str(s["total_time"])+ "," + pod_title + " - " + pod_date.strftime(pod_timeformat) + " - " + s["title"] + "\n"
    
    for e in s["enclosures"]:
        pod_m3u = pod_m3u + e["url"] + "\n\n"
        
os.system("sudo touch podcast_"+pod_name+".m3u")
os.system("sudo chmod 777 podcast_"+pod_name+".m3u")
with open("podcast_"+pod_name+".m3u", "w") as f_m3u:
    f_m3u.write(pod_m3u)
    
    
os.system("sudo touch podcast_"+pod_name+".json")
os.system("sudo chmod 777 podcast_"+pod_name+".json")    
with open("podcast_"+pod_name+".json", "w") as f_json:
    f_json.write(str(json.dumps(data, indent=4)))
