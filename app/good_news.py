class GoodNews:
    """오늘의 호재 내용을 보여준다."""

    def __init__(self, point_manager):
        self.point_manager = point_manager

    def show_news(self):
        while True:
            print()
            print("===== 오늘의 호재 =====")
            print("1. 목표 시간 출석      +5P")
            print("2. 운동 60분 달성      +8P")
            print("3. 프로틴 챙기기       +3P")
            print("4. 체성분 공시         +10P")
            print("5. 이전 메뉴")

            choice = input("호재를 선택하세요 : ").strip()

            if choice == "5":
                return
            elif choice == "1":
                print("선택한 호재가 확인되었습니다.\n")
                self.point_manager.add_points(5)
            elif choice == "2":
                print("선택한 호재가 확인되었습니다.\n")
                self.point_manager.add_points(8)
            elif choice == "3":
                print("선택한 호재가 확인되었습니다.\n")
                self.point_manager.add_points(3)
            elif choice == "4":
                print("선택한 호재가 확인되었습니다.\n")
                self.point_manager.add_points(10)
            else:
                print("1부터 5까지 입력해 주세요.\n")
