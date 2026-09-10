class PointManager:
    """운동 호재 포인트를 관리한다."""

    def __init__(self):
        self.points = 0

    def add_points(self, point):
        self.points += point
        print("포인트", point, "P가 쌓였습니다.\n")
        print("현재 누적 포인트 :", self.points, "P")

    def show_points(self):
        print("현재 누적 포인트 :", self.points, "P")
