from instabot import Bot
import os
import random
import pickle
import redditbot

import time

# Upload the image to Instagram, set the caption as the filename minus the file extension and then remove it
def uploadImage(bot, image):
    caption = redditbot.captions[image[:-4]]
    if bot.upload_photo(f"{os.getcwd()}\\images\\{image}", caption):
        print("Image Removed")
        removeImage(image, caption)

def removeImage(image, caption):
    try:
        os.remove(f"{os.getcwd()}\\images\\{image}")

        try:
            del redditbot.captions[caption]
            redditbot.saveCaptions()
        except KeyError:
            pass

        print("Image Removed")
    except OSError:
        pass

# Select an image from the images folder and return the filename
def selectImage():
    return random.choice(os.listdir(f"{os.getcwd()}\\images"))

def main():
    # Start the Reddit Bot
    redditbot.main()

    # Create the Instagram Bot
    league = Bot()

    # Login to Instagram
    league.login(username="League_boomers", password="leagueoglegendsinsta123")

    # Select the image
    image = selectImage()
    print(f"Selected Image: '{image}'")

    # Upload the image
    print("\nAttempting Upload ...")
    uploadImage(league, image)

# if you dont understand this, read this: https://stackoverflow.com/questions/419163/what-does-if-name-main-do#answer-419185
if __name__ == '__main__':
    main()