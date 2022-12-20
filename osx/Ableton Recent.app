-- credit: https://stackoverflow.com/a/3469708
on FileExists(theFile)
	tell application "System Events"
		return exists file theFile
	end tell
end FileExists

on run
	set recentSet to do shell script "/usr/local/bin/python /path/to/get_recent_set.py 2>&1"
	if FileExists(recentSet) then
		do shell script "open \"" & recentSet & "\""
		tell application "Ableton Live 11 Suite" to activate
	else
		display dialog "Could not get a recent file:\n" & recentSet
	end if
end run