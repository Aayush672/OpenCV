import cv2 as cv

img = cv.imread('Desktop/Skill Path.png')
cv.imshow('Skill Path', img)

capture = cv.VideoCapture('Desktop/Video.mp4')

while True :
    isTrue , frame = capture.read() 
#  Returns boolean that whether the video was successfully read & Reads the video frame by frame
    cv.imshow('Video', frame)
    # Display each frame
    if cv.waitKey(20) & 0xFF==ord('d'):
        #if letter 'd' is pressed
        break 
capture.release()
cv.destroyAllWindows()