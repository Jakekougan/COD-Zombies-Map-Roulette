#Import the useful modules 
import random
import tkinter as tk
from tkinter import *
import os
from pygame import mixer
import sys


#Creating the Keys for the dictionary that will store our images as corresponding values 
codz_dic = {}
bo1_maps = ['Nacht Der Untoten', 'Verruckt', 'Shi No Numa', 'Der Riese', 'Kino Der Toten', 'Five', 'Ascension', 'Call of the Dead', 'Shangri-La', 'Moon']
bo2_maps = ['Tranzit', 'Town', 'Bus Depot', 'Farm', 'Die Rise', 'Nuketown', 'Mob of the Dead', 'Buried', 'Origins']
bo3_maps = ['Shadows of Evil', 'The Giant', 'Der Eisendrache', 'Zetsubou no Shima', 'Gorod Krovi', 'Revelations','Nacht Der Untoten(BO3)', 'Verruckt(BO3)', 'Shi no Numa(BO3)', 'Kino Der Toten(BO3)', 'Ascension(BO3)', 'Shangri-La(BO3)', 'Moon(BO3)', 'Origins(BO3)' ]
bo4_maps = ['IX', 'Voyage of Despair', 'Blood of the Dead', 'Classified', 'Dead of the Night', 'Ancient Evil', 'Alpha Omega', 'Tag Der Toten']
cw_maps = ['Die Machine', 'Firebase Z', 'Maur Der Toten', 'Forsaken']
bo6_maps = ["Liberty Falls", "Terminus", "Citadelle des Morts"]

#This is to help keep track of which games have certain maps
codz_dic['Black Ops 1'] = bo1_maps
codz_dic['Black Ops 2'] = bo2_maps
codz_dic['Black Ops 3'] = bo3_maps
codz_dic['Black Ops 4'] = bo4_maps
codz_dic['Black Ops Cold War'] = cw_maps
codz_dic['Black Ops 6'] = bo6_maps


#Turns the codz_dic into a master list of every 3arc zombies map
def lst_combined():
    all_maps = []
    lsts = list(codz_dic.values())
    for i in range(len(lsts)):
        for item in lsts[i]:
            if item in all_maps:
                remastered = item + " (BO3)"
                all_maps.append(remastered)
            all_maps.append(item)
    return all_maps

#Make them usable within our functions

all_maps = lst_combined()


#Make it so the map names and map image files are both in alphabetically order for easier assignment 
all_maps.sort()
all_maps

# Determine the absolute path to the directory containing the executable 
if hasattr(sys, '_MEIPASS'):
     base_path = sys._MEIPASS 
else: 
    base_path = os.path.abspath(os.path.dirname(__file__))


#Loading in the assests
img_dir = os.path.join(base_path, 'corrected_imgs')
sound_dir = os.path.join(base_path, 'Sounds and Music')
main_dir =  os.path.join(base_path, "main_image")
correct_imgs = os.listdir(img_dir) 
maps_dic = {all_maps[j]: os.path.join(img_dir, correct_imgs[j]) for j in range(len(correct_imgs))}

 
    



#Establishes root window in tkinter
r = Tk()
   
#All Maps
def map_roulette_ALL():
    map = random.choice(all_maps)
    map_img = maps_dic.get(map)
    
    #Display
    top = Toplevel()
    top.geometry("180x85")
    top.title("Results")
    top.attributes('-fullscreen', True)

    map_img = maps_dic.get(map)
    print(f"Selected map: {map}")
    print(f"Selected Image: {map_img}")

    if map_img is not None:
        img = PhotoImage(file=map_img)
        img_display = Label(top, image=img)
        img_display.image = img_display
        img_display.place(x=0, y=0)

    label = Label(top, text="The map you've gotten is   ")
    resultLabel = Label(top, text=map)
    closing_time = Button(top, text="Close", command=top.destroy)

    label.pack()
    resultLabel.pack()
    closing_time.pack()
    

    top.mainloop()
   
def BO1():
    lsts = list(codz_dic.values())
    map = random.choice(lsts[0])
   

    #Display
    top = Toplevel()
    top.geometry("180x85")
    top.title("Results")
    top.attributes('-fullscreen', True)

    map_img = maps_dic.get(map)
    print(f"Selected map: {map}")
    print(f"Selected Image: {map_img}")

    if map_img is not None:
        img = PhotoImage(file=map_img)
        img_display = Label(top, image=img)
        img_display.image = img_display
        img_display.place(x=0, y=0)

    label = Label(top, text="The map you've gotten is   ")
    resultLabel = Label(top, text=map)
    closing_time = Button(top, text="Close", command=top.destroy)

    label.pack()
    resultLabel.pack()
    closing_time.pack()
    

    top.mainloop()

