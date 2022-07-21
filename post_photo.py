from instabot import Bot

bot = Bot()

bot.login(username="your_userid", password="your_password")

img = "photo.jpg"   # give the path and name if it is in different directory
bot.upload_photo(img, caption="(...")