from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os

imageDir = "images"
imagePaths = [os.path.join(imageDir, filename) for filename in os.listdir(imageDir)]

print("[INFO] quantifying faces...")
data = []

width = 1200
height = 1200
dim = (width, height)

batch_size = 8

for i in range(0, len(imagePaths), batch_size):
    batch_paths = imagePaths[i:i + batch_size]
    batch_images = []

    for (j, imagePath) in enumerate(batch_paths):
        print("[INFO] processing image {}/{}".format(i + j + 1, len(imagePaths)))
        print(imagePath)
        image = cv2.imread(imagePath)
        # resize the image
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
        batch_images.append(rgb)

    batch_boxes = face_recognition.batch_face_locations(batch_images, number_of_times_to_upsample=0)

    for image, boxes, path in zip(batch_images, batch_boxes, batch_paths):
        encodings = face_recognition.face_encodings(image, boxes)
        d = [{"imagePath": path, "loc": box, "encoding": enc} for (box, enc) in zip(boxes, encodings)]
        data.extend(d)


f = open("encodings.pickle", "wb")
f.write(pickle.dumps(data))
f.close()
