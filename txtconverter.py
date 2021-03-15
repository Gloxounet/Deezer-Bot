import keyboard
import clear
import time


###FONCTIONS :##########################################################

def get_available_user_from_txt() :
    user_list = []

    with open("user.txt", "r") as f :
        for x in f :
            user_list.append((x[:10],x[11:].replace("\n","")))
    
    return(user_list)

def get_artist(track):
    string = (track.get_artist()).__repr__()
    string = string[1:-1]
    string = string.split(" ",1)
    return(string[1])

def get_title(track):
    string = track.__repr__()
    string = string[1:-1]
    string = string.split(" ",1)
    return(string[1])

def get_str_from_list(liste) :
    for i,track in enumerate(liste) :
        title  = get_title(track)
        author = get_artist(track)
        liste[i] = title + " " + author

    return(liste)

def paste_list(liste,p="!p "):
    #Clear console
    clear.clear()
    print("Be ready for the pasting, starting in 5 sec...")
    time.sleep(5)
    for x in liste :
        x = p + x
        keyboard.write(x)
        time.sleep(0.1)
        keyboard.press_and_release('enter')
        time.sleep(0.3)

###PROGRAMME :##########################################################

if __name__ == "__main__" : 
    pass
