import random
import sys

# Game variables
game_vars = {
    'day': 1,
    'energy': 10,
    'money': 20,
    'bag': {
        'Lettuce' : 0,
        'Potato' : 0,
        'Cauliflower' : 0,
    }
}

seed_list = ['LET', 'POT', 'CAU']

seeds = {
    'LET': {'name': 'Lettuce',
            'price': 2,
            'growth_time': 2,
            'crop_price': 3
            },

    'POT': {'name': 'Potato',
            'price': 3,
            'growth_time': 3,
            'crop_price': 6
            },

    'CAU': {'name': 'Cauliflower',
            'price': 5,
            'growth_time': 6,
            'crop_price': 14
            },
}

farm = [ [['','',''], ['','',''], ['','',''], ['','',''], ['','','']],
         [['','',''], ['','',''], ['','',''], ['','',''], ['','','']],
         [['','',''], ['','',''], ['HSE','X',''], ['','',''], ['','','']],
         [['','',''], ['','',''], ['','',''], ['','',''], ['','','']],
         [['','',''], ['','',''], ['','',''], ['','',''], ['','','']] ]

def display_main_menu():
    """
    Display the main menu for Sundrop Farm game.

    Displays a welcome message and menu options for starting a new game, loading a saved game,
    or exiting the game.

    Example:
    ----------------------------------------------------------
    Welcome to Sundrop Farm!

    You took out a loan to buy a small farm in Albatross Town.
    You have 30 days to pay off your debt of $100.
    You might even be able to make a little profit.
    How successful will you be?
    ----------------------------------------------------------
    1) Start a new game
    2) Load your saved game

    0) Exit Game
    """

    print("----------------------------------------------------------")
    print("Welcome to Sundrop Farm!")
    print()
    print("You took out a loan to buy a small farm in Albatross Town.")
    print("You have 20 days to pay off your debt of $100.")
    print("You might even be able to make a little profit.")
    print("How successful will you be?")
    print("----------------------------------------------------------")
    print("1) Start a new game\n"
          "2) Load your saved game\n"
          "\n"
          "0) Exit Game")
    
def in_town(game_vars):
    '''
    Displays the menu of Albatross Town and returns the player's choice
    Players can
        1) Visit the shop to buy seeds
        2) Visit the farm to plant seeds and harvest crops
        3) End the day, resetting Energy to 10 and allowing crops to grow

        9) Save the game to file
        0) Exit the game (without saving)

    Args:
        game_vars: A dictionary containing game variables('day','energy','money','bag')
    
    Returns:
        town_choice : Player's choice in Albatross Town
    '''
    while True: 
        show_stats(game_vars)
        print("You are in Albatross Town")
        print("-------------------------")
        print("1) Visit Shop\n"
            "2) Visit Farm\n"
            "3) End Day\n"
            "\n"
            "9) Save Game\n"
            "0) Exit Game")
        print("-------------------------")
        try:
            town_choice = input("Your choice? ")
            if int(town_choice) in [1,2,3,9,0]:
                return town_choice
            else:
                print("Invalid choice. Please enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter a valid number (0,1,2,3,9).")

def game(game_vars, farm):
    '''
    Main game loop for Sundrop Farm
    Args: 
        game_vars: A dictionary containing game variables('day','energy','money','bag')
        farm: A list of lists containing the farm layout
    '''
    while True: 
        # 1) Start a new game
        town_choice = in_town(game_vars)

        match town_choice:

            case "1":
                # 1) Visit Shop
                in_shop(game_vars,seeds,seed_list)

            case "2":
                # 2) Visit Farm
                while True:
                    if not in_farm():
                        break
            case "3":
                # 3) End Day
                break_game = end_day(game_vars)
                if break_game:
                    break
            case "9":
                save_game(game_vars, farm)
                break
            case "0":
                break
                # sys.exit()
            case _:
                print("Invalid choice. Please enter a valid option (0,1,2,3,9).")

