import Face_Recognition.facerec as fr
import ALPR.mainProgram as alpr
import cv2
import pickle
import json


with open("checker.json") as f:
  dataJSON = json.load(f)

print(dataJSON)
print(type(dataJSON))

#Determine faces from encodings.pickle file model created from train_model.py
encodingsP = open("Face_Recognition/encodings.pickle","rb")
#use this xml file
#https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
cascade = "Face_Recognition/haarcascade_frontalface_default.xml"

# load the known faces and embeddings along with OpenCV's Haar
# cascade for face detection
print("[INFO] loading encodings + face detector...")
data = pickle.load(encodingsP, encoding='latin1')
detector = cv2.CascadeClassifier(cascade)

# load citra RGB (BGR)
frame = cv2.imread(r'image_0.jpg')

# deteksi plat dan wajah
plate_number, img_show_plate = alpr.plate_detector(frame)
img_show_plate = cv2.resize(img_show_plate, (500, 500), interpolation = cv2.INTER_AREA)

frame, boxes, names = fr.face_rec(frame, data, detector)

cocok = False
for i in dataJSON:
  if plate_number == i:
    for name in names:
      if name == dataJSON[plate_number]:
        cocok = True
        break

if cocok : print("Gerbang berhasil terbuka")
else : print("Gerbang masih tertutup")

for ((top, right, bottom, left), name) in zip(boxes, names):
  # draw the predicted face name on the image - color is in BGR
  cv2.rectangle(frame, (left, top), (right, bottom),
                (0, 255, 0), 2)
  y = top - 15 if top - 15 > 15 else top + 15
  cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
              .8, (255, 0, 0), 2)

while True:
  # display the image to our screen
  cv2.imshow("Plat: "+plate_number, img_show_plate)
  cv2.imshow(str(names), frame)
  key = cv2.waitKey(1) & 0xFF

  # quit when 'q' key is pressed
  if key == ord("q"):
    # do a bit of cleanup
    cv2.destroyAllWindows()
    break