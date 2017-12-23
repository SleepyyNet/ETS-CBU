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

print("ETS-CBU v0.1 alpha Copyright (C) 2017  codemicro")
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
genfiles = ["controls.sii.etcbu1", "gearbox_layout_scania_12.sii.etcbu1", "gearbox_layout_12_2.sii.etcbu1", "gearbox_layout_volvo_12.sii.etcbu1", "gearbox_layout_volvo_12_2.sii.etcbu1", "gearbox_layout_zf_12.sii.etcbu1", "gearbox_layout_zf_16.sii.etcbu1", "gearbox_range.sii.etcbu1", "gearbox_range_splitter.sii.etcbu1", "gearbox_splitter.sii.etcbu1", "controls.sii.etcbu2", "gearbox_layout_scania_12.sii.etcbu2", "gearbox_layout_12_2.sii.etcbu2", "gearbox_layout_volvo_12.sii.etcbu2", "gearbox_layout_volvo_12_2.sii.etcbu2", "gearbox_layout_zf_12.sii.etcbu2", "gearbox_layout_zf_16.sii.etcbu2", "gearbox_range.sii.etcbu2", "gearbox_range_splitter.sii.etcbu2", "gearbox_splitter.sii.etcbu2"]
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
profdir = directory + profilepath + "/"
#print(bytearray.fromhex(dirs[userin]).decode())

# ***********************************************************************************
# asking the user what function to do

def swapinit():
    global contofprof, directory, profilepath, profdir
    #print(profdir)
    contofprof = os.listdir(profdir)
    copyfiles = []

    endfileext = ""

    if "controls.sii.etcbu1" in contofprof:
        endfileext = ".etcbu2"
    elif "controls.sii.etcbu2" in contofprof:
        endfileext = ".etcbu1"
    
    if files[0] in contofprof:
        copyfiles.append(files[0])
    if files[1] in contofprof:
        copyfiles.append(files[1])
    if files[2] in contofprof:
        copyfiles.append(files[2])
    if files[3] in contofprof:
        copyfiles.append(files[3])
    if files[4] in contofprof:
        copyfiles.append(files[4])
    if files[5] in contofprof:
        copyfiles.append(files[5])
    if files[6] in contofprof:
        copyfiles.append(files[6])
    if files[7] in contofprof:
        copyfiles.append(files[7])
    if files[8] in contofprof:
        copyfiles.append(files[8])
    if files[9] in contofprof:
        copyfiles.append(files[9])

    #print(copyfiles)
    #input()
    #print(files)
    
    filelen = len(copyfiles)
    filenumber = 0
    
    print("Would you like to begin initiating the swap function? y/n")
    if input(" > ") == "y":
        for i in range(0, filelen):
            print(filenumber)
            os.rename(profdir + files[filenumber], profdir + files[filenumber] + endfileext)
            filenumber = filenumber + 1