def show_stats(game_vars):
    '''
    Displays the following statistics:
        - Day
        - Energy
        - Money
        - Contents of Seed Bag
    Args:
        game_vars: A dictionary containing game variables('day','energy','money','bag')
    '''
    print("+-----------------------------------------------+")
    print(f"| Day {game_vars['day']:<10} Energy: {game_vars["energy"]:<10} Money: ${game_vars["money"]:<4}|")
    if game_vars['bag']['Lettuce'] == 0 and game_vars['bag']['Potato'] == 0 and game_vars['bag']['Cauliflower'] == 0:
        print(f"| {'You have no seeds.':<45} |")
    else:
        print(f"{'| Your seeds:':<48}|")
        for seed, statistics in game_vars['bag'].items():
            if statistics > 0:
                print(f"|   {seed:<15}: {statistics:>5}{'':22}|")
    print("+-----------------------------------------------+")

def in_shop(game_vars,seeds,seed_list):
    '''
    Displays the menu of the seed shop, and allows players to buy seeds

    [Additional Feature added: Limited Capacity for Seed Bag (5 marks)]
    Seeds can be bought if player has enough money and bag has enough space (max 10 seeds)

    Ends when player selects to leave the shop

    Players can:
        1) Buy Lettuce seeds
        2) Buy Potato seeds
        3) Buy Cauliflower seeds
        0) Leave the shop
    Args:
        game_vars: A dictionary containing game variables('day','energy','money','bag')
        seeds: A dictionary containing seed information
        seed_list: A list of seed names
    '''

    print("Welcome to Pierce's Seed Shop!")
    show_stats(game_vars)
    
    while True:
        print("What do you wish to buy?")
        print(f"{'Seed':<15} {'Price':^10} {'Days to grow':^20} {'Crop Price':^10}")
        print("----------------------------------------------------------")
        print(f" {'1) Lettuce':<14} {seeds["LET"]['price']:^10} {seeds["LET"]['growth_time']:^20} {seeds["LET"]['crop_price']:^10}\n"
            f" {'2) Potato':<14} {seeds["POT"]['price']:^10} {seeds["POT"]['growth_time']:^20} {seeds["POT"]['crop_price']:^10}\n"
            f" {'3) Cauliflower':<14} {seeds["CAU"]['price']:^10} {seeds["CAU"]['growth_time']:^20} {seeds["CAU"]['crop_price']:^10}\n"
            "\n"
            " 0) Leave")
        print("----------------------------------------------------------")
        
        try:
            purchase_choice = input("Your choice? ")
            # if user wants to purchase a seed
            if int(purchase_choice) in [1,2,3]:
                print(f"You have ${game_vars["money"]}.")
                try:
                    purchase_quantity = int(input("How many do you wish to buy? "))
                    if purchase_quantity > 0: # CHECK: purchase_quantity is positive integer
                        match purchase_choice:
                            case "1":
                                total_cost = purchase_quantity * seeds["LET"]['price']
                            case "2":
                                total_cost = purchase_quantity * seeds["POT"]['price']
                            case "3":
                                total_cost = purchase_quantity * seeds["CAU"]['price']
                    else:
                        print("Please enter a valid quantity") # Error message if purchase_quantity is not positive integer
                        continue

                    if total_cost <= game_vars['money'] and sum(game_vars['bag'].values()) + purchase_quantity <= 10: # Additional feature: Limited Capacity for Seed Bag (5 marks)
                        game_vars['money'] -= total_cost

                        # Convert purchase_choice number into index of seed_list, and use the seed name as key
                        # to access seeds dictionary.
                        index = int(purchase_choice)-1 
                        seed_name = seeds[seed_list[index]]['name']
                        # seed name can be "Lettuce", "Potato", "Cauliflower"

                        game_vars['bag'][seed_name] += purchase_quantity

                        print(f"You bought {purchase_quantity} {seed_name} seeds.")
                        show_stats(game_vars)

                    elif sum(game_vars['bag'].values()) + purchase_quantity > 10:
                        # Additional feature: Limited Capacity for Seed Bag (5 marks)
                        print("You can't carry more than 10 seeds!")
                        show_stats(game_vars)

                    elif total_cost > game_vars['money']: # insufficient money to purchase seeds
                        print("You can't afford that!")
                        show_stats(game_vars)

                except ValueError:
                    print("Please enter a valid quantity")
            
            # If user decides to leave the shop
            elif purchase_choice == "0":
                break
            
            else:    # integer value but not intended input
                print("Invalid choice. Please enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter a valid number (0,1,2,3).")

