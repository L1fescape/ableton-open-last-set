import re
import os
from sys import platform
import getpass
import string

def parse_live_version(version):
    major, minor, patch = re.search("Live (\d*)\.*(\d*)\.*(\d*)", version).groups()
    return int(major or 0), int(minor or 0), int(patch or 0)

def get_ableton_preferences_filepath():
    user = getpass.getuser()
    root_pref_folder = '/Users/{user}/Library/Preferences/Ableton/'.format(user=user)
    if platform == 'win32':
        root_pref_folder = 'C:\\Users\\{user}\\AppData\\Roaming\\Ableton\\'.format(user=user)
    if not os.path.isdir(root_pref_folder):
        return

    live_folders = [name for name in os.listdir(root_pref_folder) if os.path.isdir(os.path.join(root_pref_folder, name)) and 'Live ' in name]
    if not live_folders:
        return
    live_version = max(live_folders, key=parse_live_version) # pick the most recent version

    pref_filename = '/Preferences.cfg'
    if platform == 'win32':
        pref_filename = '\\Preferences\\Preferences.cfg'

    return '{root_pref_folder}{live_version}{pref_filename}'.format(
        root_pref_folder=root_pref_folder,
        live_version=live_version,
        pref_filename=pref_filename
    )

prefs_filepath = get_ableton_preferences_filepath()
if not prefs_filepath:
    exit()

recent_set = None

# Preferences.cfg is a binary file and this is the horrible way it's being parsed at the moment.
# It looks like this file has some sort of xml structure. It would be great to be able to parse
# that and reference keys to get the most recent file instead of the method below
with open(prefs_filepath, mode='rb') as file:
    prefs_content = file.read().decode('latin1')

# attempt to filter out a lot of the garbage we get back after reading the file in as binary.
# filtering on `string.printable` is a temporary solution and will cause problems for set names
# that have unicode or emoji in them
filtered_prefs_content = ''
for c in prefs_content:
    if c in set(string.printable):
        filtered_prefs_content += c

# split on 'FileRef' and then look for the first item containing '.als'
for chunk in filtered_prefs_content.split('FileRef'):
    if chunk.find('.als') > -1:
        recent_set = chunk[chunk.find('/'):] # remove random chars infront of each path
        break

if recent_set:
    print(recent_set)