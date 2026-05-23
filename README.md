Tutorial for my friends :>

## Overview
Makes a list of Instagram users you are following that don't follow you back.

Basically, we're just getting the lists of your followers and following, and then cleaning + comparing the lists with python.

# Instructions

### Make sure you have python installed:

python <a href="https://www.python.org/downloads/">(Python Download)</a>

- add python to PATH when the option appears

## 1. Get Instagram data
### Begin Export
1. Go to <a href="https://accountscenter.instagram.com/">accountscenter.instagram.com</a>

2. Go to "Your information and permissions" and click "Export your information"

    <img src="assets/exportyour.png" width="450"/>

3. Click "Create export", select your Instagram account, and click "Export to device"

4. Choose the following settings:

    <img src="assets/exportsettings.png" width="450"/>

5. Click "Start export" and enter your password

### Download data
1. After a few minutes you should get an email that looks like this:

    <img src="assets/email.png" width="400"/>

    Click the link that says "export your information"

2. Download your information

    <img src="assets/downloads.png" width="400"/>

3. Unzip the folder that you just downloaded (We'll call this folder MYDATA)


## 2. Clean and compare the data
The data will be in MYDATA/connections/followers_and_following. The only files we care about are **following.json** and **followers_1.json**

1. Download "clean.py" from this github repository (should be listed at the top of this page)

    clean.py is a python script that puts the two lists into a format that can be compared with each other

2. Move **clean.py** to MYDATA/connections/followers_and_following

3. Open terminal in this folder (or python interpreter of your choice)

    - mac: right click inside the folder in Finder, click Services > New Terminal at folder. If that doesn't work try this: <a href="https://medium.com/@walecloud/add-open-in-terminal-option-for-finder-mac-os-d5ea2b0cde6a">Open Terminal app in this folder</a>

    - windows: right click inside the folder in Windows Explorer, click "Open in Terminal"

4. Type ```python clean.py following.json followers_1.json``` and hit enter (You can also copy and paste into bash)

5. Diff.json should now contain all users that you follow but don't follow you back.


# Notes
### What can break this process
Instagram consistently changes their data formats and data export steps, which might mean this script needs to be updated.

Also, some extra usernames may appear in the list due to people changing their usernames or deleting their accounts.

### Constraints for usability
This process is not the most technically elegant, as it's meant to be as un-daunting as possible for non-technical users. :p

I avoided requiring installing any packages/requiring any env management so this could be used with out-of-the-box python.



