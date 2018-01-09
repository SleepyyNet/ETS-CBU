Quickstart
===============

Please first read the requirements!

When you first start the script, you will be asked for the name of the user account
::
   Please input the username for the target account.
    >

This is the name of the user folder found at C:\\Users\\. For example, C:\\Users\\Joe would be
::
   Please input the username for the target account.
    > Joe

You will then be asked to select the profile that you want to perform the functions in. For sync, this will be the profile that you want to synchronise from.
	
After that, you will be presented with a command line style interface. At present there is not a help command, you will have to look at the commands section of the documentation.
	
At present, there are only three functions built into the script. They are:

* Swap
   * This will swap two sets of controller layouts. Simple.
* Backup
   * This will save the controller layouts to a .zip file, so you can do something with it and store it away somewhere.
* Sync
   * This will synchronise the controller configs from one profile into any other profiles you might want it in.
   
Swap
^^^^

The first time you use swap, you need to initialise it. You can do this by runninng
::
   sync init

This will make the current controller layouts into an .etcbu1 or an .etcbu2 file. You then start ETS2 in that profile, which will create new controller layout files. By doing this you are making the game think that there are not controller layouts and it will create a fresh, new, set of controller layouts.

As an alternative, if you wish to clone the controller layouts instead of starting fresh, you can do
::
   sync init -c
   
Doing that will create the .etcbu1 or .etcbu2 but also leave the pre-existing controller files in the profile, so you will not have to start over fresh when you next load the game.