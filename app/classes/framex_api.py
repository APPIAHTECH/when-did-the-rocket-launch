from typing import List, Dict, Optional, Any

import requests


class FrameXAPI:
    """
    Example API response:
    [
        {
            "name": "Falcon Heavy Test Flight (Hosted Webcast)-wbSwFU6tY1c",
            "width": 1920,
            "height": 1080,
            "frames": 61696,
            "frame_rate": [
                30000,
                1001
            ],
            "url": "http://framex-develop-amzw3.ondigitalocean.app/api/video/Falcon%20Heavy%20Test%20Flight%20(Hosted%20Webcast)-wbSwFU6tY1c/",
            "first_frame": "http://framex-develop-amzw3.ondigitalocean.app/api/video/Falcon%20Heavy%20Test%20Flight%20(Hosted%20Webcast)-wbSwFU6tY1c/frame/0/",
            "last_frame": "http://framex-develop-amzw3.ondigitalocean.app/api/video/Falcon%20Heavy%20Test%20Flight%20(Hosted%20Webcast)-wbSwFU6tY1c/frame/61695/"
        }
    ]
    """

    def __init__(self, api_domain: str) -> None:
        """
        :param api_domain:
        """
        self.api_domain: str = api_domain
        self.base_url: str = f"https://{api_domain}/api/video/"

    def get_video_list(self) -> Optional[List[Dict[str, Any]]]:
        """
        Fetches the list of available videos and their metadata.
        :return:
        """
        response = requests.get(self.base_url)
        response.raise_for_status()
        return response.json()  # Returns a list of video metadata

    def get_frame_url(self, video_name: str, frame_number: int) -> str:
        """
        Constructs the URL to fetch a specific frame from a video.
        :param video_name:
        :param frame_number:
        :return:
        """
        return f"https://{self.api_domain}/api/video/{video_name}/frame/{frame_number}/"

    def get_frame(self, video_name: str, frame_number: int) -> Optional[bytes]:
        """
        Fetches a specific frame as a JPEG image.
        :param video_name:
        :param frame_number:
        :return:
        """
        frame_url = self.get_frame_url(video_name, frame_number)
        response = requests.get(frame_url)
        response.raise_for_status()
        return response.content  # Returns the image bytes