def visit_farm(farm, game_vars):
    '''
    Displays the farm
    Each space on the farm has 3 rows
    # +-----+-----+-----+-----+-----+
    # |     |     |     |     |     |
    # |     |     |     |     |     |
    # |     |     |     |     |     |
    # +-----+-----+-----+-----+-----+
    # |     |     |     |     |     |
    # |     |     |     |     |     |
    # |     |     |     |     |     |
    # +-----+-----+-----+-----+-----+
    # |     |     | HSE |     |     |
    # |     |     |     |     |     |
    # |     |     |     |     |     |
    # +-----+-----+-----+-----+-----+
    # |     |     |     |     |     |
    # |     |     |     |     |     |
    # |     |     |     |     |     |
    # +-----+-----+-----+-----+-----+
    # |     |     |     |     |     |
    # |     |     |     |     |     |
    # |     |     |     |     |     |
    # +-----+-----+-----+-----+-----+
    Args: 
        farm: A list of lists containing the farm layout
        game_vars: A dictionary containing game variables('day','energy','money','bag')
    returns:
        direction: Player's choice to move
    '''

    line_across = '+-----' * len(farm[0]) + '+'

    for row in range(len(farm)):
        print(line_across)

        # Print content of the cells
        for line in range(3):  # Each cell has 3 lines of content, range(3) means 0,1,2 since 3 is exclusive
            for col in range(len(farm[0])):
                if farm[row][col][line] != '':
                    content = farm[row][col][line].center(5)
                else:
                    content = '     '
                print(f'|{content}', end='')
            print('|')

    # Print last line. Out of loop since it doesn't need to print the content of the cells
    print(line_across)

    row_x, col_x = find_position(farm)
    print(f"Energy: {game_vars['energy']}")
    print("[WASD] Move")

    if farm[row_x][col_x][0] == '' and farm[row_x][col_x][2] == '':
        print("P)lant seed")
    elif farm[row_x][col_x][0] != '' and farm[row_x][col_x][2] == '0':
        print(f"H)arvest {seeds[farm[row_x][col_x][0]]['name']} for ${seeds[farm[row_x][col_x][0]]['crop_price']}")

    print("R)eturn to Town")

def in_farm():
    '''
    Handles the actions on the farm. Player starts at (2,2), at the
    farmhouse.

    Possible actions:
    W, A, S, D - Moves the player
        - Will show error message if attempting to move off the edge
        - If move is successful, Energy is reduced by 1

    P - Plant a crop
        - Option will only appear if on an empty space
        - Shows error message if there are no seeds in the bag
        - If successful, Energy is reduced by 1

    H - Harvests a crop
        - Option will only appear if crop can be harvested, i.e., turns
        left to grow is 0
        - Option shows the money gained after harvesting
        - If successful, Energy is reduced by 1

    R - Return to town
        - Does not cost energy
    '''
    visit_farm(farm,game_vars)
    while True:
        try:
            farm_choice = input("Your choice? ").upper()
            if farm_choice in ['W','A','S','D']:
                move(farm, farm_choice, game_vars)
            elif farm_choice == 'P':
                plant_seed(farm, game_vars)
            elif farm_choice == 'H':
                harvest_crop(farm, game_vars)
            elif farm_choice == 'R':
                reset_farm(farm) # Move player back to farmhouse if he chooses to return to town
                return False
            else:
                print("Invalid choice. Please enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter a valid choice.")

def find_position(farm):
    '''
    Finds the position of the player on the farm
    Args:
        farm: A list of lists containing the farm layout
    Returns:
        row: Row position of the player
        col: Column position of the player
        (zero-based index for both row and column)
    '''
    for row in range(len(farm)):
        for col in range(len(farm[0])):
            if farm[row][col][1] == 'X':
                return row, col
            
