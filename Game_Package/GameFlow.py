from Game_Package.CardGame import CardGame
from Game_Package.Player import Player

def main():
    while True:
        name1 = input("player 1 name: ")
        name2 = input("player 2 name: ")
        try:
            game = CardGame(name1, name2, 26)
            break
        except TypeError:
            print("game parameter types invalid. try again.")
        except ValueError:
            print("game parameter values invalid. try again.")
    for i in range(10):
        card1 = game.player1.get_card()
        print(f"{game.player1} chose: {card1}")
        card2 = game.player2.get_card()
        print(f"{game.player2} chose: {card2}")
        if card1 > card2:
            print(f"{game.player1} won round {i + 1}")
            game.player1.add_card(card1)
            game.player1.add_card(card2)
        else:
            print(f"{game.player2} won round {i + 1}")
            game.player2.add_card(card1)
            game.player2.add_card(card2)
    winner = game.get_winner()
    if winner is None:
        print("Draw!")
    else:
        print(f"{winner} won!")


if __name__ == '__main__':
    main()