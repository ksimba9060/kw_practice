from thirty_one import TJ
from user_name_input import user_name
from number_input import NumberInput
from 참여자수 import User


class main:
    def __init__(self):
        self.participant_count = User()
        self.nickname_input = user_name()
        self.number_input = NumberInput()
        self.game_rule = TJ()

    def main(self):
        count = self.participant_count.user_count()
        players = self.nickname_input.user_name_input(count)
        player_index = 0

        while True:
            current_player = players[player_index]
            numbers = self.number_input.get_numbers(current_player)

            if self.game_rule.is_31(numbers):
                break

            player_index = (player_index + 1) % len(players)


if __name__ == "__main__":
    game = main()
    game.main()
