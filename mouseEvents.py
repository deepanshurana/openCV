import numpy as np
import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def showCoordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' ', y)
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        stringText = str(x) + ', ' + str(y)
        cv2.putText(img, stringText, (x, y), font, 1, (255, 0, 0), 2)
        cv2.imshow('clickevents', img)

img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('clickevents', img)

# to call the showCoordinates() function, use setMouseCallback() function.
cv2.setMouseCallback('clickevents', showCoordinates)

cv2.waitKey()
cv2.destroyAllWindows()
