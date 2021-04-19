from dearpygui.core import *
from dearpygui.simple import *

#functions.py Imports
from functions import get_available_user_from_txt ,get_playlists_name_list,get_playlists,get_tracks,print_track_list
import function_spotify as s

#USEFUL VARIABLES
user_list      = []
plateform_list = []
playlist_list  = []
plateform_list = ["Deezer","Spotify"]

#DISPLAY VARIABLES
display_plateform_list = ["Deezer","Spotify"]
display_user_list      = []
display_playlist_list  = []
tracks         = []

def refresh():
    configure_item('User', items=display_user_list)
    configure_item('Playlist', items=display_playlist_list)

def callback_plateform_users(sender,data) :
    global user_list
    global display_user_list
    global playlist_list
    global display_playlist_list
    global plateform_list

    with window("Quick Play Discord") :
        choosen_platform = plateform_list[get_value("Plateform")]
        print(choosen_platform)
        user_list = get_available_user_from_txt(choosen_platform)
        display_user_list = [i[1] for i in user_list]
        playlist_list = []
        display_playlist_list = []
        refresh()

def callback_user_playlist(sender,data):
    global playlist_list
    global display_playlist_list

    with window("Quick Play Discord") :
        choosen_user = get_value("User")
        choosen_platform = plateform_list[get_value("Plateform")]
        user = user_list[choosen_user][0]
        if choosen_platform == "Deezer" :
            playlist_list = get_playlists(user)
            display_playlist_list = get_playlists_name_list(playlist_list)
        elif choosen_platform == "Spotify" :
            playlist_list = s.get_playlists(user)
            clean_playlist = s.list_playlists(playlist_list)
            display_playlist_list = [i[1] for i in clean_playlist]
        else :
            raise NameError('Invalid plateform')
        refresh()

def callback_playlist_tracks(sender,data):
    global tracks

    with window("Quick Play Discord") :
        choosen_platform = plateform_list[get_value("Plateform")]
        choosen_playlist = get_value("Playlist")
        if choosen_platform == "Deezer" :
            tracks = get_tracks(playlist_list[choosen_playlist])
        elif choosen_platform == "Spotify" :
            tracks = s.get_tracks((s.list_playlists(playlist_list))[choosen_playlist][0])
        else :
            raise NameError('Invalid plateform')

        refresh()

def callback_start(sender,data):
    global tracks
    choosen_platform = plateform_list[get_value("Plateform")]
    with window("Quick Play Discord") :
        #Order fix
        order      = get_value("Pick Most Recent First")
        if order :
            tracks.reverse()

        wait_time  = get_value("Wait time")
        randomizer = get_value("Randomise")
        limitation = get_value("Track limit")
        prefix     = get_value("Prefix")
        
        print_track_list(track_list=tracks,limitation=limitation,randomise=randomizer,prefix=prefix,plateform=choosen_platform,t=wait_time)


#window object settings
set_main_window_size(540, 720)
set_global_font_scale(1)
set_theme("Gold")
set_style_window_padding(30,30)

with window("Quick Play Discord", width=520, height=670):
    print("GUI is running...")
    set_window_pos("Quick Play Discord", 0, 0)

    #image logo
    add_drawing("logo", width=520, height=100) #create some space for the image

    add_separator()
    add_spacing(count=12)
    #text instructions
    add_text("Please choose your settings and click start when you are ready",
    color=[232,163,33])
    add_spacing(count=12)
    add_separator()
    add_spacing(count=6)
    add_text("Main settings",
    color=[232,163,33])
    add_spacing(count=6)
    #itemlist
    add_listbox("Plateform",items=display_plateform_list,num_items=2,callback=callback_plateform_users)
    add_listbox("User"     ,items=display_user_list     ,num_items=3,callback=callback_user_playlist  )
    add_listbox("Playlist" ,items=display_playlist_list ,num_items=3,callback=callback_playlist_tracks)

    add_spacing(count=12)
    add_separator()
    add_spacing(count=6)
    add_text("Extras",
    color=[232,163,33])
    add_spacing(count=6)
    #tickbox
    add_checkbox("Randomise")

    #order
    add_checkbox("Pick Most Recent First")

    #inputbox
    add_input_int("Track limit", default_value=5)

    #inputtimefreeze
    add_input_float("Wait time", default_value=0.5)

    #prefixbox
    add_input_text("Prefix", default_value="/play")

    add_spacing(count=12)
    add_separator()
    add_spacing(count=12)
    #action button
    add_button("Start",callback=callback_start)

#place the image inside the space
draw_image("logo", "logo_quickplay.png", [0,0], [450,90])

start_dearpygui()