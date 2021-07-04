import cv2
import os
import pygame

# Create an object to read from camera
video = cv2.VideoCapture(0)

# To set the directory to save images and recording

targetDir = 'C:\AniTemp\Photos'
os.chdir(targetDir)

# To check if camera is opened previously or not
if (video.isOpened() == False):
    print("Error reading video file")

# To set resolutions convert them from float to integer.

frame_width = int(video.get(3))
frame_height = int(video.get(4))

size = (frame_width, frame_height)
img_counter = 0
# Below VideoWriter object will create
# a frame of above defined The output
# is stored in 'filename.avi' file.

result = cv2.VideoWriter('filename.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size)
while (True):
    ret, frame = video.read()

    if ret == True:

        k = cv2.waitKey(1)
        # Write the frame into the
        # file 'filename.avi'
        result.write(frame)

        # Display the frame
        # saved in the file
        cv2.imshow('Frame', frame)

        if k % 256 == 27:  # Press Esc
            print("Escape hit, closing the app")
            break
        elif k % 256 == 32:  # Press space
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(os.path.join(targetDir, img_name), frame)
            print("screenshot taken")
            img_counter = img_counter + 1

    # Break the loop
    else:
        break

# When everything done, release
# the video capture and video
# write objects
video.release()
result.release()

# Closes all the frames
cv2.destroyAllWindows()

print("The video was successfully saved")
