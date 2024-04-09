This hobby project is a video player for the terminal where the pixels are converted to characters in real time.
You can manually change the size and character 'palette' for the video.

The project is written in python and uses numpy and opencv-python as libraries.

Here is a list of all the commands:

          load <path> : load video from specified path to be played.
                 play : play the currently loaded video.
        size <height> : adjust the video height in characters (the width is decided automatically).
    palette <palette> : change the character palette. eg. the default palette is "  .,:ilwW@@" (sparse -> dense).
                 exit : exit player.
                 help : list all the commands.