def move(farm, farm_choice, game_vars):
    '''
    Handles the movement of player on the farm. Player starts at (2,2), at the
    farmhouse.

    Possible actions:
    W, A, S, D - Moves the player
    - Will show error message if attempting to move off the edge
    - If move is successful, Energy is reduced by 1

    Args:
        farm_choice: Player's choice to move
        farm: A list of lists containing the farm layout
        game_vars: A dictionary containing game variables('day','energy','money','bag')
    '''
    row, col = find_position(farm)

    if game_vars['energy'] > 0:
        moved = False

        # Move up
        if farm_choice == 'W' and row > 0 and farm[row-1][col][1] == '':
            farm[row][col][1], farm[row- 1][col][1] = '', 'X'
            moved = True
        # Move left
        elif farm_choice == 'A' and col > 0 and farm[row][col-1][1] == '':
            farm[row][col][1], farm[row][col - 1][1] = '', 'X'
            moved = True
        # Move down
        elif farm_choice == 'S' and row < (len(farm) - 1) and farm[row+1][col][1] == '':
            farm[row][col][1], farm[row + 1][col][1] = '', 'X'
            moved = True
        # Move right
        elif farm_choice == 'D' and col < (len(farm[0]) - 1) and farm[row][col+1][1] == '':
            farm[row][col][1], farm[row][col + 1][1] = '', 'X'
            moved = True
        else:
            print("Sorry, you are not allowed to move in that direction.")
    
        if moved:
            game_vars['energy'] -= 1 # Energy is reduced by 1 if move is successful
    
    # If energy is zero, then player can still input WASD, but the X will not move.
    # Instead, it prints the 'tired' message.
    else:
        print("You are too tired. You should get back to town.")

    visit_farm(farm, game_vars)

def reset_farm(farm):
    '''
    Resets the farm layout, moving the player back to the farmhouse
    Farmhouse is at (2,2)
    This function is called when player chooses to return to town
    Args:
        farm: A list of lists containing the farm layout
    '''
    for row in range(len(farm)):
        for col in range(len(farm[0])):
            if farm[row][col][1] == 'X':
                farm[row][col][1], farm[2][2][1] = '', 'X'

def plant_seed(farm, game_vars):
    '''
    Plant a seed on the farm
    - Option will only appear if on an empty space
    - Shows error message if there are no seeds in the bag
    - If successful, Energy is reduced by 1
    Args:
        farm: A list of lists containing the farm layout
        game_vars: A dictionary containing game variables('day','energy','money','bag')
    '''

    count = 1
    available_seeds = []
    row, col = find_position(farm)
    seeds_names = {"Lettuce": "LET", "Potato": "POT", "Cauliflower": "CAU"}
    
    if farm[row][col][0] == '' and game_vars['energy'] > 0 and any(value > 0 for value in game_vars['bag'].values()): # if empty and energy is more than 0 and bag has seeds
        print("-----------------------------------------------------------------")
        print(f"   {'Seed':<20}{'Days to Grow':^15}{'Crop Price':^15}{'Available':^15}")
        for seed_name, seed_qty in game_vars['bag'].items():
            if seed_qty > 0: # if there are seeds available
                crop_price = seeds[seeds_names[seed_name]]['crop_price']
                growth_time = seeds[seeds_names[seed_name]]['growth_time']
                print(f'{count}) {seed_name:<20}{growth_time:^15}{crop_price:^15}{seed_qty:^15}')
                available_seeds.append(seed_name)
                count += 1 
        print("-----------------------------------------------------------------")

        seed_choice = input("Which seed would you like to plant? ")

        if seed_choice.isdigit() and 0 < int(seed_choice) <= len(available_seeds): # check if input is a digit and within the range
            seed_to_plant = available_seeds[int(seed_choice) - 1]  # convert to zero-based index

            if game_vars['bag'][seed_to_plant] > 0: # if there are seeds available
                farm[row][col][0] = seeds_names[seed_to_plant]
                farm[row][col][2] = str(seeds[seeds_names[seed_to_plant]]['growth_time'])
                game_vars['bag'][seed_to_plant] -= 1
                game_vars['energy'] -= 1
                visit_farm(farm, game_vars)
        else:
            print("You don't have that seed.") # if input is not a digit

    elif farm[row][col][0] != '': # if not empty
        print("You are not allowed to plant a seed here.")
    
    elif game_vars['energy'] == 0:
        print("You are too tired. You should get back to town.")
    
    else:
        print("You don't have any seeds.")

