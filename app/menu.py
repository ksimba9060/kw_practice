from app.good_news import GoodNews


class Menu:
    """개미득근 챌린지의 메뉴를 보여준다."""

    def __init__(self, point_manager):
        self.good_news = GoodNews(point_manager)

    def select_menu(self):
        while True:
            print()
            print("===== 메뉴 =====")
            print("1. 오늘의 호재")
            print("2. 내 운동 주가")
            print("3. 리워드")
            print("4. 피지컬 보기")
            print("5. 운동장 마감")

            choice = input("메뉴를 선택하세요 : ").strip()

            if choice == "1":
                self.good_news.show_news()
            elif choice in ["2", "3", "4"]:
                print("아직 개발되지 않은 메뉴입니다.")
            elif choice == "5":
                print("운동장을 마감합니다.")
                break
            else:
                print("1부터 5까지 입력해 주세요.")