def BO2():
    lsts = list(codz_dic.values())
    map = random.choice(lsts[1])
   

    #Display
    top = Toplevel()
    top.geometry("180x85")
    top.title("Results")
    top.attributes('-fullscreen', True)

    map_img = maps_dic.get(map)
    print(f"Selected map: {map}")
    print(f"Selected Image: {map_img}")

    if map_img is not None:
        img = PhotoImage(file=map_img)
        img_display = Label(top, image=img)
        img_display.image = img_display
        img_display.place(x=0, y=0)

    label = Label(top, text="The map you've gotten is   ")
    resultLabel = Label(top, text=map)
    closing_time = Button(top, text="Close", command=top.destroy)

    label.pack()
    resultLabel.pack()
    closing_time.pack()
    

    top.mainloop()

def BO3():
    lsts = list(codz_dic.values())
    map = random.choice(lsts[2])
   

    #Display
    top = Toplevel()
    top.geometry("180x85")
    top.title("Results")
    top.attributes('-fullscreen', True)

    map_img = maps_dic.get(map)
    print(f"Selected map: {map}")
    print(f"Selected Image: {map_img}")

    if map_img is not None:
        img = PhotoImage(file=map_img)
        img_display = Label(top, image=img)
        img_display.image = img_display
        img_display.place(x=0, y=0)

    label = Label(top, text="The map you've gotten is   ")
    resultLabel = Label(top, text=map)
    closing_time = Button(top, text="Close", command=top.destroy)

    label.pack()
    resultLabel.pack()
    closing_time.pack()
    

    top.mainloop()
    
def BO4():
    lsts = list(codz_dic.values())
    map = random.choice(lsts[3])
   

    #Display
    top = Toplevel()
    top.geometry("180x85")
    top.title("Results")
    top.attributes('-fullscreen', True)

    map_img = maps_dic.get(map)
    print(f"Selected map: {map}")
    print(f"Selected Image: {map_img}")

    if map_img is not None:
        img = PhotoImage(file=map_img)
        img_display = Label(top, image=img)
        img_display.image = img_display
        img_display.place(x=0, y=0)

    label = Label(top, text="The map you've gotten is   ")
    resultLabel = Label(top, text=map)
    closing_time = Button(top, text="Close", command=top.destroy)

    label.pack()
    resultLabel.pack()
    closing_time.pack()
    

    top.mainloop()

def BOCW():
    lsts = list(codz_dic.values())
    map = random.choice(lsts[4])
   

    #Display
    top = Toplevel()
    top.geometry("180x85")
    top.title("Results")
    top.attributes('-fullscreen', True)

    map_img = maps_dic.get(map)
    print(f"Selected map: {map}")
    print(f"Selected Image: {map_img}")

    if map_img is not None:
        img = PhotoImage(file=map_img)
        img_display = Label(top, image=img)
        img_display.image = img_display
        img_display.place(x=0, y=0)

    label = Label(top, text="The map you've gotten is   ")
    resultLabel = Label(top, text=map)
    closing_time = Button(top, text="Close", command=top.destroy)

    label.pack()
    resultLabel.pack()
    closing_time.pack()
    

    top.mainloop()

def BO6():
    lsts = list(codz_dic.values())
    map = random.choice(lsts[5])
   

    #Display
    top = Toplevel()
    top.geometry("180x85")
    top.title("Results")
    top.attributes('-fullscreen', True)

    map_img = maps_dic.get(map)
    print(f"Selected map: {map}")
    print(f"Selected Image: {map_img}")

    if map_img is not None:
        img = PhotoImage(file=map_img)
        img_display = Label(top, image=img)
        img_display.image = img_display
        img_display.place(x=0, y=0)

    label = Label(top, text="The map you've gotten is   ")
    resultLabel = Label(top, text=map)
    closing_time = Button(top, text="Close", command=top.destroy)

    label.pack()
    resultLabel.pack()
    closing_time.pack()
    

    top.mainloop()

#Create the User Interface

r.geometry("250x170")
r.title('COD Zombies Map Roulette')
img = PhotoImage(file=os.path.join(main_dir, "96203.png"))
img1 = Label(r, image=img)
img1.place(x=0,y=0)
r.attributes('-fullscreen', True)

#Background Music
mixer.init()
mixer.music.load(os.path.join(sound_dir, "Samantha's Lullaby.mp3"))
mixer.music.play(-1)



scree_txt = 'Welcome to Map Roullette! Choose "ALL MAPS" to randomly choose a map from all games!\n\nChoose a specific game to get a random map from that game!\n'
message = tk.Message(r, text=scree_txt)

   

button1 = Button(r, text='ALL MAPS', command=map_roulette_ALL)
button2 = Button(r, text='Black Ops 1', command=BO1)
button3 = Button(r, text='Black Ops 2', command=BO2)
button4 = Button(r, text='Black Ops 3', command=BO3)
button5 = Button(r, text='Black Ops 4', command=BO4)
button6 = Button(r, text='Black Ops Cold War', command=BOCW)
button7 = Button(r, text='Black Ops 6', command=BO6)
button_exit = Button(r, text= "Exit", command= r.destroy)







message.pack(pady=10)
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)
button4.pack(pady=10)
button5.pack(pady=10)
button6.pack(pady=10)
button7.pack(pady=10)
button_exit.pack(pady=75)



#Result Window

r.mainloop()
mixer.music.stop()