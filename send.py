import praw
import time
import csv, random, sys

username = raw_input ("Please eneter your username >>")
password = raw_input ("Please enter your password  >>")

print "\n"*100

filename = raw_input ("Please enter the filename of the csv containing the names: >>")

messagefile = raw_input ("Please enter the file of the message in txt format (ie msg.txt): >>")
subject = raw_input ("Please enter the subject line here:           : >>")
ua = 'Message sender'
r = praw.Reddit(user_agent=ua)

try:
    r.login(username, password, disable_warning=True)
except praw.errors.InvalidUserPass:
    print "Could not log-in. Password incorrect, please try again"
    sys.exit(1)

names = []
message=""
with open (messagefile, "rb") as file:
    message = file.read()

with open(filename, "rb") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        name = row[0]
        if name not in names:
            names.append(name)

for user in names:
    print user
    try:
        r.send_message(user, subject, message)
        time.sleep(random.randint(1,7))
    except praw.errors.InvalidUser:
        print "User " + user + " does not exist"
print("Sent")
