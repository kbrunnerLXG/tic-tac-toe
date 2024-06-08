class User:
    def __init__(self, number):
        self.player_mark_type = None
        self.player_number = number
        self.player_mark_pos = None
        self.player_1_mark = 'X'
        self.player_2_mark = '0'
        self.player_init()

    def player_init(self):
        if self.player_number == 1:
            self.player_mark_type = self.player_1_mark
        elif self.player_number == 2:
            self.player_mark_type = self.player_2_mark

    def select_pos(self):
        self.player_mark_pos = str(input(f'Please specify Row,Column for {self.player_mark_type}: ')).split(',')
        return self.player_mark_pos
