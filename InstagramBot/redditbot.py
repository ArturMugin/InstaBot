import re

import praw
import urllib.request
import os

from PIL import Image # Install 'Pillow' package for PIL to work


# Download the image and set the filename
def downloadImage(url, fileName):
    urllib.request.urlretrieve(url, f"{os.getcwd()}\\images\\{fileName}.{url[-4:]}")
    print(f"Downloading {url} ...")

# Pre-process the image for downloading
def handleImages(leagueOfMemes):
    for submission in leagueOfMemes:
        # Remove restricted characters
        fileName = re.sub('\W+','', submission.title)


        # Download the image
        downloadImage(submission.url, fileName)

    print("All Images Downloaded")

    changeImageSizes()


"""
Resize the images to the correct sizes for Instagram

Resized to 1080x1080 so that when Instagram compresses the image its close to 600x600
"""
def changeImageSizes():
    size = 1080, 1080
    for k,v in enumerate(os.listdir(f"{os.getcwd()}\\images")):
        try:
            image = f"{os.getcwd()}\\images\\{v}"
            beforeImage = Image.open(image)
            resizeImage = beforeImage.resize(size)
            resizeImage.save(image)
        except FileNotFoundError:
            pass
    print("Image Sizes Converted to 1080x1080\n")

"""


Check if the images directory is empty by returning True or False
"""
def checkForEmptyDirectory():
    if not os.listdir(f"{os.getcwd()}\\images"):
        return True
    else:
        return False

def main():
    # Reddit API login
    reddit = praw.Reddit(client_id='_tcBKu9u-1WnAg',
                         client_secret='lA_WEyYyVTZyFFVBKO98QOBzWKM',
                         username='leagueoglegendsinsta',
                         password='leagueoglegendsinsta123',
                         user_agent='League memes')

    # Choose Sub-Reddit
    subReddit = reddit.subreddit('LeagueOfMemes')

    # Get top 5 posts
    leagueOfMemes = subReddit.top(time_filter="day", limit=5)

    """
    If the images directory is empty then download and handle the response of the top 5 posts on Reddit otherwise
    don't download anything, this is to avoid the Bot uploading photos its already uploaded. By making sure it uses
    its initials 5 photos before downloading a new set means that there is a lower chance of it re-downloading 
    a re-uploaded Image off of Reddit.
    
    This can be removed if you want.
    """
    if checkForEmptyDirectory():
        handleImages(leagueOfMemes)
    else:
        print("Skipping Image Downloads ...")

# if you dont understand this, read this: https://stackoverflow.com/questions/419163/what-does-if-name-main-do#answer-419185
if __name__ == '__main__':
    main()
