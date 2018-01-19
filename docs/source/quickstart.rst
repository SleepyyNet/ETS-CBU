Quickstart
===============

When you first start the script, you need to locate your Euro Truck Simlator 2 folder, for example C:\\Users\\yourusernamehere\\Documents\\Euro Truck Simlator 2.

You will then be asked to select the profile that you want to perform the functions in. (For sync, this will be the profile that you want to synchronise from)
	
After that, you will be presented with a command line style interface. At present there is not a help command, you will have to look at the commands section of the documentation.
	
At present, there are only three functions built into the script. They are:

* Swap
   * This provides the ability to create and load saves of controller layouts to any profile.
* Backup
   * This will save the controller layouts to a .zip file, so you can do something with it and store it away somewhere. This feature is not availavle in version 0.0.1 alpha.
* Sync
   * This will synchronise the controller configs from one profile into any other profiles you might want it in. This feature is not available in version 0.0.1 alpha.
   
Swap
^^^^

To create a backup that can be used with any profile, type
::
   swap create

And follow the onscreen instructions.

If you want to load the saves you made of the controller layouts, you can run
::
   swap load
   
This will list all the available saves found in the folder that is created by the program in your ETS2 folder. You can then choose a save to load, and once you select it, the program will load it for you.
