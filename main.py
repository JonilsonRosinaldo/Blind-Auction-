from random import choice, randint
from art import logo, title, end, figures, new_items
import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def possession(possession_dict, codes_dict, players_name):
    '''Fetches and displays the possessions of a player.'''
    pin = int(input(f"Please, {players_name}, insert your PIN.  "))
    if pin == codes_dict[players_name]:
        possessions = players_name #+ "1# "
        return f"Your possessions are {possession_dict[possessions]}"
    else:
        print("your PIN is invalid.")
        pin = int(input(f"Please, {players_name}, insert your PIN again.  "))
        if pin == codes_dict[players_name]:
            possessions = players_name #+ "'s_list"
            return f"Your possessions are {possession_dict[possessions]}"
        else:
            return 'Sorry, your PIN is invalid. You can not access your data.'


def balance(dictionary, codes):
    '''Checks the balance on the players account.'''
    nami = input("\nWhat's your name again? Just to confirm... 🧐  ").capitalize()
    if nami not in names:
        print("You've entered and invalid name. Try once more... 🤨 ")
        nami = input("\nWhat's your name?  ").capitalize()
    if nami in names:
        code = int(input("What's your code? Just to make sure 🤨...  "))
        if codes[nami] == code:
            current_balance = (f"{nami}, your current balance is: {dictionary[nami]}€ "
                               f"\nI was just ascertaining it was you, {nami} 😁")
            return current_balance
        else:
            print("\nYour pin is invalid. Please try once more 😠")
            code = int(input("What's your code?😠  "))
            if codes[nami] == code:
                current_balance = (f"{nami}, your current balance is: {dictionary[nami]}€"
                                   f"\nI was just ascertaining it was you, {nami} 😇")
                return current_balance
            else:
                return 'Your pin is invalid.😤'
    else:
        return "There is something wrong with name you've typed. 😤"


def owners(list, dict):
    '''Creates a and returns a dictionary that stores the name of the owner of each item and the respective items.'''
    # owners = {}
    for name in list:
        list_name = name #+ "'s_list"
        dict[list_name] = []
    return dict


def ordinal_str(number):
    '''Converts a cardinal number into an ordinal 'numerical' string (a number as a string).'''
    num_char_list = list(str(number))
    number_as_str = str(number)
    number_list = [int(i) for i in num_char_list]
    if number_list[-1] == 1:
        number_as_str += "st"
    elif number_list[-1] == 2:
        number_as_str += "nd"
    elif number_list[-1] == 3:
        number_as_str += "rd"
    else:
        number_as_str += "th"
    return number_as_str


def final_result(dict, list):
    '''blends the names in names with the respective values in other dictionary and returns
    a new dictionary with the new data'''
    winners = {}
    for name in list:
        if name in dict: # + "'s_list" in dict:
            winners[name] = dict[name] #+ "'s_list"]
    return winners


# When there is a draw in terms of number of items in possession, this might lead
# to a bug of repeating the same name for the same value
# This can be easily resolved if I create an if statement verifying if the name's already in the new_dict
def transform(dict, num_list_items):
    '''From a new ordered list of number of possessions this re-associates (pairs)
     the names with their proper values and returns a new_dict in crescent order so
     that it be possible to print the position of the players.'''  # I might search for a better alternative. 
    new_dict = {}
    for num in num_list_items:
        for nama in dict:
            if nama not in new_dict:
                if num == dict[nama]:
                    new_dict[nama] = num
    return new_dict


def item_choice(stuff, dict):
    if stuff == "Apple Product of choice 🖥":
        print(dict["apple"])
    elif stuff == "Dream Car 🚗":
        print(dict["car"])
    elif stuff == "iPhone 15 Pro Max 📱":
        print(dict["iphone"])
    elif stuff == "Free Meal at Restaurant of Choice 🍱":
        print(dict["croissant"])
    elif stuff == "Blank Check 💳":
        print(dict["money"])
    else:
        print(dict["present"])


print(logo)

items = ["Blank Check 💳", "3 items of 3 Luxury Brand of other player's choice💰", "Apple Product of choice 🖥",
         "Free Shop at store of choice 🛍", "Dream Car 🚗", "Louis Vuitton Bath Robe 🥋", "Chanel Sleeping Robe 👘",
         "King Sized Bed 🛏", "iPhone 15 Pro Max 📱", "Trip Tickets to Maldives 🏖", "MacBook Pro M3 Ultra 💻",
         "Christian Dior Perfume 🌷", "Gucci Bag 🧳", "Robot Vacuum Pro 🧹", "Blank Check 💳", "Blank Check 💳",
         "Free Meal at Restaurant of Choice 🍱", "2 weeks at Hotel 🏨 ⭐️⭐⭐⭐⭐ "]
names = []

players_codes = {}
# possession = []
ownerships = {}

