#This file is AI-generated, because I don't know how to use OpenCV
import cv2
import os

images = sorted(os.listdir("altered-frames"))
frame = cv2.imread(os.path.join("altered-frames", images[0]))
height, width, _ = frame.shape

video = cv2.VideoWriter("altered-output.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30, (width, height))

for img in images:
    frame = cv2.imread(os.path.join("altered-frames", img))
    video.write(frame)

video.release()
