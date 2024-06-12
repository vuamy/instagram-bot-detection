# Instagram Bot Multimodal Classification Model
Created for ECS271 Machine Learning project of classifying Instagram accounts as controlled by a real or fake user.
##
Project by Amy Vu, Aaron Nguyen, and Arisa Cowe

### Files Included
data-collect.py: script that utilizes Instaloader to gather data from public profiles on Instagram when provided with their username.
##
all .csv files: contains username and classification label for our script to web scrape from
##
data folder: all subfolders contain the gathered data for each account scraped from Instagram. includes: username, number of followers, number of accounts following, profile picture, biography, post images, and post captions
##
ECS271.ipynb: jupyter notebook containing all code for data extraction and preprocessing, individual unimodal models, and final multimodal model
##

### Results
Average across 5 validation tests
##
Numerical: F1 - 0.5, Accuracy - 0.627
##
Profile Picture: F1 - 0.638, Accuracy - 0.712
##
Posts: F1 - 0.815, Accuracy - 0.831
##
Textual: F1 - 0.881, Accuracy - 0.881
##
Average: F1 - 0.852, Accuracy - 0.864

