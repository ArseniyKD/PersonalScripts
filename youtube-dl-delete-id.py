"""
Version 1.0

The youtube-dl-delete-id.py is a script that will delete the Youtube video IDs
from the file names. I personally use it with .mp3 files.

Example of output:
    "Video title-ID_hash_das89asc01a.mp3" -> "Video title.mp3"

Current Issues:
    - Cannot process dashes in video ID correctly.
    - Hardcoded offset for .mp3, probably would be better to make modular.
    - Only works if files and script are both in the same dir.
    - Will do the conversion for absolutely all files in the dir.
    - Does not ask for permission before renaming.
"""

# Import all the OS library requirements
from os import listdir
from os import rename
from os.path import isfile, join

# A list comprehension to get all the file names, ignoring directories 
files = [f for f in listdir("./") if isfile( join( "./", f))]

for f in files:
    # Ignore the script as it will be in the working directory as the script is
    # written currently.
    if f == "youtube-dl-delete-id.py": continue
    # Reverse the file name, find the last occurrence of a '-', delete all
    # characters between the last dash and the .mp3 including the dash. 
    tmp = f[::-1]
    tmp = tmp[:4] + tmp[tmp.find("-")+1:]
    # Rename the file to the version without the video ID.
    rename( f, tmp[::-1] )
print( "Done!" )
