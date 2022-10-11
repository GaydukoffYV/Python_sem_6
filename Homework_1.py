maps = list(range(1,10))
victories = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
def print_maps():
    for i in range(3):
        print( " ", maps[0+i*3], " ", maps[1+i*3], " ", maps[2+i*3], " ")
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol
def get_result():
    win = "" 
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "Игрок"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "Компьютер"                
    return win
def check_line(sum_O,sum_X): 
    step = ""
    for line in victories:
        o = 0
        x = 0
        for j in range(0,3):
            if maps[line[j]] == "O":
                o = o + 1
            if maps[line[j]] == "X":
                x = x + 1
        if o == sum_O and x == sum_X:
            for j in range(0,3):
                if maps[line[j]] != "O" and maps[line[j]] != "X":
                    step = maps[line[j]]                
    return step
def AI():        
    step = ""
    step = check_line(2,0) 
    if step == "":
        step = check_line(0,2)          
    if step == "":
        step = check_line(1,0)           
    if step == "":
        if maps[4] != "X" and maps[4] != "O":
            step = 5           
    if step == "":
        if maps[0] != "X" and maps[0] != "O":
            step = 1              
    return step
game_over = False
human = True
 
while game_over == False:
    print_maps()
    if human == True:
        symbol = "X"
        step = int(input("Игрок делает ход: "))
    else:
        print("Компьютер делает ход: ")
        symbol = "O"
        step = AI()
    if step != "":
        step_maps(step,symbol) 
        win = get_result() 
        if win != "":
            game_over = True
        else:
            game_over = False
    else:
        print("Ничья!")
        game_over = True
        win = "дружба"
 
    human = not(human)              
print_maps()
print("Победил", win)  


