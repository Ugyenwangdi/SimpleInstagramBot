from instabot import Bot

bot = Bot()
bot.login(username="your_username", password="your_password")

post_link = "https://www.instagram.com/p/CWqleONFg4/"   # enter the post link
post = bot.get_media_id_from_link(post_link)

# like
bot.like(post)

# comment
bot.comment(post, "Comments ..")