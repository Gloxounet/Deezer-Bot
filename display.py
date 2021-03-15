import clear
import mainprogram
import random
import sys
import txtconverter


###FONCTIONS :#######################################################################################

def while_int_condition(n1,n2) :
    x = input()
    while not(n1<=int(x)<=n2)  :
        print("Please enter a proper input")
        x = input()
    return(int(x))

def print_choice_list(liste) :
    for i,elem in enumerate(liste) :
        string = (((elem.__repr__())[1:-1]).split(" ",1))[1]
        print("{}: ".format(i) + string)
    print("")   

###PROGRAMME :#######################################################################################

#Clear console
clear.clear()

#Intro
print("-----------------------------------------------")
print("Welcome to the deezer to clip board .py program")
print("-----------------------------------------------")
print("Please choose your desired user (from {} to {}): \n".format(0,len(mainprogram.user_list)-1))

#Display users
for index,e in enumerate(mainprogram.user_list) :
    print("{}: ".format(index) + e[1])
print("")

#Get user
int_user = while_int_condition(0,len(mainprogram.user_list)-1)
user     = mainprogram.get_user(mainprogram.user_list[int_user][0])

#Clear console
clear.clear()

print("Please make your selection :")
print("0: Playlist\n1: Favorite\n")

int_mode = while_int_condition(0,1)

#Clear console
clear.clear()

#Get tracks from a selected playlist :
if int_mode == 0 :
    #Get playlists
    playlists = mainprogram.get_playlists(user)
    
    #Print playlists choice
    print("Please choose your playlist :\n")
    print_choice_list(playlists)

    int_tracks = while_int_condition(0,len(playlists)-1)
    tracks     = mainprogram.get_tracks(playlists[int_tracks])

if int_mode == 1 :
    #Get favorite
    tracks = mainprogram.get_favorite(user)

#Clear console
clear.clear()

#Randomize or not the lecture, track limit :
print("Would you randomize the lecture ?")
print("0: No \n1: Yes \n")

alea = while_int_condition(0,1)

if alea == 1 :
    random.shuffle(tracks)

#Clear console
clear.clear()

print("Would you set a tracks number limit ?")
print("0: No \n1: Yes \n")

l = while_int_condition(0,1)

if l == 1 :
    lim = while_int_condition(0,len(tracks)-1)
    tracks = tracks[:lim]

#Clear console
clear.clear()

string_track_list = txtconverter.get_str_from_list(tracks)

print("Enter 0 when you are ready :")
temp = while_int_condition(0,0)

#Clear console
clear.clear()

txtconverter.paste_list(string_track_list)




