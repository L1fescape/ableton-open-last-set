import os
import re
import argparse
import logging
import getpass
import string
# from sys import platform

live_folder_prefix = 'Live '
live_folder_regex = "{prefix}(\d*)\.*(\d*)\.*(\d*)".format(
    prefix=live_folder_prefix)


def parse_live_version_from_folder_name(version):
    major, minor, patch = re.search(live_folder_regex, version).groups()
    return int(major or 0), int(minor or 0), int(patch or 0)


def get_live_version_folder(root_pref_folder, live_version=''):
    live_folders = [name for name in os.listdir(root_pref_folder) if os.path.isdir(
        os.path.join(root_pref_folder, name)) and live_folder_prefix in name]
    if not live_folders:
        logging.exception('There are no Ableton Live preferences folders in "{folder}"\
             that match format "{format}"'.format(folder=root_pref_folder, format=live_folder_regex))
        return
    # if a live version was specified via command args look for it's corresponding folder
    if live_version:
        live_folder = '{prefix}{version}'.format(
            prefix=live_folder_prefix, version=live_version)
        if live_folder not in live_folders:
            logging.exception('Ableton Live preferences folder for version "{version}" was not found'.format(
                version=live_version))
            return
        return live_folders[live_folders.index(live_folder)]
    # otherwise use the latest version
    return max(live_folders, key=parse_live_version_from_folder_name)


def get_live_preferences_filepath(live_version=''):
    user = getpass.getuser()
    root_pref_folder = '/Users/{user}/Library/Preferences/Ableton`'.format(
        user=user)
    # if platform == 'win32':
    #     root_pref_folder = 'C:\\Users\\{user}\\AppData\\Roaming\\Ableton\\'.format(user=user)
    if not os.path.isdir(root_pref_folder):
        logging.exception('Root directory "{folder}" does not exist'.format(
            folder=root_pref_folder))
        return
    live_folder = get_live_version_folder(root_pref_folder, live_version)
    if not live_folder:
        return
    pref_filename = 'Preferences.cfg'
    # if platform == 'win32':
    #     pref_filename = '\\Preferences\\Preferences.cfg'
    return os.path.join(root_pref_folder, live_folder, pref_filename)


def get_recent_set(live_version=''):
    recent_set = None
    prefs_filepath = get_live_preferences_filepath(live_version)
    if not prefs_filepath:
        return
    if not os.path.exists(prefs_filepath):
        logging.exception('Attempted to use preferences file "{filepath}" but the file does not exist'.format(
            filepath=prefs_filepath))
        return
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
            # remove random chars infront of each path
            recent_set = chunk[chunk.find('/'):]
            break
    if not recent_set:
        logging.exception('Recent set could not be found in preferences file "{filepath}"'.format(
            filepath=prefs_filepath))
        return
    return recent_set


def main():
    parser = argparse.ArgumentParser(
        description='Display the filepath of the most recent Ableton Live set by parsing Ableton\'s Preferences.cfg.')
    parser.add_argument("-v", "--live_version",
                        help="Preferred Live version to use (defaults to the latest version if omitted)", required=False, default="")
    argument = parser.parse_args()

    recent_set = get_recent_set(argument.live_version)
    if recent_set:
        print(recent_set)


if __name__ == "__main__":
    main()
