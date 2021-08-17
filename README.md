# Insta-User-Scrape-Filter-Message

All of the following info will be important for running this successfully. I recommend you leaving this pulled up as you attempt to connect it. 

Step 1 - Find profiles to scrape

Start by going to phantombuster.com and creating a free profile. 

Open the “insta follower collector” automation. 

	•	First connect your instagram proxy
	•	Then open a google sheet and type the URL of the insta account that you want to scrape (it’s best to just do one at a time)
	•	Copy and paste that URL into the “profiles to scrape” section. 
	•	Under behavior choose watcher mode and name your file “[accountname]_followers”
	•	Lastly, go to settings and choose manual. 

As an example, the result of this is a CSV file called “copycodes.io_followers.csv” and it will include information on approx. 8000 accounts that follow CopyCodes.io. 



Step 2 - Formatting your file for the script

Next step. You will want to open copycodes.io_followers.csv 

	▪	Delete all EXCEPT the following columns: username, profileUrl, isPrivate, and query.


	▪	Then, go to the isPrivate tab and sort by descending. You will see TRUE. Select any row that says TRUE and delete them. This will eliminate any account that is private. 


	▪	Lastly, change the username column name to “insta_handles”

Save as CopyCodes.io_followers.csv



Step 3 - Use a script to get the # of followers for each account

Open insta_pull.py and change insta_handle_filename to “CopyCodes.io_followers.csv”

Save and run the file. 


This will initiate a process that will take each individual account name and find the number of followers that it has. Assume 1000 names per hour. As of right now, it is not scripted to save automatically, so make sure that your computer stays awake until all names have been scraped. 

This will result in about 4000 public accounts’ number of followers and save it to a file called insta_follower.csv


	•	Next, open this file and sort “Followers” by ascending. Delete any account that has less than 10,000 followers or is private. 
	•	Save the file as something like “followers_over_10000.csv”



Step 4 (optional) - Calculate the engagement rate for each account above 10k followers


If you want to get the engagement rate for each of these accounts, do this step. 

In this instance, here is the formula that we are using for engagement rate: 

(total number of likes + total number of comments) / (total number of posts + total number of followers)

Steps to do this. 

	▪	Open working_engagement_calc.py

	▪	Copy and paste the path to the updated CSV file after input_file =

	⁃	Example: Input_file = ‘/Users/asaspadeshoward/Desktop/followers_over_10000.csv”

	▪	Next, type out your instagram account username and password in the parenthesis after loader.login

	⁃	Example: loader.login(‘username’,’password’)


Run the script. This will read the “Username” column found in your previous CSV file and calculate the engagement rate for each of the accounts in there. 

*Note* This will only work for about 50 names before it has made too many requests from instagram.

When/if it finishes it should automatically save to engagement_rate.csv

*Note 2* I have realized that engagement may not be the best metric to use for this, but we can definitely use it as a tool for determining who we could reach out to. 


Step 5 - Direct Message Bot

This is the last and final script that we currently have. 

You will need to install selenium and have a web driver for ChromeDriver in PATH. 

Upon opening direct_bot.py, enter your instagram username and password in the designated locations. 

	▪	In the “username =“ section, please enter the account @ of any account that you want to message.

	▪	Under # Messages:, you may add as many messages as you like. This will further help to disguise yourself as a human account, not a bot. 

	▪	between_messages =
	⁃	This is where you put in the maximum amount of time to delay between each message. 

The result of running this direct_bot.py will open an automated google Chrome tab that will automatically log into instagram with the account info you provide earlier. Then it will search each account and should randomly distribute one of your messages to that specific account. This will repeat until all usernames have been messaged. 

*Note* There is a snippet in direct_bot.py that I have coded out with #. This is the same snippet that I used in engagement_calc.py to quickly gather all usernames in that CSV. Unfortunately, I could not figure out how to apply that here, but I included the same snippet. 

*Note 2* As of right now, there is no code to create a line break in an insta message. I have tried \n and that did not work. You could try <br/> because that is the line break code for HTLM. Otherwise, individual paragraphs will be sent as separate messages. 


End. 