contestants_bid = {}
players_money = {}
n_players = int(input("How many players are going to play this game?  "))
play_on = n_players * 2
for player in range(n_players):
    name = input(f"What's the name of the {ordinal_str(player + 1)} player?  ").capitalize()
    names.append(name)
    players_money[f"{name}"] = (randint(130, 151) * play_on * 5)
    print(f"\n{name}, your balance is: {players_money[name]}€\n")
    players_codes[name] = randint(100, 1000)
    input(f"Your PIN to access your balance is:  '{players_codes[name]}'"
          f"\nIf you forget this PIN you can NOT check your balance."
          f"\nDo you understand this?  ")
    clear_console()
ownership = owners(names, ownerships)


rounds = 0
while play_on > 0:
    rounds += 1
    if round(rounds) == round(play_on / 2):
        print(new_items["half way"])
        print("You are Half way of the game!")
        for nima in names:
            see_code = input(f"{nima}, do you need to know your code to check your money?  ").lower()
            if see_code == "yes":
                input("Are all the players looking away from the screen?  ")
                print(f"{nima}, your code is {players_codes[nima]} ")
                see_balance = input(f"{nima}, to check your balance type 'yes'.  ").lower()
                if see_balance == "yes":
                    balancing = print(balance(players_money, players_codes))
                input("Can we go on?  ")
            clear_console()

    print(f"This is the {ordinal_str(rounds)} round!\n")
    item = choice(items)
    items.remove(item)

    for key in players_money:
        show = item_choice(item, new_items)
        print(f"\nThe next gift is: {item}\n")

        input("Are you ready?  ")
        clear_console()
        balance_check = input(f"{key}, to check your balance type 'yes'. To bid type 'no'.  ").lower()
        if balance_check == 'yes':
            balancing = print(balance(players_money, players_codes))
        bid = int(input(f"{key}, how much are you wiling to pay for the {item}?\n"))
        end = input("Are you done?  ").lower()
        contestants_bid[key] = bid
        if end == "yes":
            clear_console()
        if end == "no":
            someone_else = False
            clear_console()

    person = ""
    winner = 0
    for key in contestants_bid:
        if contestants_bid[key] > winner:
            winner = contestants_bid[key]
            person = key
    if players_money[person] >= winner:
        if item == "Blank Check 💳":
            players_money[person] = round(players_money[person] * 1.3)
            players_money[person] -= winner
        else:
            players_money[person] -= winner

        ownership[person].append(item) # + "'s_list"
        print(new_items["smile"])
        print(f"\nThe winner of the {item} is {person}.")
        play_on -= 1
    else:
        print(f"\n{person} has not enough money on virtual account to afford the {item}.")
        see_code = input(f"{person}, do you need to know your code to check your money?  ").lower()
        if see_code == "yes":
            input("Are all the players looking away from the screen?  ")
            print(f"{person}, your code is {players_codes[person]} ")
            see_balance = input(f"{person}, to check your balance type 'yes'.  ").lower()
            if see_balance == "yes":
                balancing = print(balance(players_money, players_codes))
            input("Can we go on?  ")
        clear_console()
        print(new_items["shrug"])
        print(f"\nThere is no winner in this round.")
        play_on -= 1



    quest = int(input(f"\nGuys, how many of you want to know what items are in your possession? Type how many of you.  "))
    if quest > 0:
        for i in range(quest):
            name = input(f"\nWhat's the name of the {ordinal_str(i + 1)} person  ").capitalize()
            if name in names:
                possessions = possession(ownership, players_codes, name)
                print(possessions)
                input("Are you finished?  ")
                clear_console()
            else:
                print("You've entered an invalid name. So you will not be able to check your possessions.")
    if play_on > 0:
        ready = input(f"{title}\n\nAre you ready for the next round?  ")
        clear_console()
    else:
        players_and_possessions = final_result(ownership, names)
        win = {}
        for key in players_and_possessions:
            win[key] = len(players_and_possessions[key])
        list_of_players = [key for key, value in win.items()]
        num_of_possessions = [value for key, value in win.items()]
        num_of_possessions.sort() # this automatically sorts it out for me with no need to create a further variable
        ordered_dict = transform(win, num_of_possessions).items()
        winner_items = 0
        player = ""
        draw = 0
        drawer = ""
        objects = []
        drawer_objects = []
        for key, value in ownership.items():
            if len(value) > winner_items:
                winner_items = len(value)
                player = key
                objects = value
            elif len(value) == winner_items:
                draw = len(value)
                drawer = key
                drawer_objects = value
        if winner == draw:
            n = n_players
            position = ordinal_str(n)
            for name, number in ordered_dict:
                n -= 1
                print(f"{name} ended in {position} place with {number} item/s: {ownership[name]}")
                input("Can we proceed? ")
            print(figures[0])
            print("It's a draw! 🙃")

        elif winner > draw:
            n = n_players
            for name, number in ordered_dict:
                n -= 1
                position = ordinal_str(n)
                print(f"{name} ended in {position} place with {number} item/s: {ownership[name]}")
                input("Can we proceed? ")

# use the ordered_dict to print podium.
        print(new_items["good"])
        print("The game has ended. Hope you've really enjoyed. Please have fun!"
              "MERRY CHRISTMAS!!!")
        print(end)
        #check the lenght of the individual lists and use if statments to define the winner in each possible case.
        # Create a trophy and maybe a podium. starting from the last place.

