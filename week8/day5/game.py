import random


class Game:
    def __init__(self):
        self.game_list=['r','s','p']
    def get_user_item(self):
        user_item=''
        while user_item not in ['r', 'p', 's']:
            user_item=input(f"Select (r)ock , (p)aper, or (s)cissors :")
        return user_item
    def get_computer_item(self):
        return random.choice(self.game_list)
    def get_game_result(self, user_item, computer_item):
        if user_item==computer_item:
            return 'draw'
        # if user_item=='r':
        #     if computer_item=='s':
        #         return 'win'
        #     return 'loss'
        # if user_item=='p':
        #     if computer_item=='r':
        #         return 'win'
        #     return 'loss'
        # if user_item=='s':
        #     if computer_item=='p':
        #         return 'win'
        #     return 'loss'

        if (user_item == 'r' and computer_item == 's') or (user_item== 'p' and computer_item == 'r') or (user_item == 's' and computer_item == 'p'):
            return 'win'
        return 'loss'
    def play(self):
        user_item=self.get_user_item()
        computer_item=self.get_computer_item()
        result=self.get_game_result(user_item,computer_item)
        print(f"you selected {user_item}, the computer selected {computer_item}, the result: {result}")
        return  result