def harvest_crop(farm, game_vars):
    '''
    Harvests a crop
    - Option will only appear if crop can be harvested, i.e., days left to grow is 0
    - Displays the money gained after harvesting
    - If successful, Energy is reduced by 1
    Args:
        farm: A list of lists containing the farm layout
        game_vars: A dictionary containing game variables('day','energy','money','bag')
    '''
    row, col = find_position(farm)

    if farm[row][col][2] == "0": # check if crop is ready for harvest
        game_vars['energy'] -= 1
        game_vars['money'] += seeds[farm[row][col][0]]['crop_price']

        print(f"You harvested the {seeds[farm[row][col][0]]['name'].capitalize()} and sold it for ${seeds[farm[row][col][0]]['crop_price']}!")
        print(f"You now have ${game_vars['money']}!")

        # empty square after harvest
        farm[row][col][0], farm[row][col][2]= '', ''
        visit_farm(farm, game_vars)

    else:
        print("You are unable to harvest!")

def end_day(game_vars):
    '''
    Ends the day
    - The day number increases by 1
    - Energy is reset to 10
    - Every planted crop has their growth time reduced by 1, to a minimum of 0
    Args:
        game_vars: A dictionary containing game variables('day','energy','money','bag')
    '''
    break_game = False

    if game_vars['day'] == 20:
        print(f"You have ${game_vars['money']} after 20 days.")
        break_game = True
        if game_vars['money'] >= 100:
            print(f"You paid off your debt of $100 and made a profit of ${game_vars['money'] - 100}.")
            print("You win!")
        else: 
            print("You have run out of time to pay off your debt. You lose.")

    game_vars['day'] += 1
    game_vars['energy'] = 10

    # Reduce growth time of crops by 1
    for row in range(len(farm)):
        for col in range(len(farm[0])):
            if farm[row][col][2] != '': 
                farm[row][col][2] = str(max(0, int(farm[row][col][2]) - 1)) # max returns the maximum of two values
    
    return break_game

def save_game(game_vars, farm):
    '''
    Saves the game into the file "savegame.txt"
    Args: 
        game_vars: A dictionary containing game variables('day','energy','money','bag')
        farm: A list of lists containing the farm layout
    '''
    with open("savegame.txt", "w") as file:
        file.write(f"{game_vars['day']}\n{game_vars['energy']}\n{game_vars['money']}\n") # first 3 lines: day, energy, money
        # next 3 lines: Lettuce, Potato, Cauliflower
        file.write(f"{game_vars['bag']['Lettuce']}\n{game_vars['bag']['Potato']}\n{game_vars['bag']['Cauliflower']}\n") 

        for row in range(len(farm)):
            for col in range(len(farm[row])):
                file.write(f"{row},{col},{farm[row][col][0]}:{farm[row][col][1]}:{farm[row][col][2]}\n")

        print("Game saved.")

def load_game(game_vars, farm):
    '''
    Loads the saved game by reading the file "savegame.txt"
    if the file is not found, prints "No saved game found." (FileNotFoundError)
    Args:
        game_vars: A dictionary containing game variables('day','energy','money','bag')
        farm: A list of lists containing the farm layout
    '''
    try:
        with open("savegame.txt", "r") as file:
            lines = file.readlines()
            game_vars['day'] = int(lines[0].strip())
            game_vars['energy'] = int(lines[1].strip())
            game_vars['money'] = int(lines[2].strip())
            game_vars['bag']['Lettuce'] = int(lines[3].strip())
            game_vars['bag']['Potato'] = int(lines[4].strip())
            game_vars['bag']['Cauliflower'] = int(lines[5].strip())

            for line in lines[6:]:
                farm_load_list = line.strip().split(",")
                farm_load_list = [int(farm_load_list[0]), int(farm_load_list[1]), farm_load_list[2].split(":")]
                farm[farm_load_list[0]][farm_load_list[1]] = farm_load_list[2]
            print("Game saved.")
    except FileNotFoundError:
        print("No saved game found.")

#----------------------------------------------------------------------
#    Main Game Loop
#----------------------------------------------------------------------

while True:
    display_main_menu()
    try:
        option = input("Your choice? ")

        match option:

            case "0":
                # 0) Exit Game
                print("Goodbye!")
                break

            case "1":
                game(game_vars,farm)

            case "2":
                load_game(game_vars,farm)
                game(game_vars,farm)
            case _:
                # Integer input but not 1, 2 or 0
                print("Invalid choice. Please enter a valid option (0,1,2).")

    except ValueError:
        print("Enter a valid number (1,2,0).")

