# Game variables
game_vars = {
    'day': 1,
    'energy': 10,
    'money': 20,
    'bag': {},
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
    if game_vars['bag'] == {}:
        print(f"| {"Your have no seeds.":46}|")
    else:
        print(f"{'| Your seeds:':<48}|")
        for seed, statistics in game_vars['bag'].items():
            print(f"|   {seed:<15}: {statistics[2]:>5}{'':22}|")
    print("+-----------------------------------------------+")

def in_shop(game_vars,seeds,seed_list):
    '''
    Displays the menu of the seed shop, and allows players to buy seeds
    Seeds can be bought if player has enough money
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

    # Prints once
    print("Welcome to Pierce's Seed Shop!")
    print("+-----------------------------------------------+")
    print(f"| Day {game_vars['day']:<10} Energy: {game_vars["energy"]:<10} Money: ${game_vars["money"]:<4}|")
    if game_vars['bag'] == {}:
        print(f"| {'You have no seeds.':<45} |")
    print("+-----------------------------------------------+")
    
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

                    # Buying seeds with sufficient money
                    if total_cost <= game_vars['money']:
                        game_vars['money'] -= total_cost

                        # Convert purchase_choice number into index of seed_list, and use the seed name as key
                        # to access seeds dictionary.
                        index = int(purchase_choice)-1 
                        seed_name = seeds[seed_list[index]]['name'] # seed_list = ['LET', 'POT', 'CAU']
                        # seed name can be "Lettuce", "Potato", "Cauliflower"

                        # Update dictionary accordingly
                        if seed_name in game_vars['bag']:
                            game_vars['bag'][seed_name][2] += purchase_quantity
                        else:
                            game_vars['bag'][seed_name] = [seeds[seed_list[index]]['growth_time'], 
                                                           seeds[seed_list[index]]['crop_price'], 
                                                           purchase_quantity,
                                                           seed_list[index]]

                        print(f"You bought {purchase_quantity} {seed_name} seeds.")
                        show_stats(game_vars)
                    
                    # insufficient money to purchase seeds
                    else:
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
    if farm[row_x][col_x][0] == '' and farm [row_x][col_x][2] == '':
        print(f"Energy: {game_vars['energy']}")
        print("[WASD] Move")
        print("P)lant seed")
        print("R)eturn to Town")
    
    else:
        print(f"Energy: {game_vars['energy']}")
        print("[WASD] Move")
        print("R)eturn to Town")


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
                farm[row][col][1] = ''
                farm[2][2][1] = 'X'

def plant_seed(farm, game_vars):
    bag_items = list(game_vars['bag'].items()) # Convert dictionary to list of tuples
    # Example: [('Lettuce', [2, 3, 5, 'LET']), ('Potato', [3, 6, 1, 'POT']), ('Cauliflower', [6, 14, 1, 'CAU'])]

    row, col = find_position(farm)
    
    if farm[row][col][0] == '' and game_vars['energy'] > 0 and len(bag_items) > 0: # if empty and energy is more than 0 and bag has seeds
        print("-----------------------------------------------------------------")
        print(f"   {'Seed':<20}{'Days to Grow':^15}{'Crop Price':^15}{'Available':^15}")
        for i in range(len(bag_items)):
            if bag_items[i][1][2] > 0:
                print(f'{i+1}) {bag_items[i][0]:<20}{bag_items[i][1][0]:^15}{bag_items[i][1][1]:^15}{bag_items[i][1][2]:^15}')
        print("-----------------------------------------------------------------")
        seed_choice = input("Which seed would you like to plant? ")

        if seed_choice.isdigit() and 0 < int(seed_choice) <= len(bag_items): # if input is a digit and within the range
            seed_choice = int(seed_choice) - 1 # Convert to zero-based index
            seed_to_plant = bag_items[seed_choice][0]
            if game_vars['bag'][seed_to_plant][2] > 0: # if there are seeds available
                farm[row][col][0] = game_vars['bag'][seed_to_plant][3]
                farm[row][col][2] = str(game_vars['bag'][seed_to_plant][1])
                game_vars['bag'][seed_to_plant][2] -= 1
                game_vars['energy'] -= 1
                visit_farm(farm, game_vars)
        else:
            print("You don't have that seed.")

    elif farm[row][col][0] != '': # if not empty
        print("You are not allowed to plant a seed here.")
    
    elif game_vars['energy'] == 0:
        print("You are too tired. You should get back to town.")
    
    else:
        print("You don't have any seeds.")

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
            elif farm_choice == 'R':
                reset_farm(farm) # Move player back to farmhouse if he chooses to return to town
                return False
            else:
                print("Invalid choice. Please enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter a valid choice.")

#----------------------------------------------------------------------
# end_day(game_vars)
#
#    Ends the day
#      - The day number increases by 1
#      - Energy is reset to 10
#      - Every planted crop has their growth time reduced by 1, to a
#        minimum of 0
#----------------------------------------------------------------------
def end_day(game_vars):
    pass


#----------------------------------------------------------------------
# save_game(game_vars, farm)
#
#    Saves the game into the file "savegame.txt"
#----------------------------------------------------------------------
def save_game(game_vars, farm):
    pass

#----------------------------------------------------------------------
# load_game(game_vars, farm)
#
#    Loads the saved game by reading the file "savegame.txt"
#----------------------------------------------------------------------
def load_game(game_vars, farm):
    pass

#----------------------------------------------------------------------
#    Main Game Loop
#----------------------------------------------------------------------

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
    print("You have 30 days to pay off your debt of $100.")
    print("You might even be able to make a little profit.")
    print("How successful will you be?")
    print("----------------------------------------------------------")
    print("1) Start a new game\n"
          "2) Load your saved game\n"
          "\n"
          "0) Exit Game")

# Write your main game loop here
while True:
    display_main_menu()
    try:
        option = input("Your choice? ")

        match option:

            case "0":
                # 0) Exit Game
                break

            case "1":

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
                            pass
                        case "9":
                            pass
                        case "0":
                            break
                        case _:
                            print("Invalid choice. Please enter a valid option (0,1,2,3,9).")

            case "2":
                # 2) Load your saved game
                pass
                
            case _:
                # Integer input but not 1, 2 or 0
                print("Invalid choice. Please enter a valid option (0,1,2).")

    except ValueError:
        print("Enter a valid number (1,2,0).")

