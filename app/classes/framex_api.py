import os
from urllib.parse import quote, urljoin

from httpx import Client

API_BASE = os.getenv("API_BASE", "https://framex-develop-amzw3.ondigitalocean.app/api/")
VIDEO_NAME = os.getenv(
    "VIDEO_NAME", "Falcon Heavy Test Flight (Hosted Webcast)-wbSwFU6tY1c"
)


class FrameXAPI:
    def __init__(self):
        self.client = Client(timeout=30)

    def video(self):
        """
        Fetch video metadata.
        """
        r = self.client.get(urljoin(API_BASE, f"video/{quote(VIDEO_NAME)}/"))
        r.raise_for_status()
        return r.json()

    def video_frame(self, frame_num: int) -> bytes:
        """
        Fetch the image of a specific frame as bytes.
        """
        r = self.client.get(urljoin(API_BASE, f"video/{quote(VIDEO_NAME)}/frame/{frame_num}/"))
        r.raise_for_status()
        return r.content
