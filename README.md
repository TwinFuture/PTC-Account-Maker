# PTC-Account-Maker
Automactially Create as many PTC accounts as you wish!

#Installation Guide
####REQUIRES GOOGLE CHOME PYTHON AND SELENIUM, MAKE SURE YOU HAVE THIS INSTALLED!

First download and install python for windows!
When installing click more / advanced and select all options
Link: https://www.python.org/ftp/python/3.5.2/python-3.5.2-amd64.exe

PLEASE NOTE WHERE PYTHON IS BEING INSTALLED TO, YOU WILL NEED THIS DIRECTORY LATER!

One python is installed, you now need to install a module for python!

To do this on your desktop press the start button on the bottom left and search for command prompt.
Once you have command prompt open we need to type in cd and the directory you have python installed!

EG 
#####cd C:\Users\TwinFuture\AppData\Local\Programs\Python\Python35

If you didn't note the location down, you can find it by following these steps.
Go to the start button again and search for python, right click python and press go to file location.
This will take you to another folder with shortcuts, right click the shortcut and hit properties then go to file location again.
This is where python is installed.
In you windows explorer, where you see all the python files is an address bar, click in this and copy it.
Type cd into command prompt and paste the location you just copied from your windows explorer address bar.

The rest is easy :)
Now once we are in our location within command prompt we then just need to type 
pip.exe install selenium
Once this is done installing, we can now go back to the original download and open our accounts.txt file

Now we need to add some account names to a list which we want to create we add a desired username on each line. eg;
Pokemon1
Pokemon2
Pokemon3

Now we can right click
PTC-ACC-GENERATOR.py
Select edit with IDLE
Once IDLE is opened, have a look at the password and country, you might wanna change these I WOULD!

The email address I would recommend you keep it the same unless you have a domain name with a catch all
As it uses your accountnameLIST@uniquez-home.com

Once you have changed the the password mainly in PTC-ACC-GENERATOR.py as that's all we really need to change.
We can now hit f5 and watch it start creating your pokemon accounts.

Once an account has been created you will see it in created.txt :)

Any bugs, please let me know! I have just mocked this up within a few hours as I wanted something like this myself that I can trust.

I THINK THAT'S ALL, ENJOY!


