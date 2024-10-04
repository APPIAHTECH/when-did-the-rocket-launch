from typing import List, Dict, Optional, Any

from app.classes import FrameXAPI

if __name__ == "__main__":
    framex_api = FrameXAPI(api_domain="framex-develop-amzw3.ondigitalocean.app")
    video_list: Optional[List[Dict[str, Any]]] = framex_api.get_video_list()

    if video_list:
        for video in video_list:
            print(f"Video Name: {video['name']}, Frames: {video['frames']}, Frame Rate: {video['frame_rate']}")

    selected_video_name: str = "Falcon Heavy Test Flight (Hosted Webcast)-wbSwFU6tY1c"
    frame_number: int = 42
    frame_image: Optional[bytes] = framex_api.get_frame(selected_video_name, frame_number)
