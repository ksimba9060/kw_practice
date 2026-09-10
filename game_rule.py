class GameRule:
    def start_game(self, players):
        raise NotImplementedError

    def is_finished(self, game):
        raise NotImplementedError

    def get_current_player(self, game):
        raise NotImplementedError

    def process_turn(self, game, numbers):
        raise NotImplementedError
