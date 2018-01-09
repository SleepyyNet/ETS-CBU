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

print("ETS-CBU v0.0 alpha Copyright (C) 2018 codemicro")
print("This program comes with ABSOLUTELY NO WARRANTY.")
print("This is free software, and you are welcome to redistribute it")
print("under certain conditions; see LICENCE.txt for details.")
print()
print()

import os
import shutil
import sys
import time
import pyperclip

# gathering required data

print("Please input the username for the target account (see the docs for info).")
username = input(" > ")
directory = "C:/Users/" + username + "/Documents/Euro Truck Simulator 2/profiles/"
print("Is this the correct path? " + directory)
userin = input("y/n: ")
if userin == "n":
    print("Please input the correct directory for your profiles folder.")
    directory = input()

files = ["controls.sii", "gearbox_layout_scania_12.sii", "gearbox_layout_scania_12_2.sii", "gearbox_layout_volvo_12.sii", "gearbox_layout_volvo_12_2.sii", "gearbox_layout_zf_12.sii", "gearbox_layout_zf_16.sii", "gearbox_range.sii", "gearbox_range_splitter.sii", "gearbox_splitter.sii"]

# choosing a profile

dirnumber = 0
listnumber = 1
dirs = os.listdir(directory)
dirlen = len(dirs)
print("Please pick a folder to swap the controller configs.")
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
profdir = directory + profilepath + "/"
os.chdir(profdir)
profcont = os.listdir(profdir)
proflen = len(profcont)

# swap
## create
stage = 0
for i in range(0, proflen):
    if files[stage] in profcont:
        #add to another list
        #advance counter
