import cv2
import numpy as np
import time
import sys

class VideoToTextPlayer:
    def __init__(self):
        self.frames = None
        self.palette = np.array(list("  .,:ilwW@@"))
        self.width, self.height= None, 50
    
    # processes singular frame
    def _process_frame(self, frame):
        if self.width is None:
            self.width = int(len(frame[0]) / len(frame) * self.height * 2)
        step1 = cv2.resize(frame, (self.width, self.height)).astype(int)
        step2 = self.palette[np.round(len(self.palette) * step1 / 255).astype(int) - 1]
        step3 = '\n'*3 + '\n'.join(''.join(row) for row in step2)
        return step3

    # processes and prints frames in real time
    def _play(self):
        next_frame = self._process_frame(self.frames[0])
        for frame in self.frames[0:]:
            start = time.perf_counter()

            current_frame = next_frame
            sys.stdout.write(current_frame)
            next_frame = self._process_frame(frame)

            end = time.perf_counter()
            time.sleep(max(0, 0.0333-(end-start)))
    
    # loads video to be played
    def _load(self, video_path):
        video = cv2.VideoCapture(video_path)
        frames = []
        while True:
            bool, frame = video.read()
            if not bool:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frames.append(frame)
        self.frames = np.array(frames)
    
    # terminal user interface
    def tui(self):
        while True:
            print("type 'help' for help with the commands!")
            inp = input(r">>> ")
            if inp == "help":
                print("""
=help=====================================
- load <path>: load video from path
- play: play loaded video
- size <height>: adjust height in char
- palette <palette>: change text 'palette'
- exit: exit player
==========================================
""")        
            elif inp[:5] == "load ":
                try:
                    video_path = inp[6:-1] if inp[5] == '"' and inp[-1] == '"' else inp[5:]
                    self._load(video_path)
                    print(f"\nloaded video {video_path}\n")
                except Exception as error:
                    print("\n" + str(error) + "\n")

            elif inp == "play":
                try:
                    self._play()
                    print("\n\n")
                except Exception as error:
                    print("\n" + str(error) + "\n")
            
            elif inp[:5] == "size ":
                try:
                    self.width, self.height = None, int(inp[5:])
                    print(f"\nchanged height to {self.height} characters\n")
                except Exception as error:
                    print("\n" + str(error) + "\n")
            
            elif inp[:8] == 'palette ':
                try:
                    self.palette = np.array(list(inp[8:]))
                    print(f"\nchanged palette to {inp[8:]}\n")
                except Exception as error:
                    print("\n" + str(error) + "\n")
                
            elif inp == "exit":
                break
            
            else:
                print("")

player = VideoToTextPlayer()
player.tui()