from instabot import Bot

bot = Bot()
bot.login(username="your_username", password="your_password")

# To unfollow everyone use:
# Please Note that using this will remove all your followings
bot.unfollow_everyone()