class ExerciseTime:
    """목표 운동 시각을 등록한다."""

    def __init__(self):
        self.target_time = ""

    def register_time(self) :
        print()
        print("===== 목표 운동 시각 등록 =====")

        while True:
            target_time = input("목표 운동 시각을 입력하세요 (예: 19:30) : ").strip()

            if self._is_valid_time(target_time):
                self.target_time = target_time
                break

            print("시각은 00:00부터 23:59 사이로 입력해 주세요.")

        print("목표 운동 시각 :", self.target_time)
        return self.target_time

    def _is_valid_time(self, target_time: str) :
        try:
            hour, minute = target_time.split(":")
            hour = int(hour)
            minute = int(minute)
            return 0 <= hour <= 23 and 0 <= minute <= 59
        except ValueError:
            return False
