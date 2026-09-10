# record.py

class Record:

    def __init__(self):
        self.history = []


    def add_history(self, round_num, name):

        record = {
            "round": round_num,
            "name": name
        }

        self.history.append(record)


    def show_history(self):

        print()
        print("==== 탈락 기록 ====")

        if len(self.history) == 0:
            print("기록이 없습니다.")

        else:
            for record in self.history:
                print(
                    f"{record['round']}회차 탈락자: {record['name']}"
                )