import copy
import random

class Board:
  def __init__(self, board):
    self.board = copy.deepcopy(board)

  def place_token(self, token, column):
    if -1 < column < 7:
      if len(self.board[column]) != 6:
        self.board[column].append(token) #adds token to lowest empty spot of column
        return True
    return False

  def print_board(self):
    for i in range (5, -1, -1):
      print ("|", end="") #end="" means to print on same line
      for j in range (7):
        if i < len(self.board[j]): #limits i to len(board)
          print (self.board[j][i] + "|", end ="")
        else:
          print (" |", end ="")
      print() #show new line
    print()
 #tie 
  def tie(self):
    for i in range (7):
      if len(self.board[i]) != 6: #if board isn't full
        return False #it isn't a tie
    return True

#win, block, nothing   
  def check(self, token, opponent, column):
  #row win
    if column < 3:#columns 1,2,3- player's input
      for i in range (6):#loop through all rows
        for j in range (column + 1):#starting column for every 4 column
            count = 0
            for k in range(4): #find current column
              if i < len(self.board[j + k]):#if i is less than how many tokens in column  
                if self.board[j+k][i] == token: #where token is
                  count += 1
            if count == 4: #four in a row
              return 1

    if column >= 3:#columns 4,5,6,7- player's input
      for i in range (6): #every row 
        for j in range (column - 3, 4): #starting column starting from 3 less than the column to the fourth column
          count = 0 #tokens in a row
          for k in range(4): #add to the starting column to find current column being checked
            if i < len(self.board[j + k]):#row being checked if less than the length of column
              if token == self.board[j + k][i]:#token in spot is token being passed in
                count += 1#add one if tokens are same
          if count == 4: #four in a row
            return 1

  #column win
    for i in range (3): #if i == 3, 4 + 3 = 7, index is out of bounds
      count = 0
      for j in range (4):
        if i + j < len(self.board[column]):#if current row is less than length of the column passed in as  parameter
          if token == self.board[column][i + j]: #token in spot is the same as token being passed in
            count += 1 #add one if tokens are same
      if count == 4: #four tokens in a row 
            return 1

  #diagonal win (left to right)
    for i in range (4): #horizontaly
      for j in range (2):#verticaly
        count = 0
        for k in range (4):#incraments up
          if j + k < len(self.board[i + k]):
            if self.board[i + k][j + k] == token:
              count += 1
        if count == 4:
          return 1
          
  #diagonal win (right to left) 
    for i in range (6, 2, -1): #right to middle
      for j in range (2): #4+ j won't be out of bounds
        count = 0
        for k in range (4): #current row - j
          if j + k < len(self.board[i - k]): #row isn't out of bounds
            if self.board[i - k][j + k] == token:
              count += 1
        if count == 4:
          return 1

  #row block
    if column < 3:#columns 1,2,3- player's input
      for i in range (6):#loop through all rows
        for j in range (column + 1):#starting column for every 4 column
          opponent_count = 0
          count = 0
          for k in range(4): #find current column
            if i < len(self.board[j + k]):#if i is less than how many tokens in column  
              if self.board[j+k][i] == opponent:
                opponent_count += 1
              elif self.board[j+k][i] == token:
                if column == j + k and i == len(self.board[column]) - 1: #checks current row and column is last token put in
                  count += 1
          if opponent_count == 3 and count == 1:
            return -1
    
    if column >= 3:#columns 4,5,6,7- player's input
      for i in range (6): #every row 
        for j in range (column - 3, 4): #starting column starting from 3 less than the column to the fourth column
          opponent_count = 0
          count = 0 #tokens in a row
          for k in range(4): #add to the starting column to find current column being checked
            if i < len(self.board[j + k]):#row being checked if less than the length of column
              if self.board[j+k][i] == opponent:
                opponent_count += 1
              elif self.board[j+k][i] == token:
                if column == j + k and i == len(self.board[column]) - 1: #checks current row and column is last token put in
                  count += 1
          if opponent_count == 3 and count == 1: #four in a row
            return -1

    #column block
      for i in range (3): #if i == 3, 4 + 3 = 7, index is out of bounds
        opponent_count = 0
        count = 0
        for j in range (4):
          if i + j < len(self.board[column]):#if current row is less than length of the column passed in as  parameter
            if self.board[column][i+j] == opponent:
              opponent_count += 1
            elif self.board[column][i+j] == token:
              if i + j == len(self.board[column]) - 1: #checks row and column is last token put in
                count += 1
          if opponent_count == 3 and count == 1:
            return -1   

    #diagonal block (left to right)
      for i in range (4): #horizontaly
        for j in range (2):#verticaly
          opponent_count = 0
          count = 0
          for k in range (4):#incraments up
            if i + k < len(self.board[j + k]):
                if self.board[j+k][i] == opponent:
                    opponent_count += 1
                elif self.board[j+k][i] == token:
                  if column == i + k: #checks row and column is last token put in
                    count += 1
          if opponent_count == 3 and count == 1:
            return -1  

    #diagonal block (right to left)
    for i in range (6, 2, -1): #right to middle
      for j in range (2): #4+ j won't be out of bounds
        opponent_count = 0
        count = 0
        for k in range (4): #current row - j
          if i + k < len(self.board[j - k]): #row isn't out of bounds
            if self.board[j-k][i] == opponent:
              opponent_count += 1
            elif self.board[j-k][i] == token:
              if column == i - k: #checks row and column is last token put in
                count += 1
        if opponent_count == 3 and count == 1:
          return -1
    return 0 #if not block or win situation

