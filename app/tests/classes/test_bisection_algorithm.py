class MockFrameXAPI:
    def __init__(self):
        self.frames = 100  # Default to 100 frames

    def video(self):
        """Mock method to return video metadata."""
        return {"frames": self.frames}

    def video_frame(self, frame_number):
        """Mock method to return fake frame data."""
        return b'fake_frame_data'

    def set_total_frames(self, frames):
        """Set the total number of frames for the video."""
        self.frames = frames


import unittest

from app.classes.bisection import BisectionAlgorithm


class TestBisectionAlgorithm(unittest.TestCase):

    def setUp(self):
        self.api = MockFrameXAPI()
        self.bisector = BisectionAlgorithm(self.api)

    def test_bisect(self):
        """Test the bisection logic."""
        self.api.set_total_frames(1000)  # Set total frames for the mock API
        next_frame, _ = self.bisector.get_next_frame()
        self.assertIsNotNone(next_frame)
        self.assertEqual(next_frame, 49)
