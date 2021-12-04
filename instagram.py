# Automating instagram
# Install python instabot
# Examples in the link
# https://github.com/ohld/igbot/blob/master/examples/unfollow_non_followers.py

# import Bot from instabot to interact with instagram
from instabot import Bot


# Instance of Bot
bot = Bot()

# login with username and password
bot.login(username="username", password="password")



# You can either convert photo to .jpg or replace the photo with jpeg type one.

# upload the photo a jpg or jpeg
img = "tomioka.jpg"
bot.upload_photo(img, caption="(...")

# Follow user
bot.follow("username to follow")
bot.unfollow("username to unfollow")

# Send message
bot.send_message("message", ['receiverUsername'])

# Print all followers
followers = bot.get_user_followers("username")
for follower in followers:
    print(bot.get_user_info(follower))

"""
    instabot example
    Workflow:
        1) unfollows users that don't follow you.
"""
# bot.unfollow_non_followers()

bot.logout()



# ################# We can also user instapy to create instabot

# # first install instapy, use: pip install instapy 

# from instapy import InstaPy
# from instapy import smart_run
# session = InstaPy(username="25iytt", password="uGHENDI^000", headless_browser=False)
# with smart_run(session):
#     session.set_relationship_bounds(enabled=True, delimit_by_numbers=True, max_followers=5000, min_following=10, min_followers=10)
#     session.follow_user_followers(['cristiano'], amount=10, randomize=False)
#     #session.unfollow_users(amount=10, allFollowing=True)
#     session.end()