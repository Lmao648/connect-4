import turtle
player_turn = 1
game_still_running = True
circle_list = []
screen = turtle.Screen()
screen.setup(800, 800)
screen.setworldcoordinates(-500,-500,500,500)
rows = 6
columns = 7
x_position = -450
y_position = -450*(rows)/columns
board_height_start = -2*y_position
board_width_start = -2*x_position
turtle.speed(100)
def rectangle_draw (x_position, y_position, board_height_start, board_width_start):
    turtle.penup()
    turtle.goto(x_position, y_position)
    turtle.seth(0)
    turtle.pendown()
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.forward(board_width_start)
    turtle.left(90)
    turtle.forward(board_height_start)
    turtle.left(90)
    turtle.forward(board_width_start)
    turtle.left(90)
    turtle.forward(board_height_start)
    turtle.left(90)
    turtle.end_fill()

def circle_draw (x_position, y_position, radius, color):
    turtle.penup()
    turtle.goto(x_position, y_position - radius)
    turtle.seth(0)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius, 360, 150)
    turtle.end_fill()

def list_of_circles():
    global circle_list
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(0)
        circle_list.append(row)

def adding_circles():
    global circle_list
    amount_of_row_gap = board_height_start/rows
    amount_of_column_gap = board_width_start/columns
    radius = amount_of_row_gap / 3
    circle_y_position = y_position + amount_of_row_gap / 2
    for i in range(rows):
        circle_x_position = x_position + amount_of_column_gap / 2
        for j in range(columns):
            if circle_list[i][j]==0:
                circle_draw(circle_x_position, circle_y_position, radius, "white")
            if circle_list[i][j]==1:
                circle_draw(circle_x_position, circle_y_position, radius, "red")
            if circle_list[i][j]==2:
                circle_draw(circle_x_position, circle_y_position, radius, "black")
            circle_x_position = circle_x_position + amount_of_column_gap
        circle_y_position = circle_y_position + amount_of_row_gap

def placing_pieces(board, turn, column):
    for i in range(rows):
        if board[i][column]==0: 
            board[i][column]=turn
            return i
        
def placing_player_pieces(board, turn, column): #drawing method
    global circle_list
    row = placing_pieces(board, turn, column)
    amount_row_gap = board_height_start/rows
    amount_column_gap = board_width_start/columns
    circle_y_position = y_position + amount_row_gap / 2
    circle_x_position = x_position + amount_column_gap / 2
    rows2 = 6
    columns2 = 7
    radius = amount_row_gap / 3
    if circle_list[rows2][columns2] == 0:
        circle_draw(circle_x_position, circle_y_position, radius, "white")
    if circle_list[rows2][columns2] == 2:
        for i in range (5):
            circle_draw(circle_x_position, circle_y_position, radius, "white")
            circle_draw(circle_x_position, circle_y_position, radius, "black")
    if circle_list[rows2][columns2] == 1:
        for i in range (5):
            circle_draw(circle_x_position, circle_y_position, radius, "white")
            circle_draw(circle_x_position, circle_y_position, radius, "red")
    return rows2

def in_play(x, y):
    global player_turn
    global game_still_running
    global circle_list
    columns3 = []
    if game_still_running:
        return
    for i in range(7):
        col = 900/7*i-450+900/14 
        columns3.append(col)
    print(columns3)
    for i in range(len(columns3)):
        if abs(x-columns3[i]) < 900/14*2/3 and circle_list[rows-1][i]==0:
            placing_player_pieces(circle_list, player_turn, i)
            
            #if turn == 1:
                #screen.textinput("Game Over, Player 2 Loses, Player 1 Wins")
            #if turn == 2:
                #screen.textinput("Game Over, Player 1 Loses, Player 2 Wins")
            #if game_draw:
                #screen.textinput("Game Over, Nobody Won")
            player_turn = -player_turn
        #if statement to check which column to add

list_of_circles()
print(circle_list)
rectangle_draw(x_position, y_position, board_height_start, board_width_start)
adding_circles()

screen.onclick(in_play)
screen.mainloop()