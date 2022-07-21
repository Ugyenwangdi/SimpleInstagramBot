from instabot import Bot

bot = Bot()
bot.login(username="your_username", password="your_password")

# To unfollow a single user.
bot.unfollow("username")

# To unfollow more users.
unfollow_list = ["userId1", "userId2", "userId3", "..."]
bot.unfollow_users(unfollow_list)