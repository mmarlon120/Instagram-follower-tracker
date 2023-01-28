import instaloader
import os.path



class Insta_info:
    def __init__(self, username):
        self.username = username
        self.loader = instaloader.Instaloader()
        self.profile = instaloader.Profile.from_username(self.loader.context, self.username)

    def Login(self):
        login = self.loader.load_session_from_file(self.username)
        return login
    
    def get_my_followers(self):
        for followers in self.profile.get_followers():
            with open("followers.txt" , "a+") as f:
                file = f.write(followers.username+'\n')

def main():
    old_list = []
    new_list = []
# This is the simple login to check which account you'd like to check
    username = input("Username = ")
# This block is to be able to test the program without access to
# Instaloader
# If you're the owner of test1 or test2 then you're already here :)
    if username == "test1":
        old_list = ["Elliot","Josh","Nick"]
        new_list = ["Dylan","God King Touchy","Sage", "Katana"]
        print(comparitor(old_list, new_list))
        exit(0)
    elif username == "test2":
        old_list = ["Elliot","Josh","Nick", "Cousin Canoli"]
        new_list = ["Dylan","God King Touchy","Sage"]
        print(comparitor(old_list, new_list))
        exit(0)
#This block will log into the selected account then make the
#required follower list.
    insta_info = Insta_info(username)
    insta_info.Login()
    path = "./followers.txt"
    if os.path.isfile(path) == False:
        print("No prior list to compare against. Making list")
        insta_info.get_my_followers()
    else:
        #Getting the old follower list to compare against
        with open("followers.txt" , "r") as f:
            old_data = f.read()
            old_list = old_data.split("\n")
        #Making the new list to compare against the old
        os.remove("followers.txt")
        insta_info.get_my_followers()
        with open("followers.txt" , "r") as f:
            new_data = f.read()
            new_list = new_data.split("\n")
        print(comparitor(old_list, new_list))
        exit(0)

#List Organizer is to format the information given to comparitor
#The Format should come out as "Old List | New List"
def list_organizer(old, new, difference):
    string = ""
    if difference > 0:
        for follower in range(difference):
            old.append(" ")
    else:
        difference = difference * -1
        for follower in range(difference):
            new.append(" ")
    new.sort(key = len, reverse = True)
    lengthkey = len(new[0])
    for follower in new:
        if len(follower) < lengthkey:
            newfollower = follower.rjust(lengthkey, " ")
            print(f"{newfollower}|{old[new.index(follower)]}")
        else:
            print(f"{follower}|{old[new.index(follower)]}")
#Comparator takes the raw following information taken from 
#the old and new followers.txt and extracts useful information
def comparitor(old, new):
    if old == new:
        return "There has been no change to your follower count"
    for follower in old:
        if follower in new:
            new.remove(follower)
            old.remove(follower)
    net = len(new) - len(old)
    print(f"Followers Gained|Lost: {net}")
    list_organizer(old, new, net)

main()