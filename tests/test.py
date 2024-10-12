import cv2
import numpy as np
import unittest
from SignLangASL_Recognizer import SignLanguageRecognizer

class TestSignLanguageRecognizer(unittest.TestCase):
    def setUp(self):
        """Set up the recognizer for testing."""
        self.recognizer = SignLanguageRecognizer()

    def test_initialization(self):
        """Test if the recognizer initializes correctly."""
        self.assertIsInstance(self.recognizer, SignLanguageRecognizer)
        self.assertIsNotNone(self.recognizer.model)  # Check if model is loaded
        self.assertIsNotNone(self.recognizer.detector)  # Check if detector is initialized

    def test_labels(self):
        """Test if labels are correctly defined."""
        expected_labels = {i: str(i) for i in range(10)}
        expected_labels.update({i + 10: chr(65 + i) for i in range(26)})
        expected_labels[12] = 'Nothing'
        expected_labels[37] = 'del'
        expected_labels[39] = 'space'
        self.assertEqual(self.recognizer.labels, expected_labels)

    def test_predict_from_image(self):
        """Test the prediction function with a dummy image."""
        # Create a dummy black image
        dummy_image = np.zeros((640, 480, 3), dtype=np.uint8)

        label, annotated_image = self.recognizer.predict_from_image(dummy_image)

        # Check if a label is returned
        self.assertIsInstance(label, str)
        self.assertEqual(label, 'Nothing')  # Since it's a blank image

        # Check if the annotated image is returned and has the same shape
        self.assertIsInstance(annotated_image, np.ndarray)
        self.assertEqual(annotated_image.shape, dummy_image.shape)

    def test_run_webcam(self):
        """Test if the webcam function runs without errors."""
        try:
            self.recognizer.run_webcam()  # This will open a webcam window
        except Exception as e:
            self.fail(f"run_webcam raised Exception: {e}")

if __name__ == "__main__":
    unittest.main()
