# RedditPythonTools
These tools work using the reddit API and include features such as name collecting and mass PMing. It also has a script
that checks for duplicate names and removes them which can also concat multiple lists (in .csv format) into one.
## INSTALLATION
To install this, run setup.bat. This will download the python installer. Please install python using this as default. 
When python is installed press any key on the setup.bat file. DO NOT DO THIS BEFORE PYTHON HAS INSTALLED. This will
install all the libraries.

## COLLECTING NAMES
To collect names double click on the file called run.bat. This will start the relevant script. If you get an error saying
"No module called PRAW", run setup.bat again but do not re-install python. Then try again. If that doesn't work please
add an issue on GitHub

Once the script is working you need to enter the unique id for the thread you want to collect the names off. To get this
you simply need to find the 6 chars in the url (marked with Xs below:)

https://www.reddit.com/r/subreddit/comments/XXXXXX/title/

DO NOT ENTER A FULL URL, THIS WILL NOT WORK. Once a thread is done you can do another. This will generate a csv file of
names. Its name will look random, do not worry. When you are done collecting names, enter END when it asks for a new
thread.

## CHECKING FOR DUPES
If you have multiple csvs from the above script you can turn them into one file. REMEMBER: There will be no dupes inside
one csv, only between them. To do this run concat.bat. This will ask you to enter the names of the csvs (i.e. myNames.csv)
Once you have entered all the names enter END and it will write out a csv of all the names called final.csv. If you want
to add more names to this, simply enter final.csv as the first csv file, then any other files after that. WARNING: This
will overrite final.csv so be very careful

## SENDING PMs
The final step is to send PMs to users, to do this run send.bat. This will ask you to login with the reddit account you
want to use to send the messages. It will the ask for a csv file to read in. If you have used the last script then this
should be final.csv. This will then send a message to all of the names on the list. I suggest making one big csv file of
all the names before running the names (using concat.bat) so that there are no dupes. This script will check for dupes 
when it is run (it will only message each user once) but if it is run twice it cannot check so might thus send the same thing
to two people.

To have a line break in your message remeber to include two newlines in the source file.
