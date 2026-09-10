from game_record import GameRecord
from game_rule import GameRule
from nickname_input import NicknameInput
from number_input import NumberInput
from participant_count import ParticipantCount


class main:
    def __init__(self):
        self.participant_count = ParticipantCount()
        self.nickname_input = NicknameInput()
        self.number_input = NumberInput()
        self.game_rule = GameRule()
        self.game_record = GameRecord()

    def main(self):
        count = self.participant_count.get_count()
        players = self.nickname_input.get_nicknames(count)
        game = self.game_rule.start_game(players)

        while not self.game_rule.is_finished(game):
            current_player = self.game_rule.get_current_player(game)
            numbers = self.number_input.get_numbers(current_player)
            self.game_rule.process_turn(game, numbers)

        self.game_record.print_result(game)



game = main()
game.main()