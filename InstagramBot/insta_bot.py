from instabot import Bot


league = Bot()
#login to insta
league.login(username="League_boomers", password="leagueoglegendsinsta123")
def upload():
    #choose which pic and caption to post
    league.upload_photo("pic.jpg", caption="This is my first post!")


while True:
    try:
        upload()
        time.sleep(7200)
    except KeyboardInterrupt:
        print('Manual break by user')
