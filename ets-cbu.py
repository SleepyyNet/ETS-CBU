'''
    ETS-CBU is a program to manage ETS2 controller layouts.
    Copyright (C) 2018 codemicro

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.

'''

version = "0.0a"

print("ETS-CBU v0.0 alpha Copyright (C) 2018 codemicro")
print("This program comes with ABSOLUTELY NO WARRANTY.")
print("This is free software, and you are welcome to redistribute it")
print("under certain conditions; see LICENCE.txt for details.")
print()
print()

import os, shutil, sys, time, zipfile # stock libraries
import easygui # included libraries
import confgen # custom libraries

# gathering required data

print("Please locate your ETS2 folder.")
time.sleep(2)
directory = easygui.diropenbox() + "\\"
print(directory)

files = ["controls.sii", "gearbox_layout_scania_12.sii", "gearbox_layout_scania_12_2.sii", "gearbox_layout_volvo_12.sii", "gearbox_layout_volvo_12_2.sii", "gearbox_layout_zf_12.sii", "gearbox_layout_zf_16.sii", "gearbox_range.sii", "gearbox_range_splitter.sii", "gearbox_splitter.sii"]

# choosing a profile

dirnumber = 0
listnumber = 1
dirs = os.listdir(directory + "\\profiles\\")
dirlen = len(dirs)
print("Please pick a folder to change the controller configs.")
for i in range(0, dirlen):
    profilename = bytearray.fromhex(dirs[dirnumber]).decode()
    print(listnumber, ": ", profilename)
    listnumber = listnumber + 1
    dirnumber = dirnumber + 1
print("Please input a number.")
userin = input(" > ")
userin = int(userin)
userin = userin - 1
profilepath = dirs[userin]
profdir = directory + "profiles\\" + profilepath + "\\"
os.chdir(profdir)
profcont = os.listdir(profdir)
proflen = len(profcont)
filelen = len(files)

# swap
## create
def swapcreate():
    global profilepath, profdir
    
    copyfiles = []

    stage = 0
    for i in range(0, filelen): # making a variable saying what there is in that profile
        if files[stage] in profcont:
            copyfiles.append(files[stage])
            stage = stage + 1

    if os.path.exists(directory + "\\etscbu.backups") == False: # if it isn't aready there, make it and make it hidden
        os.makedirs(directory + "\\etscbu.backups")

    zipname = input("Save name: ") # asking for save name
    newZip = zipfile.ZipFile(directory + "\\etscbu.backups\\" + zipname + ".etcs", "w") # creating the zip
    
    stage = 0
    confgen.make(profdir, zipname, profilepath, version) #making the .conf file
    copyfiles.append(".conf")
    filelen2 = len(copyfiles)
    for i in range(0, filelen2):
        newZip.write(copyfiles[stage], compress_type=zipfile.ZIP_STORED)
        stage = stage + 1
    os.unlink(profdir + "\\.conf") # delete the old .conf
    newZip.close() # finishing with the zip
    print("Save successfully created!") # output final result

# TODO swap load

def swapload():
    global directory, profdir
	# reading all saves in backup dir
    bulist = os.listdir(directory + "\etscbu.backups\\")
    print(directory + "\etscbu.backups\\")
    print(bulist)
    bulen = len(bulist)

    if bulen == 0:
        print("There are no saves available!")
    elif bulen > 0:
        stage = 0
        ok = []
        for i in range(0, bulen):
            if bulist[stage].endswith(".etcs") == True:
                ok.append(bulist[stage])
            stage = stage + 1
        print(ok)
        
        oklen = len(ok)
        stage = 0
        listnumberx = 1

        print("Please choose a save.")
        for i in range(0, oklen):
            target = zipfile.ZipFile(directory + "etscbu.backups\\" + ok[stage])
            target.extract(".conf")
            targetconf = open(".conf", "r")
            #lines = targetconf.readlines()
            #targetline = lines[0]
            listnumberxstr = str(listnumberx)
            savename = targetconf.readlines()[0][9:].rstrip("\n")
            print(listnumberxstr + ": " + savename)
            #listobj = ["placeholder to use up 0"]
            targetconf.close()
            os.unlink(".conf")
            stage = stage + 1
            listnumberx = listnumberx + 1

        print("Please input a number.")
        userin = input(" > ")
        userin = int(userin)
        userin = userin - 1
        chosensave = ok[userin]
        loadsave = directory + "etscbu.backups\\" + chosensave
        extractref = zipfile.ZipFile(loadsave, 'r')
        extractref.extractall(profdir)
        extractref.close()
        os.unlink(profdir + "\\.conf") # delete the old .conf

# TODO update docs

# cli like interface
print()
print("Please input command for the profile " + bytearray.fromhex(dirs[userin]).decode() + ".")
while True:
    userfunction = input(">> ")

    if userfunction == "swap create":
        swapcreate()
        continue
    elif userfunction == "swap load":
        swapload()
        #todo SWAP LOAD
        continue
    elif userfunction == "swap":
        print("Usage: \nswap create \n    Saves the current state of the controller layouts for that profile. \nswap load \n    Loads a controller save.")
        continue
    # essential stuff
    elif userfunction == "exit":
        sys.exit()
    else:
        print("Not a valid command!")
