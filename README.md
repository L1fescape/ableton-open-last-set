# Launch Ableton with your most recent set loaded

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
- Launch your spiffy new app and load directely into whatever you were last working on!

## TODOs
- support windows
- select latest live version in `/Users/[username]/Library/Preferences/Ableton` folder instead of hardcoding
- remove python dependency
- handle case where getting the most recent set errors or returns null 
- have applescript wait until project is loaded before giving application focus (currently focuses right when ableton loads)

## Notes
- the main motivation was to remove an additional step when trying to hop back into a project with a fresh idea on my mind. I get distracted very easily, so the fewer steps there are between me and making music the more music will be made. Saving time was not an objective (and it doesn't save much time - see the next note).
- When calling `open my_set.als` Ableton will *still* open to a blank Untitled.als project before then opening your set
