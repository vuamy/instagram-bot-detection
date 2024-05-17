import csv
from instaloader import Instaloader
from instaloader import Profile
import instaloader
import time
from random import randint
import os

# initialize instaloader to help scrape data
L = instaloader.Instaloader(download_video_thumbnails=False)
L.login("instabotincomments", "Flan5645!")  

usernames = [] # usernames of accounts
userclass = [] # real = 0, bot = 1, fake = 2

# read through training data and save in array
with open('Instagram_Username_Dataset_Updated.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        name = line[0]
        bot = line[1]
        usernames.append(name)
        userclass.append(bot)
    print(usernames)

# determine random number for sleep
tsleep = randint(10,20)

failed_list = []

# testing instaloader loop

for name in usernames:
    # create folder for this user
    newpath = "./{}".format(name)
    if not os.path.exists(newpath):
        os.makedirs(newpath)    
    
    # create paths within folders
    captionfile = open((os.path.join(newpath, "{}_captions.txt".format(name))), "w+", encoding="utf-8")
    os.makedirs(os.path.join(newpath, "{}_images".format(name)), exist_ok=True)
    imagepath = "./{}/{}_images".format(name, name)
    
    try:
        # get profile from the given username
        profile = Profile.from_username(L.context, name)
    
        # download information into their folder
        count = 0 # keeps track of how many images
        for post in profile.get_posts():
            count += 1

            # saves all captions into a single txt file
            if post.caption:
                captionfile.write(post.caption+"\n")

            # saves all images concatenated by image count into the image folder    
            L.download_pic(os.path.join(imagepath, "{}_image_{}".format(name, count)), post.url, post.date_utc)

        #creates text file for follower/followee count, first line is for number of followers, second line is for number of followees
        follower_followee = open((os.path.join(newpath, "{}_follower_info.txt".format(name))), "w+", encoding="utf-8")
        follower_followee.write(str(profile.followers) +"\n"+str(profile.followees))

        #creates text file for biography
        bio = open((os.path.join(newpath, "{}_biography.txt".format(name))), "w+", encoding="utf-8")
        bio.write(str(profile.biography))

        #saves the profile picture into image folder
        L.download_profilepic_if_new(profile, None)
    except:
        failed_list.append(name)

    captionfile.close()



    time.sleep(tsleep) # sleep so instagram doesnt kick us out

print("List of profiles failed to generate: " + str(failed_list))