game_vars = {
    'day': 1,
    'energy': 10,
    'money': 20,
    'bag': {},
}

farm = [ [['','',''], ['','',''], ['','',''], ['','',''], ['','','']],
         [['','',''], ['','',''], ['','',''], ['','',''], ['','','']],
         [['','',''], ['','',''], ['HSE','X',''], ['','',''], ['','','']],
         [['','',''], ['','',''], ['','',''], ['','',''], ['','','']],
         [['','',''], ['','',''], ['','',''], ['','',''], ['','','']] ]

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
    Move the player on the farm according to the player's choice
    Args:
        farm_choice: Player's choice to move
    '''
    row, col = find_position(farm)

    if game_vars['energy'] > 0:
        moved = False
        if farm_choice == 'W' and row > 0 and farm[row-1][col][1] == '':
            farm[row][col][1], farm[row- 1][col][1] = '', 'X'
            moved = True
        elif farm_choice == 'A' and col > 0 and farm[row][col-1][1] == '':
            farm[row][col][1], farm[row][col - 1][1] = '', 'X'
            moved = True
        elif farm_choice == 'S' and row < (len(farm) - 1) and farm[row+1][col][1] == '':
            farm[row][col][1], farm[row + 1][col][1] = '', 'X'
            moved = True
        elif farm_choice == 'D' and col < (len(farm[0]) - 1) and farm[row][col+1][1] == '':
            farm[row][col][1], farm[row][col + 1][1] = '', 'X'
            moved = True
        else:
            print("Sorry, you are not allowed to move in that direction.")
    
        if moved:
            game_vars['energy'] -= 1
    
    # If energy is zero, then player can still input WASD, but the X will not move.
    # Instead, it prints the 'tired' message.
    else:
        print("You are too tired. You should get back to town.")
    
    visit_farm(farm, game_vars)

def in_farm():
    visit_farm(farm,game_vars)
    while True:
        try:
            farm_choice = input("Your choice? ").upper()
            if farm_choice in ['W','A','S','D']:
                move(farm, farm_choice, game_vars)
            elif farm_choice == 'R':
                return False
            else:
                print("Invalid choice. Please enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter a valid choice.")


while True:
    if not in_farm():
        break
