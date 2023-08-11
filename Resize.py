import cv2 as cv

# img = cv.imread('Desktop/Skill Path.png')
# cv.imshow('Skill',img)
def rescaleFrame(frame , scale = 0.8):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interplotation = cv.INTER_AREA)

capture = cv.VideoCapture('Desktop/Recording.mov')

while True :
    isTrue , frame = capture.read() 
#  Returns boolean that whether the video was successfully read & Reads the video frame by frame
    cv.imshow('Video', frame)
    # Display each frame
    if cv.waitKey(20) & 0xFF==ord('d'):
        #if letter 'd' is pressed
        break 
capture.release()
cv.destroyAllWimdows()
