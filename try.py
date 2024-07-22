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
    print(f"| Day {game_vars['day']:<10} Energy: {game_vars['energy']:<10} Money: ${game_vars['money']:<4}|")
    if game_vars['bag'] == {}:
        print(f"| {'You have no seeds.':46}|")
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
    print(f"| Day {game_vars['day']:<10} Energy: {game_vars['energy']:<10} Money: ${game_vars['money']:<4}|")
    if game_vars['bag'] == {}:
        print(f"| {'You have no seeds.':<45} |")
    print("+-----------------------------------------------+")
    
    while True:
        print("What do you wish to buy?")
        print(f"{'Seed':<15} {'Price':^10} {'Days to grow':^20} {'Crop Price':^10}")
        print("----------------------------------------------------------")
        print(f" {'1) Lettuce':<14} {seeds['LET']['price']:^10} {seeds['LET']['growth_time']:^20} {seeds['LET']['crop_price']:^10}\n"
            f" {'2) Potato':<14} {seeds['POT']['price']:^10} {seeds['POT']['growth_time']:^20} {seeds['POT']['crop_price']:^10}\n"
            f" {'3) Cauliflower':<14} {seeds['CAU']['price']:^10} {seeds['CAU']['growth_time']:^20} {seeds['CAU']['crop_price']:^10}\n"
            "\n"
            " 0) Leave")
        print("----------------------------------------------------------")
        
        try:
            purchase_choice = input("Your choice? ")
            # if user wants to purchase a seed
            if int(purchase_choice) in [1,2,3]:
                print(f"You have ${game_vars['money']}.")
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
                        seed_code = seed_list[index]  # seed_list = ['LET', 'POT', 'CAU']
                        seed_name = seeds[seed_code]['name']  # seed name can be "Lettuce", "Potato", "Cauliflower"

                        # Update dictionary accordingly
                        if seed_name in game_vars['bag']:
                            game_vars['bag'][seed_name][2] += purchase_quantity
                        else:
                            game_vars['bag'][seed_name] = [seeds[seed_code]['growth_time'], 
                                                           seeds[seed_code]['crop_price'], 
                                                           purchase_quantity,
                                                           seed_code]

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
    '''
    print("Welcome to your farm! Here is your current farm layout:")
    display_farm(farm)
    print("\nYou can:")
    print("1) Plant a seed")
    print("2) Harvest crops")
    print("3) Return to town")
    
    while True:
        try:
            choice = int(input("Your choice? "))
            if choice == 1:
                plant_seed(farm, game_vars)
                display_farm(farm)
            elif choice == 2:
                harvest_crops(farm, game_vars)
                display_farm(farm)
            elif choice == 3:
                break
            else:
                print("Invalid choice. Please enter a valid choice (1,2,3).")
        except ValueError:
            print("Invalid input. Please enter a valid number (1,2,3).")

def display_farm(farm):
    '''
    Displays the farm layout
    Args:
        farm: A list of lists containing the farm layout
    '''
    print("+-----+-----+-----+-----+-----+")
    for row in farm:
        for cell in row:
            print(f"| {cell[0]:^3} ", end="")
        print("|")
        for cell in row:
            print(f"| {cell[1]:^3} ", end="")
        print("|")
        for cell in row:
            print(f"| {cell[2]:^3} ", end="")
        print("|")
        print("+-----+-----+-----+-----+-----+")

def plant_seed(farm, game_vars):
    '''
    Allows the player to plant seeds on the farm
    Player can select the type of seed and the position to plant
    Each planting action costs 1 energy
    Args:
        farm: A list of lists containing the farm layout
        game_vars: A dictionary containing game variables('day','energy','money','bag')
    '''
    if game_vars['energy'] <= 0:
        print("You don't have enough energy to plant seeds.")
        return

    if not game_vars['bag']:
        print("You don't have any seeds to plant.")
        return

    print("You have the following seeds in your bag:")
    for i, (seed_name, seed_info) in enumerate(game_vars['bag'].items(), 1):
        print(f"{i}) {seed_name}: {seed_info[2]} seeds available")
    
    try:
        seed_choice = int(input("Which seed do you want to plant? ")) - 1
        if seed_choice not in range(len(game_vars['bag'])):
            print("Invalid choice. Please choose a valid seed.")
            return
        
        seed_name = list(game_vars['bag'].keys())[seed_choice]
        seed_code = game_vars['bag'][seed_name][3]
        
        print("Choose a position to plant the seed:")
        for i, row in enumerate(farm):
            for j, cell in enumerate(row):
                print(f"{i},{j}", end=" ")
            print()
        
        row_choice = int(input("Row: "))
        col_choice = int(input("Column: "))
        
        if (0 <= row_choice < len(farm)) and (0 <= col_choice < len(farm[0])):
            if farm[row_choice][col_choice][0] == '':
                farm[row_choice][col_choice] = [seed_code, 'PLT', seeds[seed_code]['growth_time']]
                game_vars['bag'][seed_name][2] -= 1
                if game_vars['bag'][seed_name][2] == 0:
                    del game_vars['bag'][seed_name]
                game_vars['energy'] -= 1
                print(f"You planted {seed_name} at ({row_choice},{col_choice}).")
            else:
                print("This position is already occupied.")
        else:
            print("Invalid position. Please choose a valid position.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def harvest_crops(farm, game_vars):
    '''
    Allows the player to harvest crops on the farm
    Each harvesting action costs 1 energy
    Args:
        farm: A list of lists containing the farm layout
        game_vars: A dictionary containing game variables('day','energy','money','bag')
    '''
    if game_vars['energy'] <= 0:
        print("You don't have enough energy to harvest crops.")
        return
    
    harvested = False
    for i, row in enumerate(farm):
        for j, cell in enumerate(row):
            if cell[0] != '' and cell[2] == '0':
                seed_code = cell[0]
                crop_name = seeds[seed_code]['name']
                crop_price = seeds[seed_code]['crop_price']
                game_vars['money'] += crop_price
                farm[i][j] = ['','','']
                game_vars['energy'] -= 1
                harvested = True
                print(f"You harvested {crop_name} at ({i},{j}) and earned ${crop_price}.")
    
    if not harvested:
        print("There are no crops ready to harvest.")
    
while True:
    choice = in_town(game_vars)
    if choice == "1":
        in_shop(game_vars, seeds, seed_list)
    elif choice == "2":
        visit_farm(farm, game_vars)
    elif choice == "3":
        end_day(game_vars, farm)
    elif choice == "9":
        print("Game saved (not implemented).")
    elif choice == "0":
        print("Exiting game.")
        break
