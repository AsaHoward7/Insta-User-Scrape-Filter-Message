import pandas as pd
from instaloader import Instaloader, Profile

input_file = '/Users/asaspadeshoward/Desktop/followers_over_9000.csv'

loader = Instaloader()
loader.login('yourusername','yourpassword')
insta_handles_list = list()
engagement_list = list()

profile_df = pd.read_csv(input_file)
#take out .head() to get all of them
for idx, row in profile_df.iterrows():
    target_profile = row.Username

    profile = Profile.from_username(loader.context, target_profile)

    num_followers = profile.followers
    total_num_likes = 0
    total_num_comments = 0
    total_num_posts = 0

    for post in profile.get_posts():
        total_num_likes += post.likes
        total_num_comments += post.comments
        total_num_posts += 1

    engagement = float(total_num_likes + total_num_comments) / (num_followers * total_num_posts)
    print (target_profile,engagement * 100)

    insta_handles_list.append(target_profile)
    engagement_list.append(engagement * 100)

# Create dictionary to organize the data
insta_dictionary = {'insta_handles': insta_handles_list, 'engagement_%': engagement_list}
# Convert to Pandas DataFrame for easy output
df = pd.DataFrame(insta_dictionary)
# Save to CSV File and remove the index column
df.to_csv("engagement_rate.csv", index=False)

