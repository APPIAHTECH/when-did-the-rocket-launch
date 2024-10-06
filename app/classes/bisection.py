class BisectionAlgorithm:
    def __init__(self, framex_api):
        self.framex_api = framex_api
        self.video_meta = framex_api.video()
        self.left = 0
        self.right = self.video_meta['frames'] - 1
        self.result_frame = None

    def get_next_frame(self):
        """
        Get the next frame to test in the bisection algorithm.
        """
        if self.left + 1 < self.right:
            mid = (self.left + self.right) // 2
            frame_data = self.framex_api.video_frame(mid)
            return mid, frame_data
        else:
            self.result_frame = self.right
            return None, None

    def test_frame(self, is_rocket_launched):
        """
        Based on user's answer, adjust the bisection range and return the next frame.
        """
        if is_rocket_launched:
            self.right = (self.left + self.right) // 2
        else:
            self.left = (self.left + self.right) // 2

        return self.get_next_frame()
