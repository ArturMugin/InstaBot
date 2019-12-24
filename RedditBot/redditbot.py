import praw
import urllib.request
import os


# Download the image and set the filename
def downloadImage(url, file_name):
    urllib.request.urlretrieve(url, f"{os.getcwd()}\\images\\{file_name}.{url[-4:]}")

# Pre-process the image for downloading
def handleImages(leagueOfMemes):
    for submission in leagueOfMemes:
        # Delete Windows restricted characters
        fileName = submission.title.translate({ord(i): None for i in '!,./?*"!;][=+'})

        # Download the image
        downloadImage(submission.url, fileName)


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

    # Handle the response of the top 5 posts
    handleImages(leagueOfMemes)
main()
