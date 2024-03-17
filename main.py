import cv2 as cv
import os
from time import time
from src.video.holdcapture import WindowCapture as h_Cap
from src.video.boardcapture import WindowCapture as b_Cap
from src.video.nextcapture import WindowCapture as n_Cap

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# WindowCapture.list_window_names()
# exit()

# initialize the WindowCapture class
holdcap = h_Cap()
boardcap = b_Cap()
nextcap = n_Cap()

loop_time = time()
while(True):

    # get an updated image of the game
    hold = holdcap.get_screenshot()
    cv.imshow('Hold', hold)
    cv.moveWindow('Hold', 800, 200)

    board = boardcap.get_screenshot()   
    cv.imshow('Board', board)
    cv.moveWindow('Board', 930, 200)

    next = nextcap.get_screenshot()   
    cv.imshow('Next', next)
    cv.moveWindow('Next', 1120, 200)
    
    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
#print(1536/2, " ", 864/4)
