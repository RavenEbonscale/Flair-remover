from praw import Reddit as rd
from datetime import date
import configparser
from time import sleep

Days = ["Monday","Tuseday","Wensday","Thursday","Friday","Saturday","Sunday"]

print("===============Reading Config File===================")

config = configparser.ConfigParser()
config.read("config.ini")
print("===========Logging into reddit==================")

red = rd(    username=config['Api_keys']['username'],
    password=config['Api_keys']['password'],
    client_id=config['Api_keys']['client_id'],
    client_secret =config['Api_keys']['secret'],
    user_agent = 'Flair deleter by u/Purple_scale_boi')

print(f"{red.user.me()} has logged in sucessfully ")

#This is a santiy check to make sure it is gettig the right day



def check_day(today):
    """Checks if is the correct day"""
    if today == "Saturday":
        return True
    else:
        return False
        
def check_flairs():
    sub =  red.subreddit(config['msc']['subreddit'])
    for post in sub.stream.submissions():
        flair,pid  = post.link_flair_text, post.id
        if str(flair) == "Suspect SOS":
            subm =red.submission(id=pid)
            subm.mod.remove()
        day = date.weekday(date.today())
        if check_day(str(Days[day])) is True:
            break
        else:
            continue

def unrestriced_mehtod():
    """The Main"""
    while True:
        day = date.weekday(date.today())
        if check_day(str(Days[day])) is False:
            check_flairs()
        else:
            sleep(3600)

#Named after a anime reminder to change           
unrestriced_mehtod()