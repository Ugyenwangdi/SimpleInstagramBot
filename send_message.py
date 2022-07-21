from instabot import Bot

bot = Bot()
bot.login(username="your_username", password="your_password")

# To send message to a single user.
message = "Hello, Thanks for the gift"
bot.send_message(message, "username")