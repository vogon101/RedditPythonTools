import praw
import time

filename = str(time.time())+".csv"

print "To get the thread index find the string of chars marked as Xs here:"
print "https://www.reddit.com/r/Subreddit/comments/XXXXX/title/"
print "\nWhen you are done please enter END to end the program and write it to a script"

ua = '/u/someone for /r/somesub'
r = praw.Reddit(user_agent=ua)
r.config._ssl_url = None

authors=[]
while True:
    t = raw_input("Please enter the thread to run >>>")
    if t == "END":
        break
    print "Starting the fetch"
    try:
        thread = r.get_submission(submission_id=t)
    except praw.errors.NotFound:
        print "Sorry, that thread was not found, please try again"
        continue
    except praw.errors.Forbidden:
        print "Sorry, that thread is in a private sub, this script can't access that"
        continue
    thread.replace_more_comments(limit=None, threshold=0)
    flat_list = praw.helpers.flatten_tree(thread.comments)
    with open(filename, 'a') as f:
        for thing in flat_list:
            if thing.author is not None and thing.author.name not in authors:
                authors.append(thing.author.name)
                f.write(thing.author.name)
                f.write('\n')
    print "Done"