def swapinitc():
    global contofprof, directory, profilepath, profdir, genfiles, files
    #print(profdir)
    contofprof = os.listdir(profdir)
    copyfiles = []
    newcopyfiles = []

    endfileext = ""

    if "controls.sii.etcbu1" in contofprof:
        endfileext = ".etcbu2"
    elif "controls.sii.etcbu2" in contofprof:
        endfileext = ".etcbu1"
    else:
        endfileext = ".etcbu1"

    print(endfileext)
    input()
    
    if files[0] in contofprof:
        copyfiles.append(files[0])
    if files[1] in contofprof:
        copyfiles.append(files[1])
    if files[2] in contofprof:
        copyfiles.append(files[2])
    if files[3] in contofprof:
        copyfiles.append(files[3])
    if files[4] in contofprof:
        copyfiles.append(files[4])
    if files[5] in contofprof:
        copyfiles.append(files[5])
    if files[6] in contofprof:
        copyfiles.append(files[6])
    if files[7] in contofprof:
        copyfiles.append(files[7])
    if files[8] in contofprof:
        copyfiles.append(files[8])
    if files[9] in contofprof:
        copyfiles.append(files[9])

    print(copyfiles)
    input()
    #print(files)
    
    filelen = len(copyfiles)
    filenumber = 0
    
    print("Would you like to begin initiating the swap copy function? y/n")
    if input(" > ") == "y":
        for i in range(0, filelen):
            #print(filenumber)
            os.rename(profdir + files[filenumber], profdir + files[filenumber] + endfileext)
            filenumber = filenumber + 1
        contofprof = os.listdir(profdir)
        
        if genfiles[0] in contofprof:
            newcopyfiles.append(genfiles[0])
        if genfiles[1] in contofprof:
            newcopyfiles.append(genfiles[1])
        if genfiles[2] in contofprof:
            newcopyfiles.append(genfiles[2])
        if genfiles[3] in contofprof:
            newcopyfiles.append(genfiles[3])
        if genfiles[4] in contofprof:
            newcopyfiles.append(genfiles[4])
        if genfiles[5] in contofprof:
            newcopyfiles.append(genfiles[5])
        if genfiles[6] in contofprof:
            newcopyfiles.append(genfiles[6])
        if genfiles[7] in contofprof:
            newcopyfiles.append(genfiles[7])
        if genfiles[8] in contofprof:
            newcopyfiles.append(genfiles[8])
        if genfiles[9] in contofprof:
            newcopyfiles.append(genfiles[9])

        print(newcopyfiles)
        input()

        newfilelen = len(newcopyfiles)
        filenumber = 0

        for i in range(0, filelen):
            #print(filenumber)
            shutil.copy2(profdir + genfiles[filenumber] + endfileext, profdir + files[filenumber] + ".sii")
            filenumber = filenumber + 1

def swap():
    global contofprof, directory, profilepath, profdir
    #print(profdir)
    contofprof = os.listdir(profdir)
    copyfiles = []

    endfileext = ""

    if "controls.sii.etcbu1" in contofprof:
        endfileext = ".etcbu2"
    elif "controls.sii.etcbu2" in contofprof:
        endfileext = ".etcbu1"

    #checking to see if there are any prexisting .etcbu files
    genfilecount = 0
    '''
    for i in range(0, len(contofprof)):    
        if genfiles[genfilecount] in contofprof:
            print("There are already alternative files in this directory!")
            print("Aborting script in three seconds.")
            time.sleep(3)
            sys.exit()
        genfilecount = genfilecount + 1
    '''    
    #indexing original control files
    if files[0] in contofprof:
        copyfiles.append(files[0])
    if files[1] in contofprof:
        copyfiles.append(files[1])
    if files[2] in contofprof:
        copyfiles.append(files[2])
    if files[3] in contofprof:
        copyfiles.append(files[3])
    if files[4] in contofprof:
        copyfiles.append(files[4])
    if files[5] in contofprof:
        copyfiles.append(files[5])
    if files[6] in contofprof:
        copyfiles.append(files[6])
    if files[7] in contofprof:
        copyfiles.append(files[7])
    if files[8] in contofprof:
        copyfiles.append(files[8])
    if files[9] in contofprof:
        copyfiles.append(files[9])
    #print(copyfiles)
    input()
    #print(files)
    filelen = len(copyfiles)
    filenumber = 0
    print("Would you like to begin swapping the controller layouts? y/n")
    if input(" > ") == "y":
        for i in range(0, filelen):
            print(filenumber)
            os.rename(profdir + files[filenumber], profdir + files[filenumber] + endfileext)
            filenumber = filenumber + 1
print("Please input command for the profile " + bytearray.fromhex(dirs[userin]).decode() + "?")
while True:
    userfunction = input(">> ")

    if userfunction == "swap init":
        swapinit()
        continue
    elif userfunction == "swap init -c":
        swapinitc()
        continue
    elif userfunction == "swap":
        swap()
        continue

    elif userfunction == "exit":
        sys.exit()
    
