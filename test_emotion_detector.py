import unittest
from emotion_detector import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    
    def test_positive_emotion(self):
        text = "I am so happy and thrilled!"
        result = emotion_detector(text)
        self.assertIn("joy", result["label"].lower())
        self.assertGreater(result["score"], 0.8)  # Assuming joy score should be high for happy text

    def test_negative_emotion(self):
        text = "I am very sad and disappointed."
        result = emotion_detector(text)
        self.assertIn("sadness", result["label"].lower())
        self.assertGreater(result["score"], 0.7)  # Assuming sadness score should be high for sad text

    def test_neutral_emotion(self):
        text = "This is a regular statement."
        result = emotion_detector(text)
        # Check if no emotion has a high score, assuming low emotion scores imply neutrality
        self.assertLess(result["score"], 0.5)  # Score threshold can be adjusted as per observed behavior

if __name__ == "__main__":
    unittest.main()
