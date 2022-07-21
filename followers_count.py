from instabot import Bot

bot = Bot()
bot.login(username="your_username", password="your_password")

# Count number of followers
followers = bot.get_user_followers("username")
print("Total number of followers:")
print(len(followers))