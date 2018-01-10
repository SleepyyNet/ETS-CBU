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

    If you wish to contact me concerning this program, drop me a line at:
        thomasdpain@gmail.com
    and I'll do my best to respond in a timely manner.
'''

version = "0.0a"

print("ETS-CBU v0.0 alpha Copyright (C) 2018 codemicro")
print("This program comes with ABSOLUTELY NO WARRANTY.")
print("This is free software, and you are welcome to redistribute it")
print("under certain conditions; see LICENCE.txt for details.")
print()
print()

import os, shutil, sys, time, zipfile #, win32con, win32api # stock libraries
import easygui # included libraries
import confgen # custom libraries

# gathering required data

print("Please locate your ETS2 folder.")
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
        #win32api.SetFileAttributes(directory + "\\etscbu.backups", win32con.FILE_ATTRIBUTE_HIDDEN)

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
	# reading all saves in backup dir
	bulist = os.listdir(directory + "\\etscbu.backups\\")
	print(directory + "\\etscbu.backups\\")
	print(bulist)
    # list saves by current profile (profile names need to be taken from .conf and turned from hex to a string, the printed)
    # allow the loading of saves

# TODO swap load -a
    # list saves from ALL profiles
    # allow the loading of saves

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
        continue
    elif userfunction == "swap":
        print("Usage: \nswap create \n    Saves the current state of the controller layouts for that profile. \nswap load \n    Loads a controller save.")
        continue
    # essential stuff
    elif userfunction == "exit":
        sys.exit()
    else:
        print("Not a valid command!")
