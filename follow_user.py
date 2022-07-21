from instabot import Bot

bot = Bot()

bot.login(username="your_userid", password="your_password")

# To follow single user.
bot.follow("username")


# to follow multiple users

list_of_user = ["userId1", "userId2", "userId3", "...."]
bot.follow_users(list_of_user)