class NicknameInput:
    def __init__(self):
        self.users = []

    def get_nicknames(self, participant_count):
        for i in range(int(participant_count)):
            user = input(f"{i+1}번째 참가자: ")
            self.users.append(user)

participant_count = 1
abc = NicknameInput()
abc.get_nicknames.run(participant_count)






