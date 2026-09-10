class PhysicalCheck:
    """사용자의 시드 피지컬 정보를 등록한다."""

    def __init__(self):
        self.nickname = ""
        self.weight = 0.0
        self.muscle = 0.0
        self.body_fat = 0.0

    def check_physical(self, nickname: str) -> None:
        self.nickname = nickname

        print()
        print("===== 시드 피지컬 등록 =====")
        print("등록 종목:", self.nickname)

        print()
        print("----- 현재 피지컬 -----")
        print("※ 아래 정보는 숫자만 입력해 주세요.")
        print("※ 모를 경우 인포데스크에 문의해 주세요.")
        print()

        self.weight = self._read_number("몸무게 (kg)     : ")
        self.muscle = self._read_number("골격근량 (kg)   : ")
        self.body_fat = self._read_number("체지방량 (kg)   : ")

        self._print_result()

    def _read_number(self, prompt: str) -> float:
        while True:
            try:
                value = float(input(prompt))
                if value <= 0:
                    print("0보다 큰 숫자를 입력해 주세요.")
                    continue
                return value
            except ValueError:
                print("숫자만 입력해 주세요.")

    def _print_result(self) -> None:
        print()
        print("===== 나의 시드 피지컬 =====")
        print("종목명   :", self.nickname)
        print("몸무게   :", self.weight, "kg")
        print("골격근량 :", self.muscle, "kg")
        print("체지방량 :", self.body_fat, "kg")
        print()
        print("시드 피지컬 등록이 완료되었습니다.")
