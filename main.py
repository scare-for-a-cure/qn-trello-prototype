from trello import TrelloApi
from secrets import TRELLO_API_KEY,TRELLO_BOARD_ID,TRELLO_SECRET,TRELLO_TOKEN



def main():
    # Installed in this environment:
    # Trello API
    # Various Google APIs for working with Google Docs.
    print(f'Hi, Chad')  # Press Ctrl+F8 to toggle the breakpoint.
    trello = TrelloApi(TRELLO_API_KEY)
    trello.set_token(TRELLO_TOKEN)
    trello.boards.get(TRELLO_BOARD_ID)
    print(trello)
    card = trello.cards.get("pyhDPxft")
    print(card)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
