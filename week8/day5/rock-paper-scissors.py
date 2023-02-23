from game import Game


def get_user_menu_choice():
    choice = ''
    while choice not in ['g', 'q']:
        choice = input(f"Menu:\n(g) Play a new game\n(q) Show scores and quit\n:")
    return choice


def print_results(results):
    print(
        f"game results: \n you won {results['win']} times, \n you lost {results['loss']} times, \n you drew {results['draw']} times \n Thank You for playing!")


def main():
    choice = get_user_menu_choice()
    results = {'win': 0, 'loss': 0, 'draw': 0}
    while choice != 'q':
        new_game = Game()
        result = new_game.play()
        results[result] += 1
        choice = get_user_menu_choice()
    else:
        print_results(results)


main()
