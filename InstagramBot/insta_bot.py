from instabot import Bot
import os
import random
import time

league = Bot()
#login to insta
league.login(username="League_boomers", password="leagueoglegendsinsta123")
def upload():
    #choose which pic and caption to post
    path =r'C:\Users\Mr Kek\Desktop\Insta bot\RedditBot\images\\'
    path_for_delete =r'C:\Users\Mr Kek\Desktop\Insta bot\RedditBot\images'
    files = os.listdir(path)
    index = random.randrange(0, len(files))
    print(files[index])



    #choose a ramd,om file from folder and assign caption as a name of the file (delete 4 characters .jpg)
    league.upload_photo(path + files[index], caption=files[index][:-4])



#    time.sleep(5)
#    os.remove(path_for_delete + files[index] + ".REMOVE_ME")



upload()

