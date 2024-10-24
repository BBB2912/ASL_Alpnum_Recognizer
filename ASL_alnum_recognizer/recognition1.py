import cv2
import numpy as np
import time
from tensorflow.keras.models import load_model
from cvzone.HandTrackingModule import HandDetector
import os
import pkg_resources  # Use pkg_resources to access package data
from wordPromoter import trie

class SignLanguageRecognizer:
    def __init__(self, model_path=None, detection_confidence=0.5, tracking_confidence=0.5):
        self.writingList = []  # List to store recognized letters
        self.detector = HandDetector(maxHands=1,
                                     detectionCon=detection_confidence,
                                     minTrackCon=tracking_confidence)
        self.input_prefix = None
        self.context = ''
        self.WP = trie
        self.sentence=None
        self.choosing=False
        self.suggestions=None
       
        if model_path is None:
            # Use pkg_resources to load the model from the package
            model_path = pkg_resources.resource_filename(
                __name__, 'models/signLanguageDetectoralpnum.h5')

        self.model = load_model(model_path)
        self.sentLen = 0
        # Mapping of model output to letters
        self.labels = {
            0: '1', 1: '10', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
            9: '9', 10: 'A', 11: 'B', 12: 'Nothing', 13: 'C', 14: 'D', 15: 'E', 16: 'F',
            17: 'G', 18: 'H', 19: 'I', 20: 'J', 21: 'K', 22: 'L', 23: 'M', 24: 'N',
            25: 'O', 26: 'P', 27: 'Q', 28: 'R', 29: 'S', 30: 'T', 31: 'U', 32: 'V',
            33: 'W', 34: 'X', 35: 'Y', 36: 'Z', 37: 'del', 39: ' '
        }

        self.last_prediction_time = 0  # Track time of last prediction
        self.delay = 3  # Delay in seconds between predictions

    def return_params(self):
        """Returns the current input prefix and context based on recognized letters."""
        if ' ' in self.writingList:
            text = ''.join(self.writingList)
            input_prefix = text.split()[-1]
            context = ' '.join(text.split()[:-1])
        else:
            input_prefix = ''.join(self.writingList)
            context = ''

        return input_prefix, context
    
    def get_suggestions(self, input_prefix, context):
        """Fetches word suggestions based on the current input prefix and context."""
        return [word for word, rank in self.WP.suggest(input_prefix, context)]

    def predict_from_image(self, image):
        """Predicts the ASL sign from a given image and updates the recognized letters."""
        label = self.labels.get(12, 'Nothing')  # Default to 'Nothing'

        # Find hand landmarks
        hands, img = self.detector.findHands(image)

        if hands:
            # Get the first detected hand
            hand = hands[0]

            # Extract the 21 landmarks of the hand
            landmarks = hand['lmList']  # List of 21 landmarks

            # Flatten the list of landmarks into a 1D array
            landmarks_flattened = np.array(landmarks).flatten()

            # Add batch dimension
            landmarks_input = np.expand_dims(landmarks_flattened, axis=0)

            # Predict using the model
            prediction = self.model.predict(landmarks_input, verbose=0)
            index = np.argmax(prediction)
            label = self.labels.get(index, 'Unknown')

        return label, img

    def return_result(self,label,img):
        # Only append to the list or handle 'del' if enough time has passed
            current_time = time.time()
            if current_time - self.last_prediction_time > self.delay:
                os.system('cls')
                if self.choosing == False or label=='del':
                    if label == 'del' and self.writingList:
                        # Remove the last letter if 'del' is detected
                        self.writingList.pop()
                    elif label=='Z':
                        self.choosing=True
                        print("choosing mode....!")
                        return
                    elif label != 'Nothing' and label != 'del' and label!='Z':
                        # Append the label to the writing list if it's not 'Nothing' or 'del'
                        self.writingList.append(label.lower())
                        
                else:
                    if label.isdigit():
                        word=self.suggestions[int(label)-1]
                        self.writingList=list(self.context)+list(' '+word)
                        self.choosing=False
                    else:
                        print('show numbers 1- 10')
                    
                # Update the last prediction time
                self.last_prediction_time = current_time

        # Join the writing list to form the string
                
                self.sentence = ''.join(self.writingList)
                self.input_prefix, self.context = self.return_params()
                
                self.suggestions = self.get_suggestions(self.input_prefix, self.context)
                print(f"Suggestions for '{self.input_prefix}' in context '{self.context}': {self.suggestions}")
                print(self.sentence)
    def run_webcam(self):
        """Runs the sign language recognizer using the webcam and displays the prediction in real-time."""
        # Initialize webcam
        cap = cv2.VideoCapture(0)

        # Initial delay before starting predictions (e.g., 3 seconds)
        initial_delay = 3  # 3-second initial delay
        time.sleep(initial_delay)

        # Start the real-time prediction loop after the initial delay
        while True:
            success, img = cap.read()

            if success:
                label, annotated_img = self.predict_from_image(img)

                if label:
                    self.return_result(label,annotated_img)
                # Display the webcam feed with prediction
                cv2.imshow('ASL Sign Language Detector', annotated_img)

            # Break loop with 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the capture and close OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

# If this script is run directly, start the webcam recognizer
if __name__ == "__main__":
    recognizer = SignLanguageRecognizer()
    recognizer.run_webcam()