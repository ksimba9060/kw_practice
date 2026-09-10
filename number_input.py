class NumberInput:
    def get_numbers(self, current_player):
        while True:
            value = input(
                f"{current_player}님, 말할 숫자를 1~3개 입력하세요: "
            ).strip()
            number_text = value.split()

            if not 1 <= len(number_text) <= 3:
                print("숫자는 한 번에 1개에서 3개까지 입력할 수 있습니다.")
                continue

            try:
                numbers = [int(number) for number in number_text]
            except ValueError:
                print("숫자만 입력해 주세요.")
                continue

            return numbers
