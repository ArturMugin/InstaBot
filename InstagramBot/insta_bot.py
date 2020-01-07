from instabot import Bot
import os
import random
import redditbot
from time import sleep as s
import schedule
import glob

# Upload the image to Instagram, set the caption as the filename minus the file extension and then remove it
def uploadImage(bot, image):
    path = f"{os.getcwd()}\\images\\{image}"
    hashtags = ["#league", "#leagueoflegends", "#lol", "#riot", "#games", "#riotgames", "#legends", "#game", "#leagueoflegendsmemes", "#leagueoflegendsfanart", "#leagueoflegendscosplay", "#gaming", "#art", "#rito", "#leagueoflegend", "#lolgame", "#leaguegame", "#champions", "#leaguememes", "#lolmemes", "#leagueoflegendsmeme", "#garen", "#jinx", "#xayah"]
    originalCaption = redditbot.captions[image[:-4]]
    caption = f"{originalCaption}\n.\n.\n.\n{' '.join(hashtag for hashtag in hashtags)}"

    if image[-4:] in [".jpg", ".jpeg", ".png"]:
        if bot.upload_photo(path, caption):
            removeImage(image, originalCaption)
    else:
        if bot.upload_video(path, caption):
            removeImage(image, originalCaption)

def removeImage(image, caption):
    try:
        os.remove(f"{os.getcwd()}\\images\\{image}")

        try:
            del redditbot.captions[caption]
            redditbot.saveCaptions()
            print("Image Removed")
        except KeyError:
            pass

        print("Image Removed")
    except OSError:
        pass

# Select an image from the images folder and return the filename
def selectImage():
    return random.choice(os.listdir(f"{os.getcwd()}\\images"))

# Recursively delete .REMOVE_ME file extensions in the project folder
def deleteRemoveMe():
    for file in glob.glob(f"{os.getcwd()}\\**/*.REMOVE_ME", recursive=True):
        os.remove(file)

def main(bot):
    # Delete REMOVE_ME files
    deleteRemoveMe()

    # Select the image
    image = selectImage()
    print(f"\nSelected Image: '{image}'")

    # Upload the image
    print("Attempting Upload ...")
    uploadImage(bot, image)

"""
if you dont understand this, read this: https://stackoverflow.com/questions/419163/what-does-if-name-main-do#answer-419185
creates a scheduler to run after a certain time period where n is a number and f is a function:
schedule.every().second.do(main) - every second
schedule.every(n).seconds.do(main) - every n amount of seconds
schedule.every().minute.do(f) - every minute
schedule.every(n).minutes.do(f) - every n amount of minutes
schedule.every().hour.do(main) - every hour
schedule.every(n).hours.do(f) - every n amount of hours
"""
if __name__ == '__main__':
    # Start the Reddit Bot
    redditbot.main()

    # Create the Instagram Bot
    league = Bot()

    # Login to Instagram
    #league.login(username="testingapitest", password="Testingapitest123")
    league.login(username="LVL7.Yasuo", password="art2000")

    main(league)
    schedule.every(4).hours.do(lambda: main(league))

    while 1:
        schedule.run_pending()
        s(1)