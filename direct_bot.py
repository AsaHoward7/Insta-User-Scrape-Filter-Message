from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random

# Username and password of your instagram account:
my_username = 'username'
my_password = 'password'




#Below is my attempt to grab usernames from a csv. It's the exact same snippet
#from engagement_calc.py that does this. 
#input_file = '/Users/asaspadeshoward/Desktop/followers_over_9000.csv'
#insta_handles_list = list()
#profile_df = pd.read_csv.head(input_file)
#for idx, row in profile_df.iterrows():
       # target_profile = row.Username

username = ['asa_howard','copycodes.io']


# Messages:
mssg_1 = "Hey, we saw that you followed @camilleramzee who happens to be one of our amazing paid influencers on our platform so we wanted to reach out. We can tell all the hard work you have put into building your following and wanted to talk about a way for you to make some extra cash off of the following you have already built. CopyCodes is a centralized place for discount codes, affiliate links, and other shopping finds and pays YOU when people access them. <br />Let us know if you are interested and we can give you some more information or set up a quick 5-10 minute phone call. Looking forward to hearing from you and getting you set up as an influencer to start making money. <br />CopyCodes.io"
mssg_2 = "Hey, we were checking out your page and noticed that you followed @camilleramzee! If you know her, she is actually one of our amazing paid influencers on our new platform, CopyCodes. We can see all the hard work you have put into building your following and wanted to talk about a way for you to make some extra cash off of the following you have already built. CopyCodes is a centralized place for discount codes, affiliate links, and other shopping finds and pays YOU when people access them. \nWe would love for you to join our community of paid influencers! Let us know if you are interested and we can give you some more information or set up a quick 5-10 minute phone call. Looking forward to hearing from you! \nCopyCodes.io"

messages = [mssg_1, mssg_2]



#delay time
between_messages = 300

browser = webdriver.Chrome('chromedriver')

# Authorization:
def auth(username, password):
	try:
		browser.get('https://instagram.com')
		time.sleep(random.randrange(2,4))

		input_username = browser.find_element_by_name('username')
		input_password = browser.find_element_by_name('password')

		input_username.send_keys(username)
		time.sleep(random.randrange(1,2))
		input_password.send_keys(password)
		time.sleep(random.randrange(1,2))
		input_password.send_keys(Keys.ENTER)

	except Exception as err:
		print(err)
		browser.quit()

# Sending messages:
def send_message(users, messages):
	try:
		browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
		time.sleep(random.randrange(3,5))
		browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
		time.sleep(random.randrange(1,2))
		browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button').click()
		for user in users:
			time.sleep(random.randrange(1,2))
			browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(user)
			time.sleep(random.randrange(2,3))
			browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]').find_element_by_tag_name('button').click()
			time.sleep(random.randrange(3,4))
			browser.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()
			time.sleep(random.randrange(3,4))
			text_area = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
			text_area.send_keys(random.choice(messages))
			time.sleep(random.randrange(2,4))
			text_area.send_keys(Keys.ENTER)
			print(f'Message successfully sent to {user}')
			time.sleep(between_messages)
			browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()

	except Exception as err:
		print(err)
		browser.quit()

	


auth(my_username, my_password)
time.sleep(random.randrange(2,4))
send_message(username, messages)


