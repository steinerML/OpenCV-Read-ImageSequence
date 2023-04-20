import cv2 

# Create a video capture object, in this case we are reading from image sequence
# Note the name of the files. 
# For Cars0000.jpg  >> Cars%04d.jpg
# For Cars000.jpg  >> Cars%03d.jpg
# For Cars_00.jpg  >> Cars_%02d.jpg

#videocapture object for an image sequence
vid_capture = cv2.VideoCapture('Image_sequence/Cars%04d.jpg')


if (vid_capture.isOpened() == False):
	print("Error processing image sequence")

else:
  # Get frame rate information
  fps = int(vid_capture.get(cv2.CAP_PROP_FPS)) #or cv2.CAP_PROP_FPS instead of 5
  print("Frame Rate : ",fps,"frames per second")  
 
  # Get frame count
  frame_count = vid_capture.get(7) #or cv2.CAP_PROP_FRAME_COUNT instead of 5
  print("Frame count : ", frame_count)

while(vid_capture.isOpened()):
  # vCapture.read() methods returns a tuple, first element is a bool 
  # and the second is frame
 
  ret, frame = vid_capture.read()
  
  if ret == True:
    cv2.imshow('Autobahn webcam',frame)
    k = cv2.waitKey(20)
    #If you press q stop
    if k == ord('q'):
      break
  else:
     break

# Release the objects
vid_capture.release()
cv2.destroyAllWindows()