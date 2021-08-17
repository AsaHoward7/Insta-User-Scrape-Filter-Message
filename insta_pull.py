import instaloader
import pandas as pd

# Create list of Insta Handles
insta_handle_filename = "bethannrobinson_followers.csv"
# Read in the file
handles = pd.read_csv(insta_handle_filename)

# Function to pull Followers based on instagram handle
def pull_insta_info(handle):
    # Create an instance of Instaloader class
    bot = instaloader.Instaloader()

    # Load a profile from an Instagram handle
    profile = instaloader.Profile.from_username(bot.context, handle)

    # Example of using API
    # print(type(profile))
    # print("Username: ", profile.username)
    # print("User ID: ", profile.userid)
    # print("Number of Posts: ", profile.mediacount)
    # print("Followers: ", profile.followers)
    # print("Followees: ", profile.followees)
    # print("Bio: ", profile.biography,profile.external_url)

    return profile.followers

# Create empty list to add username and follower count
follower_list = list()
user_list = list()

# Iterate through list of Instagram handles
for rowIndex, row in handles.iterrows():
    # Try/Except to catch errors and private accounts
    try:
        # Use function to pull follower count
        followers = pull_insta_info(row.insta_handles)
        # Add follower count to list
        follower_list.append(followers)
        # Add username to list
        user_list.append((row.insta_handles))
        print(row.insta_handles, followers)
    except:
        print("User is private: ", row.insta_handles)
        # If not able to collect info assume private or non-exist account
        follower_list.append("private_account")
        # Add user to list to maintain ordering
        user_list.append(row.insta_handles)

# Create dictionary to organize the data
insta_dictionary = {'Username': user_list, 'Followers': follower_list}
# Convert to Pandas DataFrame for easy output
df = pd.DataFrame(insta_dictionary)
# Save to CSV File and remove the index column
df.to_csv("insta_follower.csv", index=False)


