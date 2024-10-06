import unittest

from app.classes.framex_api import FrameXAPI


class TestFrameXAPI(unittest.TestCase):
    def test_video_frame(self):
        framex_api = FrameXAPI()
        frame_num = 100

        # Simulating a test for retrieving frame data
        result = framex_api.video_frame(frame_num)

        # Check if result is not empty (assuming the API should return bytes)
        self.assertIsInstance(result, bytes)  # Ensure the result is in bytes format
