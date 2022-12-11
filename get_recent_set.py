import getpass
import string

user = getpass.getuser()
live_version = '11.2.6'
preferences_file = '/Users/{user}/Library/Preferences/Ableton/Live {live_version}/Preferences.cfg'.format(user=user, live_version=live_version)
recent_set = None

# Preferences.cfg is a binary file and this is the horrible way it's being parsed at the moment.
# It looks like this file has some sort of xml structure. It would be great to be able to parse
# that and reference keys to get the most recent file instead of the method below
with open(preferences_file, mode='rb') as file:
    prefs_content = file.read().decode('latin1')
# attempt to filter out a lot of the garbage we get back after reading the file in as binary.
# this will cause problems if set names have unicode chars or emoji in them
filtered_prefs_content = ''
for c in prefs_content:
    if c in set(string.printable):
        filtered_prefs_content += c
# split on 'FileRef' and then look for the first item containing '.als'
for chunk in filtered_prefs_content.split('FileRef'):
    if chunk.find('.als') > -1:
        recent_set = chunk[1:] # there's always one random character infront of each FileRef
        break

if recent_set:
    print(recent_set)