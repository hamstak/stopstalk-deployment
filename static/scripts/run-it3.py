import os
from datetime import datetime

stopstalk_logs = "/root/stopstalk-logs/"
if not os.path.exists(stopstalk_logs):
    print "Creating directory " + stopstalk_logs + " ..."
    os.makedirs(stopstalk_logs)

os.chdir(stopstalk_logs)
today = str(datetime.now()).split(" ")[0]
today_dir = stopstalk_logs + today + "/"
if not os.path.exists(today_dir):
    print "Creating directory " + today + " ..."
    os.makedirs(today_dir)

os.chdir(today_dir)

directory = "/home/www-data/web2py/"

print "Retrieving submissions ..."
os.system("python " + directory + \
          "web2py.py -S stopstalk -M -R " + directory + \
          "applications/stopstalk/static/scripts/submissions3.py > " + \
          today_dir + "submissions3.log")
os.system("cat " + today_dir + "/submissions3.log")

print "Refreshing tags ..."
os.system("python " + directory + \
          "web2py.py -S stopstalk -M -R " + directory + \
          "applications/stopstalk/static/scripts/refresh_tags.py > " + \
          today_dir + "tags3.log")
os.system("cat " + today_dir + "/tags3.log")
