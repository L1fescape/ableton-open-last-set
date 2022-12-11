# Ableton Open Last Set 
> Launch Ableton with your last set loaded

Parses Ableton's `Preferences.cfg` file to get the list of most recent sets (the same list you see in the `File -> Open Recent Set` dropdown). Then calls `open` on that file.

**Disclaimer**: This is functional but still very much a work in progress

## Dependencies
- python

## Demo

![ableton open recent demo](demo.gif)

## Setup

OSX:
- Copy `get_recent_set.py` somewhere on your computer
- Launch the `Script Editor` app and create a new script with the contents inside of `osx/Ableton Recent.app`, replace `/path/to/get_recent_set.py` with the location you used for the previous step, hit save and set the `File Format` dropdown to `Application`
- Launch your spiffy new app and load directely in o whatever you were last working on!

## TODOs
- support windows
- select latest live version in `/Users/[username]/Library/Preferences/Ableton` folder instead of hardcoding
- remove python dependency
- handle case where getting the most recent set errors or returns null 
- have applescript wait until project is loaded before giving application focus (currently focuses right when ableton loads)

## Notes
- the main motivation was to remove an additional step when trying to hop back into a project with a fresh idea on my mind. Saving time was not the motivation. I get discracted very easily and one additional step to open a project or seeing a bunch of my other projects in the dropdown list can easily cause me to forget an idea
