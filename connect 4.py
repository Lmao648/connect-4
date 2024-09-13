import turtle
import time
screen = turtle.Screen()
screen.setup(800, 800)
screen.setworldcoordinates(-500,-500,500,500)


screen.tracer(0)#stop screen update
turtle.speed(0)#add speed


rows = 6
columns = 7
circle_list = []
turn=1
x_position = -450
y_position = -450*(rows)/columns
board_height_start = -2*y_position #switch these
board_width_start = -2*x_position


def rectangle_draw (xpos, ypos, board_width_start, board_height_start):
   turtle.penup()
   turtle.goto(xpos, ypos)
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
   turtle.seth(0)#forgot to set angle
   turtle.fillcolor(color)
   turtle.pendown()
   turtle.begin_fill()
   turtle.circle(radius, 360, 150)
   turtle.end_fill()
  
def list_of_circles():
   global circle_list
   for i in range(rows):#changed to rows
       row = []
       for j in range(columns):
           row.append(0)
       circle_list.append(row)


def adding_circles():
   global circle_list
   amount_of_row_gap = board_height_start/rows
   amount_of_column_gap = board_width_start/columns
   radius = amount_of_row_gap / 3 #put amt row gap up
   circle_y_position = y_position + amount_of_row_gap / 2
  
   for i in range(rows):#sub x y pos with xcircle, ycircle pos
       circle_x_position = x_position + amount_of_column_gap / 2
       for j in range(columns):
           if circle_list[i][j]==0:
               circle_draw(circle_x_position, circle_y_position, radius, "white")
              
           elif circle_list[i][j] == 1:
               circle_draw(circle_x_position,circle_y_position,radius,'black')
           else:
               circle_draw(circle_x_position,circle_y_position,radius,'red')
           circle_x_position += amount_of_column_gap #have to increment xpos at column
       circle_y_position += amount_of_row_gap#have to increment ypos at row


# place piece in col for turn
#return the current row you're on
def place_piece(bb,turn,col):
   for i in range(rows):
       if bb[i][col] == 0:
           bb[i][col] = turn
           return i
      
def place_piece_and_draw(bb,turn,col):
   row = place_piece(bb,turn,col)
   row_gap = board_height_start/rows
   col_gap = board_width_start/columns
   Y = x_position + (row_gap*row + row_gap / 2)+64
   X = y_position + (col_gap*col + col_gap/2)-64
   i = row
   j = col
   if circle_list[i][j] == 0:
       circle_draw(X,Y,row_gap/3,'white')
   elif circle_list[i][j] == 1:
       for k in range(5):
           circle_draw(X,Y,row_gap/3,'white')
           screen.update()#add screen update and sleep here
           time.sleep(0.05)
           circle_draw(X,Y,row_gap/3,'black')
           screen.update()
           time.sleep(0.05)
   else:
       for k in range(5):
           circle_draw(X,Y,row_gap/3,'white')
           screen.update()
           time.sleep(0.05)
           circle_draw(X,Y,row_gap/3,'red')
           screen.update()
           time.sleep(0.05)
   return row


def play(x,y):
   global turn,working
   if working: return
   working = True
   cols = [] #naming choice
   for i in range(7):
       col = 900/7 * i - 450 + 900/14
       cols.append(col)
   #doesn't print columns list, check
   for i in range(len(cols)):
       if abs(x-cols[i]) < 900/14*2/3 and circle_list[rows-1][i]==0:
           place_piece_and_draw(circle_list,turn,i)#don't need to make it equal
          
           #drawPiece = place_piece_and_draw(circle_list,turn,i)#actual line
           #r = game_over_lastmove(board,turn,drawPiece,i)
           '''
           r = -2#added temp
           if r==0:
               screen.textinput('Game over','tie')
           elif r==1:
               screen.textinput('Game over','player 1 won')
           elif r==-1:
               screen.textinput('Game over','player 2 won')
           if r!=-2: screen.bye()'''
           turn = -turn
   working = False




list_of_circles()
print(circle_list)
rectangle_draw(x_position, y_position, board_width_start, board_height_start)
adding_circles()




working=False
screen.onclick(play)


screen.update()#makes turtle instantaneous
screen.mainloop()#mainloop at end



