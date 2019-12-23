import praw
import urllib.request

#list of post titles
mylist_new = list()



#name the jpg file and download it
def dl_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)





# reddit api login
reddit = praw.Reddit(client_id='_tcBKu9u-1WnAg',
                     client_secret='lA_WEyYyVTZyFFVBKO98QOBzWKM',
                     username='leagueoglegendsinsta',
                     password='leagueoglegendsinsta123',
                     user_agent='League memes')



def download():
    #choose subredit
    subreddit = reddit.subreddit('LeagueOfMemes')

    #take top five posts per day
    LeagueOfMemes = subreddit.top(time_filter='day', limit=6)


    # function to be done with the posts
    for submission in LeagueOfMemes:
        #delete windows restricted characters for files
        file_name = submission.title.translate({ord(i): None for i in '!,./?*"!;][=+'})
        #print the title of post
        print(file_name)
        url = submission.url
        #take iamge url of a post
        dl_jpg(url, 'images/', file_name)
        #add post title to list
        mylist_new.append(submission.title)




#start program
download()
#print the list
print(mylist_new)

