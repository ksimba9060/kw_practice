class menu:
    def main_menu(self):
        print("==메뉴선택==")
        print("1.게임시작")
        print("2.랭킹보기")
        print("3.게임종료")  

    def game_start(self):
        while True:
            x = input(">")
            if x == "1":
                game.main()
                
            elif x == "2":
                abc = Record()
                abc.show_history()

            elif x == "3":
                break

            else:
                print("잘못된 숫자를 입력하셨습니다.")



game = menu()
game.main_menu()
game.game_start()