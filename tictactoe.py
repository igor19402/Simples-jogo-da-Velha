# write your code here

# Project Final


game = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
print("---------")
print("|", game[0], game[1], game[2], "|")
print("|", game[3], game[4], game[5], "|")
print("|", game[6], game[7], game[8], "|")
print("---------")

numbers_grid = [1, 2, 3]
check_numerics = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
state_of_game = True
count_not_numbers = 0
time_player = 1

while state_of_game:
    print("Enter the coordinates:")
    positions = input().split()
    count_not_numbers = 0
    for n in positions:
        if n not in check_numerics:
            count_not_numbers += 1
    if count_not_numbers > 0:
        print("You should enter numbers!")
    else:
        row = int(positions[0])
        column = int(positions[1])
        index = (((row - 1) * 3) + (column + 2)) - 3
        if (row not in numbers_grid) or (column not in numbers_grid):
            print("Coordinates should be from 1 to 3!")
        elif game[index] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            if time_player % 2 == 0:
                game[index] = "O"
            else:
                game[index] = "X"
            time_player += 1
            print("---------")
            print("|", game[0], game[1], game[2], "|")
            print("|", game[3], game[4], game[5], "|")
            print("|", game[6], game[7], game[8], "|")
            print("---------")
            if (game[0] == game[1] == game[2]) or (game[3] == game[4] == game[5]) or (game[6] == game[7] == game[8]):
                if game[0] == game[1] == game[2] == 'X':
                    print("X wins")
                    break
                elif game[0] == game[1] == game[2] == 'O':
                    print("O wins")
                    break
                if game[3] == game[4] == game[5] == 'X':
                    print("X wins")
                    break
                elif game[3] == game[4] == game[5] == 'O':
                    print("O wins")
                    break
                if game[6] == game[7] == game[8] == 'X':
                    print("X wins")
                    break
                elif game[6] == game[7] == game[8] == 'O':
                    print("O wins")
                    break
            elif (game[0] == game[3] == game[6]) or (game[1] == game[4] == game[7]) or (game[2] == game[5] == game[8]):
                if game[0] == game[3] == game[6] == 'X':
                    print("X wins")
                    break
                elif game[0] == game[3] == game[6] == 'O':
                    print("O wins")
                    break
                if game[1] == game[4] == game[7] == 'X':
                    print("X wins")
                    break
                elif game[1] == game[4] == game[7] == 'O':
                    print("O wins")
                    break
                if game[2] == game[5] == game[8] == 'X':
                    print("X wins")
                    break
                elif game[2] == game[5] == game[8] == 'O':
                    print("O wins")
                    break
            elif (game[0] == game[4] == game[8]) or (game[2] == game[4] == game[6]):
                if game[0] == game[4] == game[8] == 'X':
                    print("X wins")
                    break
                elif game[0] == game[4] == game[8] == 'O':
                    print("O wins")
                    break
                if game[2] == game[4] == game[6] == 'X':
                    print("X wins")
                    break
                elif game[2] == game[4] == game[6] == 'O':
                    print("O wins")
                    break
            elif " " not in game:
                print("Drawn")
                break