class Node:
  def __init__(self, board):
    self.board = Board(board)
    self.priority = 0
    self.column = 0
    self.best_node = None
    self.level = 0
    self.nodes = []

lst = [] #create empty list
#create empty board
for i in range(7):
  lst.append([]) #add 7 seven empty lists to lst
main_board = Board(lst)#creates a board out of lst
main_board.print_board()#prints board

class Computer:
  def __init__(self, token, opponent, board):
    self.token = token
    self.opponent = opponent
    self.node = Node(board)
    self.best_level = 0

  #build tree
  def build_tree(self, node, level):
    if node.nodes == []: #no nodes
      for column in range(7):
        new_node = Node(node.board.board)
        new_node.column = column
        new_node.level = level #current level
        if level % 2 == 0: #level is player's turn
          if new_node.board.place_token(self.opponent, column): #places token- returns True
            new_node.priority = new_node.board.check(self.opponent, self.token,column)*-1 #check for a computer win or block
            if new_node.priority != 0: #block or win
              if self.best_level == 0 or self.best_level > level:
                self.best_level = level # lowest level
            node.nodes.append(new_node) #adds node to list
        else:#computer's turn
          if new_node.board.place_token(self.token, column): #places token- returns True
            new_node.priority = new_node.board.check(self.token, self.opponent,column) #check for a computer win
            if new_node.priority != 0:  #checks if block or win
              if self.best_level == 0 or self.best_level > level:
                self.best_level = level # lowest level  
            node.nodes.append(new_node) #adds node to list
    if (self.best_level == 0 or level < self.best_level) and level < 7:
      for n in node.nodes: #loops through level
        if n.priority == 0:# only if not block or win
          self.build_tree(n, level + 1) #creates new level

#search tree
  def best_move(self, node):
    if node.level == 0: # first node
      temp = None # best node in level
      for n in node.nodes:
        if (temp == None and n.priority == -1) or (n.priority == 1): #sets temp to best node in level
          temp = n
        if temp != None:
          return temp
    if node.nodes == []: #bottom of tree
      if node.level <= self.best_level: #level you are at is smaller than best level
        if node.priority != 0: #win or block
          return node # best node
        return None # if level doesn't have best node
    else:
      for n in node.nodes: 
        temp = self.best_move(n)#reset temp to best node on level below
        if (temp != None and node.best_node == None) or (temp != None and temp.level <= node.best_node.level): #if temp is a node and there is a best node checks if temp level is less than best_node level- win or block in less moves
          node.best_node = temp
      return node.best_node    
      
  def make_move(self):
    self.best_level = 0
    self.node = Node(main_board.board)
    self.build_tree(self.node, 1)
    bestNode = self.best_move(self.node)#best node=best move(-1,0,1)
    #check if priority of bestNode is -1 or 1
    if bestNode != None: #if there's a best spot
      main_board.place_token(self.token, bestNode.column)#place Computer token at best spot
      return bestNode.column #returns column of best node
    else:# if there isn't a best spot
      col = random.randint(0, 6)
      main_board.place_token(self.token, col)
      return col

player = "*"
computer = Computer("#", player, main_board)

while True: #forever loop
  col = int(input("What column would you like? (1-7)"))- 1
  if main_board.place_token(player, col) == True:
    main_board.print_board()
    win = main_board.check(player, computer.token, col)
    if win == 1:
      print("Player wins!")
      break
    elif main_board.tie() == True:
      print("It's a tie!")
      break
  else: #no token placed
    continue #goes back to top of loop
  col = computer.make_move()#computer.make_move is the random number returned
  main_board.print_board()
  win = main_board.check(computer.token, player, col )
  if win == 1:
    print("Computer Wins")    
    break
  elif main_board.tie() == True:
      print("It's a tie!")
      break
    
