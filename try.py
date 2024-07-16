map = [ [' ', 'T', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
      ]

def display_map(map):
    for row in map:
        print("+---+---+---+---+---+")
        print("|"," | ".join(row),"|")
    print("+---+---+---+---+---+")

def find_t_position(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'T':
                return i,j # return the coordinates of 'T'

def move(map,direction):
    i, j = find_t_position(map)
    if direction == 'w' and i > 0 and map[i-1][j] == ' ':
        map[i][j], map[i-1][j] = ' ', 'T'
    elif direction == 'a' and j > 0 and map[i][j-1] == ' ':
        map[i][j], map[i][j-1] = ' ', 'T'
    elif direction == 's' and i < len(map)-1 and map[i+1][j] == ' ':
        map[i][j], map[i+1][j] = ' ', 'T'
    elif direction == 'd' and j < len(map[i])-1 and map[i][j+1] == ' ':
        map[i][j], map[i][j+1] = ' ', 'T'
    else:
        print("Sorry, you are not allowed to move in that direction.")
def main():
    while True:
        display_map(map)
        direction = input("Enter your direction or Q to quit: ").lower()
        if direction == 'q':
            break
        elif direction in 'wasd':
            move(map, direction)
main()


