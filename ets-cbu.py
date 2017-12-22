'''
    ETS-CBU is a program to manage ETS2 and ATS controller layouts.
    Copyright (C) 2017 codemicro

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

print("ETS-CBU v0.1 alpha Copyright (C) 2017 codemicro")
print("This program comes with ABSOLUTELY NO WARRANTY.")
print("This is free software, and you are welcome to redistribute it")
print("under certain conditions; see LICENCE.txt for details.")
print()
print()

import os
import shutil
import sys
import time

# ***********************************************************************************
# sorting out all the vars

print("Please input the username for the target account (see information.pdf or readme.md for info).")
username = input(" > ")
directory = "C:/Users/" + username + "/Documents/Euro Truck Simulator 2/profiles/"
#print(directory)
dirnumber = 0
listnumber = 1
dirs = os.listdir(directory)
#print(dirs)
dirlen = len(dirs)
files = ["controls.sii", "gearbox_layout_scania_12.sii", "gearbox_layout_scania_12_2.sii", "gearbox_layout_volvo_12.sii", "gearbox_layout_volvo_12_2.sii", "gearbox_layout_zf_12.sii", "gearbox_layout_zf_16.sii", "gearbox_range.sii", "gearbox_range_splitter.sii", "gearbox_splitter.sii"]
genfiles = ["controls.sii.etcbu", "gearbox_layout_scania_12.sii.etcbu", "gearbox_layout_12_2.sii.etcbu", "gearbox_layout_volvo_12.sii.etcbu", "gearbox_layout_volvo_12_2.sii.etcbu", "gearbox_layout_zf_12.sii.etcbu", "gearbox_layout_zf_16.sii.etcbu", "gearbox_range.sii.etcbu", "gearbox_range_splitter.sii.etcbu", "gearbox_splitter.sii.etcbu"]
#bytearray.fromhex("7061756c").decode()
#shutil.move('test.txt', 'newtest.txt')

# ***********************************************************************************
# asking the user what profile to use

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
print(bytearray.fromhex(dirs[userin]).decode())

# ***********************************************************************************
# asking the user what function to do

print("Would you like to BACKUP, SWAP, or SYNC your controller layouts for the profile " + bytearray.fromhex(dirs[userin]).decode() + "?")
userfunction = input(" > ")

# ***********************************************************************************
# performing the functions

if userfunction == "SWAP" or "swap" or "Swap":
    profdir = directory + profilepath + "/"
    #print(profdir)
    contofprof = os.listdir(profdir)
    copyfiles = []

    #checking to see if there are any prexisting .etcbu files
    genfilecount = 0
    for i in range(0, len(contofprof)):    
        if genfiles[genfilecount] in contofprof:
            print("There are already alternative files in this directory!")
            print("Aborting script in three seconds.")
            time.sleep(3)
            sys.exit()
        genfilecount = genfilecount + 1
        
    #indexing original control files
    if files[0] in contofprof:
        copyfiles.append(files[0])
    if files[1] in contofprof:
        copyfiles.append("gearbox_layout_scania_12.sii")
    if files[2] in contofprof:
        copyfiles.append("gearbox_layout_scania_12_2.sii")
    if files[3] in contofprof:
        copyfiles.append("gearbox_layout_volvo_12.sii")
    if files[4] in contofprof:
        copyfiles.append("gearbox_layout_volvo_12_2.sii")
    if files[5] in contofprof:
        copyfiles.append("gearbox_layout_zf_12.sii")
    if files[6] in contofprof:
        copyfiles.append("gearbox_layout_zf_16.sii")
    if files[7] in contofprof:
        copyfiles.append("gearbox_range.sii")
    if files[8] in contofprof:
        copyfiles.append("gearbox_range_splitter.sii")
    if files[9] in contofprof:
        copyfiles.append("gearbox_splitter.sii")
    #print(copyfiles)
    input()
    #print(files)
    filelen = len(copyfiles)
    filenumber = 0
    print("Would you like to begin swapping the controller layouts? y/n")
    if input(" > ") == "y":
        for i in range(0, filelen):
            print(filenumber)
            os.rename(profdir + files[filenumber], profdir + files[filenumber] + ".etcbu")
            filenumber = filenumber + 1
    else:
        sys.exit()
