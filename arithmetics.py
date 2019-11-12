import cv2

imag = cv2.imread('samples/messi.jpeg')
print(imag.size) # returns Total number of pixels accessed.
print(imag.shape)# returns tuple of (rows, columns, channels).
print(imag.dtype)# returns image datatype.

b, g, r = cv2.split(imag) # split the images into 3 channels(black, green, red)

print(b, g, r)

cv2.imshow('frame', b)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# to merge all the channels, use .merge() method. 
imag = cv2.merge((b, g, r))
cv2.imshow('original', imag)
cv2.waitKey(2000)
cv2.destroyAllWindows()

'''
Now, you can also add images on each other using .add() method.
But to work with it, your images must be of same size.
Use .resize() method on both images.
(You can also add .png files.)
'''

imag1 = cv2.imread('samples/ld2.jpeg')
img1 = cv2.resize(imag, (512, 512))
img2 = cv2.resize(imag1, (512, 512))

res = cv2.add(img1, img2)
cv2.imshow('added', res)
cv2.waitKey(4000)
cv2.destroyAllWindows()

'''
to give weightage to one image wrt other, use .


'''
res = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
cv2.imshow('addweight', res)
cv2.waitKey(5000)
cv2.destroyAllWindows()
