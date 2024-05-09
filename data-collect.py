import csv
from instaloader import Instaloader
from instaloader import Profile
import instaloader
import time
from random import randint

# initialize instaloader to help scrape data
L = instaloader.Instaloader()

usernames = [] # usernames of accounts
userclass = [] # real = 0, bot = 1, fake = 2

# read through training data and save in array
with open('train_data.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        name = line[0]
        bot = line[1]
        usernames.append(name)
        userclass.append(bot)

# determine random number for sleep
tsleep = randint(1,20)

# testing instaloader loop
for name in usernames:
    profile = Profile.from_username(L.context, name)
    print(profile)
    time.sleep(tsleep)