class StockRegistration:
    """운동 주식으로 사용할 종목명과 닉네임을 등록한다."""

    def __init__(self):
        self.stock_name = ""

    def register_stock(self) -> str:
        print()
        print("===== 닉네임 등록 =====")

        while True:
            stock_name = input("닉네임(종목명)을 입력하세요 (최대 5자) : ").strip()

            if len(stock_name) == 0:
                print("닉네암을 입력해 주세요.")
            elif len(stock_name) > 5:
                print("닉네임은 최대 5자까지 입력할 수 있습니다.")
            else:
                self.stock_name = stock_name + " 개미"
                break

        print("등록 닉네임 :", self.stock_name)
        return self.stock_name
