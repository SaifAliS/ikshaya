import face_recognition
import pickle
import time
import cv2

filepath="./image_3.jpg"
def faceRecog(filepath):
    currentname = "unknown"
    #Determine faces from encodings.pickle file model created from train_model.py
    encodingsP = "./encodings.pickle"

    # load the known faces and embeddings along with OpenCV's Haar
    # cascade for face detection
    data = pickle.loads(open(encodingsP, "rb").read())

    names=[]
    # loop over frames from the video file stream
        # Detect the fce boxes
    unknown_image = face_recognition.load_image_file(filepath)
    # compute the facial embeddings for each face bounding box
    encodings = face_recognition.face_encodings(unknown_image)
    names = []
    for encoding in encodings:
	# attempt to match each face in the input image to our known
	# encodings
        matches = face_recognition.compare_faces(data["encodings"],encoding)
        name = "Unknown" #if face is not recognized, then print Unknown

		# check to see if we have found a match
        if True in matches:
			# find the indexes of all matched faces then initialize a
			# dictionary to count the total number of times each face
			# was matched
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

			# loop over the matched indexes and maintain a count for
			# each recognized face face
            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1

			# determine the recognized face with the largest number
			# of votes (note: in the event of an unlikely tie Python
			# will select first entry in the dictionary)
            name = max(counts, key=counts.get)

			#If someone in your dataset is identified, print their name on the screen
            if currentname != name:
                currentname = name

		# update the list of names
    
        names.append(name)
    return names


def hello(event,context):
    try:
        if 1==1:
            return faceRecog(filepath)
        else:
            return "Something went wrong"
    except Exception as e:
        return str(e) 