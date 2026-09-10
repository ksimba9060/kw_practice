class LoginManager:
    """아이디와 비밀번호를 확인하는 로그인 관리자."""

    def __init__(self, correct_id: str, correct_pw: str, max_attempts: int = 3):
        self.correct_id = correct_id
        self.correct_pw = correct_pw
        self.max_attempts = max_attempts

    def login(self) -> bool:
        for _ in range(self.max_attempts):
            print()
            print("===== 로그인 =====")

            user_id = input("ID : ").strip()
            user_pw = input("PASSWORD : ").strip()

            if user_id == self.correct_id and user_pw == self.correct_pw:
                print("로그인 되었습니다.")
                return True

            print("아이디 또는 비밀번호가 틀렸습니다.\n")

        print()
        print(f"로그인 {self.max_attempts}회 실패로 프로그램을 종료합니다.\n")
        return False
