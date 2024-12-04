# KING QUEEN BISHOP KNIGHT ROOK PAWN



'''
def curr_pos(dict1,str1):
    curr_row=None
    crr_col=None
    for i in range(1,9):
        list3=dict1[i]
        list_currpos=[]
        for j in range(0,8):
            if(list3[j]==str1):
              list_currpos.extend([i,j])
              break
            else:
              continue
        break
    return list_currpos
'''

                
def rook_move(dict1,str1,row,column,player1,player2,list_currpos,player1_element,player2_element):
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=1)):
              if(r==row and c==column):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c-1] in player2_element)):
                  break
              else:
                  r-=1
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=8)):
              if(r==row and c==column):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c-1] in player2_element)):
                  break
              else:
                  r+=1
        r=list_currpos[0]
        c=list_currpos[1]
        while(c<=8):
              if(r==row and c==column):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c-1] in player2_element)):
                  break
              else:
                  c+=1
        r=list_currpos[0]
        c=list_currpos[1]
        while(c>=1):
              if(r==row and c==column):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c-1] in player2_element)):
                  break
              else:
                  c-=1
        print("INVALID MOVE FOR ROOK")
        return False
        
    
def knight_move(dict1,str1,row,column,player1,player2,list_currpos,player1_element,player2_element):
        if(row==list_currpos[0]-2 and column==list_currpos[1]+1):
          return True
        elif(row==list_currpos[0]-2 and column==list_currpos[1]-1):
          return True
        elif(row==list_currpos[0]+2 and column==list_currpos[1]-1):
          return True
        elif(row==list_currpos[0]+2 and column==list_currpos[1]+1):
          return True
        elif(row==list_currpos[0]-1 and column==list_currpos[1]+2):
          return True
        elif(row==list_currpos[0]-1 and column==list_currpos[1]-2):
          return True
        elif(row==list_currpos[0]+1 and column==list_currpos[1]+2):
          return True
        elif(row==list_currpos[0]+1 and column==list_currpos[1]-2):
          return True
        else:
          return False
          print("INVALID MOVE FOR KNIGHT")

def bishop_move(dict1,str1,row,column,player1,player2,list_currpos,player1_element,player2_element):
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=1 and r<=8) and (c>=1 and c<=8)):
              if(r==row and c==column):
                  return True
              elif(dict1[r][c-1] in player1_element) or (dict1[r][c] in player2_element)():
                  break
              else:
                  r+=1
                  c+=1
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=1 and r<=8) and (c>=1 and c<=8)):
              if(r==row and c==column):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c] in player2_element)):
                  break
              else:
                  r-=1
                  c+=1
                   
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=1 and r<=8) and (c>=1 and c<=8)):
              if(r==row and c==column):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c] in player2_element)):
                  break
              else:
                  r-=1
                  c-=1
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=1 and r<=8) and (c>=1 and c<=8)):
              if(r==row and c==column):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c] in player2_element)):
                  break
              else:
                  r+=1
                  c-=1
        print("INVALID MOVE FOR BISHOP")
        return False
         
    
def queen_move(dict1,str1,row,column,player1,player2,list_currpos,player1_element,player2_element):
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=1)):
              if(r==row and c==column):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c] in player2_element)):
                  break
              else:
                  r-=1
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=8)):
              if(r==row and c==column):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c] in player2_element)):
                  break
              else:
                  r+=1
        r=list_currpos[0]
        c=list_currpos[1]
        while(c<=8):
              if(r==row and c==column):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c] in player2_element)):
                  break
              else:
                  c+=1
        r=list_currpos[0]
        c=list_currpos[1]
        while(c>=1):
              if(r==row and c==column):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c] in player2_element)):
                  break
              else:
                  c-=1
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=1 and r<=8) and (c>=0 and c<8)):
              if(r==row and c==column):
                  return True
              elif(dict1[r][c-1] in player1_element) or (dict1[r][c] in player2_element)():
                  break
              else:
                  r+=1
                  c+=1
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=1 and r<=8) and (c>=0 and c<8)):
              if(r==row and c==column):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c] in player2_element)):
                  break
              else:
                  r-=1
                  c+=1
                   
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=1 and r<=8) and (c>=0 and c<8)):
              if(r==row and c==column):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c] in player2_element)):
                  break
              else:
                  r-=1
                  c-=1
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=1 and r<=8) and (c>=0 and c<8)):
              if(r==row and c==column):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c] in player2_element)):
                  break
              else:
                  r+=1
                  c-=1
        print("INVALID MOVE FOR QUEEN")
        return False

        
     

def pawn_move(dict1,str1,row,column,player1,player2,list_currpos,player1_element,player2_element):
    if(str1=="P1"):
        if(list_currpos[0]==2):
            if((row==list_currpos[0]+1 or row==list_currpos[1]+2) and (column==list_currpos[1])):
                return True
            elif((row==list_currpos[0]+1) and (column==list_currpos[1]+1) and (dict1[row][column-1]!="_")):
                return True
            elif((row==list_currpos[0]+1) and (column==list_currpos[1]-1) and (dict1[row][column-1]!="_")):
                return True
            else:
                return False
        else:
            if((row==list_currpos[0]+1 and column==list_currpos[1])):
                return True
            elif((row==list_currpos[0]+1) and (column==list_currpos[1]+1) and (dict1[row][column-1]!="_")):
                return True
            elif((row==list_currpos[0]+1) and (column==list_currpos[1]-1) and (dict1[row][column-1]!="_")):
                return True
            else:
                return False
    elif(str1=="P2"):
        if(list_currpos[0]==7):
            if((row==list_currpos[0]-1 or row==list_currpos[1]-2) and (column==list_currpos[1])):
                return True
            elif((row==list_currpos[0]-1) and column==list_currpos[1]+1 and dict1[row][column-1]!="_"):
                return True
            elif((row==list_currpos[0]-1) and column==list_currpos[1]-1 and dict1[row][column-1]!="_"):
                return True
            else:
                return False
        else:
            if((row==list_currpos[0]-1) and column==list_currpos[1]):
                return True
            elif((row==list_currpos[0]-1) and column==list_currpos[1]+1 and dict1[row][column-1]!="_"):
                return True
            elif((row==list_currpos[0]-1) and column==list_currpos[1]-1 and dict1[row][column-1]!="_"):
                return True
            return False
    else:
        return False
        print("INVALID MOVE FOR PAWN")

def king_move(dict1,str1,row,column,player1,player2,list_currpos,player1_element,player2_element):
    if(row==list_currpos[0]+1 and column==list_currpos[1]):
        return True
    elif(row==list_currpos[0]-1 and column==list_currpos[1]):
        return True
    elif(row==list_currpos[0] and column==list_currpos[1]-1):
        return True
    elif(row==list_currpos[0] and column==list_currpos[1]+1 ):
        return True
    elif(row==list_currpos[0]-1 and column==list_currpos[1]-1):
        return True
    elif(row==list_currpos[0]-1 and column==list_currpos[1]+1):
        return True
    elif(row==list_currpos[0]+1 and column==list_currpos[1]+1):
        return True
    elif(row==list_currpos[0]+1 and column==list_currpos[1]-1):
        return True
    else:
        print("INVALID MOVE FOR KING")
        return false
    


def check_king(dict1,str1,row,column,player1,player2,list_currpos,player1_element,player2_element):
  if((str1=="R1" or str1=="R2")):
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=1)):
              if((dict1[r][c-1]==player2_element[2])):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c-1] in player2_element)):
                  break
              else:
                  r-=1
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=8)):
              if((dict1[r][c-1]==player2_element[2])):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c-1] in player2_element)):
                  break
              else:
                  r+=1
        r=list_currpos[0]
        c=list_currpos[1]
        while(c<=8):
              if((dict1[r][c-1]==player2_element[2])):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c-1] in player2_element)):
                  break
              else:
                  c+=1
        r=list_currpos[0]
        c=list_currpos[1]
        while(c>=1):
              if((dict1[r][c-1]==player2_element[2])):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c-1] in player2_element)):
                  break
              else:
                  c-=1
        return False
  elif((str1=="k1" or str1=="k2")):
        r=list_currpos[0]
        c=list_currpos[1]
        if((dict1[r-2][c+1-1]==player2_element[2])):
          return True
        elif((dict1[r-1][c+2-1]==player2_element[2])):
          return True
        elif((dict1[r+1][c+2-1]==player2_element[2])):
          return True
        elif((dict1[r+2][c+1-1]==player2_element[2])):
          return True
        elif((dict1[r+1][c-2-1]==player2_element[2])):
          return True
        elif((dict1[r+2][c-1-1]==player2_element[2])):
          return True
        elif((dict1[r-2][c-1-1]==player2_element[2])):
          return True
        elif((dict1[r-1][c-2-1]==player2_element[2])):
          return True
        else:
          return False
  elif((str1=="B1" or str1=="B2")):
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=1 and r<=8) and (c>=0 and c<8)):
              if(dict1[r][c-1]==player2_element[2]):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c-1] in player2_element)):
                  break
              else:
                  r+=1
                  c+=1
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=1 and r<=8) and (c>=0 and c<8)):
              if((dict1[r][c-1]==player2_element[2])):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c-1] in player2_element)):
                  break
              else:
                  r-=1
                  c+=1
                   
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=1 and r<=8) and (c>=0 and c<8)):
              if((dict1[r][c-1]==player2_element[2])):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c-1] in player2_element)):
                  break
              else:
                  r-=1
                  c-=1
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=1 and r<=8) and (c>=0 and c<8)):
              if((dict1[r][c-1]==player2_element[2])):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c-1] in player2_element)):
                  break
              else:
                  r+=1
                  c-=1
        return False
  elif((str1=="Q1" or str1=="Q2")):
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=1 and r<=8) and (c>=0 and c<8)):
              if(dict1[r][c-1]==player2_element[2]):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c-1] in player2_element)):
                  break
              else:
                  r+=1
                  c+=1
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=1 and r<=8) and (c>=0 and c<8)):
              if((dict1[r][c-1]==player2_element[2])):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c-1] in player2_element)):
                  break
              else:
                  r-=1
                  c+=1
                   
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=1 and r<=8) and (c>=0 and c<8)):
              if((dict1[r][c-1]==player2_element[2])):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c-1] in player2_element)):
                  break
              else:
                  r-=1
                  c-=1
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=1 and r<=8) and (c>=0 and c<8)):
              if((dict1[r][c-1]==player2_element[2])):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c-1] in player2_element)):
                  break
              else:
                  r+=1
                  c-=1
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=1)):
              if((dict1[r][c-1]==player2_element[2])):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c-1] in player2_element)):
                  break
              else:
                  r-=1
        r=list_currpos[0]
        c=list_currpos[1]
        while((r>=8)):
              if((dict1[r][c-1]==player2_element[2])):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c-1] in player2_element)):
                  break
              else:
                  r+=1
        r=list_currpos[0]
        c=list_currpos[1]
        while(c<=8):
              if((dict1[r][c-1]==player2_element[2])):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c-1] in player2_element)):
                  break
              else:
                  c+=1
        r=list_currpos[0]
        c=list_currpos[1]
        while(c>=1):
              if((dict1[r][c-1]==player2_element[2])):
                  return True
              elif((dict1[r][c-1] in player1_element) or (dict1[r][c-1] in player2_element)):
                  break
              else:
                  c-=1
        
        return False
        
        
  elif((str1=="K1" or str1=="K2")):
        r=list_currpos[0]
        c=list_currpos[1]
        if((dict1[r-1][c-1]==player2_element[2])):
          return True
        elif((dict1[r+1][c-1]==player2_element[2])):
          return True
        elif((dict1[r][c-1-1]==player2_element[2])):
          return True
        elif((dict1[r][c+1-1]==player2_element[2])):
          return True
        elif((dict1[r-1][c-1-1]==player2_element[2])):
          return True
        elif((dict1[r-1][c+1-1]==player2_element[2])):
          return True
        elif((dict1[r+1][c-1-1]==player2_element[2])):
          return True
        elif((dict1[r+1][c+1-1]==player2_element[2])):
          return True
        else:
          return False
  elif((str1=="P1" or str1=="P2")):
     r=list_currpos[0]
     c=list_currpos[1]
     if(dict1[r+1][c-1-1]==player2_element[2]):
             return True
     if(dict1[r+1][c+1-1]==player2_element[2]):
             return True
     else:
             return False
  else:
          return False
    
                
    
        
    


def valid_move(dict1,str1,row,column,player1,player2,list_currpos,player1_element,player2_element):
     if((str1=="R1" or str1=="R2")and dict1[row][column-1] not in player1_element):
        return rook_move(dict1,str1,row,column,player1,player2,list_currpos,player1_element,player2_element)
     elif((str1=="k1" or str1=="k2") and dict1[row][column-1] not in player1_element):
        return knight_move(dict1,str1,row,column,player1,player2,list_currpos,player1_element,player2_element)
     elif((str1=="B1" or str1=="B2")and dict1[row][column-1] not in player1_element):
        return bishop_move(dict1,str1,row,column,player1,player2,list_currpos,player1_element,player2_element)
     elif((str1=="Q1" or str1=="Q2")and dict1[row][column-1] not in player1_element):
        return queen_move(dict1,str1,row,column,player1,player2,list_currpos,player1_element,player2_element)
     elif((str1=="K1" or str1=="K2")and dict1[row][column-1] not in player1_element):
        return king_move(dict1,str1,row,column,player1,player2,list_currpos,player1_element,player2_element)
     elif((str1=="P1" or str1=="P2")and dict1[row][column-1] not in player1_element):
        return pawn_move(dict1,str1,row,column,player1,player2,list_currpos,player1_element,player2_element)
     else:
         return False
    
def chessboard(dict1,str1,row,column,player1,player2,list_currpos,player1_element,player2_element):
     if((row<=8 and row>=1) and (column>=1 and column<=8) and str1 in player1_element):
        if(valid_move(dict1,str1,row,column,player1,player2,list_currpos,player1_element,player2_element)==True):
          if(dict1[row][column-1]=="K1" or dict1[row][column-1]=="K2"): 
            dict1[list_currpos[0]][list_currpos[1]-1]="_"
            dict1[row][column-1]=str1
            print("PLAYER",player1,"WINS THE GAME!!!")
          else:
            dict1[list_currpos[0]][list_currpos[1]-1]="_"
            dict1[row][column-1]=str1
            board(dict1)
            if((check_king(dict1,str1,row,column,player1,player2,[row,column],player1_element,player2_element)==True)):
               print(print("ALERT FOR CHECK"))
               print("PLAYER",player2,"CHANCE!!")
               str1=input("Enter the string")
               curr_row=int(input("Enter the current row"))
               curr_column=int(input("Enter the current column"))
               row=int(input("Enter the Row"))
               column=int(input("Enter the Column "))
               list_currpos=[curr_row,curr_column]
               chessboard(dict1,str1,row,column,player2,player1,list_currpos,player2_element,player1_element)
               return
            else:
               print("PLAYER",player2,"CHANCE!!")
               str1=input("Enter the string")
               curr_row=int(input("Enter the current row"))
               curr_column=int(input("Enter the current column"))
               row=int(input("Enter the Row"))
               column=int(input("Enter the Column "))
               list_currpos=[curr_row,curr_column]
               chessboard(dict1,str1,row,column,player2,player1,list_currpos,player2_element,player1_element)
               return
                
        else:
          print("INVALID MOVE")
          board(dict1)
          print("Enter the move again")
          str1=input("Enter the String Again")
          curr_row=int(input("Enter the current row"))
          curr_column=int(input("Enter the current column"))
          row=int(input("Enter the Row Again"))
          column=int(input("Enter the Column Again"))
          list_currpos=[curr_row,curr_column]
          chessboard(dict1,str1,row,column,player1,player2,list_currpos,player1_element,player2_element)
          return
     else:
          print("ROW AND COLUMN ENTERED OUT OF BOARD RANGE OR STRING ENTERED IS WRONG!!")
          board(dict1)
          print("Enter the move again")
          str1=input("Enter the String Again")
          curr_row=int(input("Enter the current row"))
          curr_column=int(input("Enter the current column"))
          row=int(input("Enter the Row Again"))
          column=int(input("Enter the Column Again"))
          list_currpos=[curr_row,curr_column]
          chessboard(dict1,str1,row,column,player1,player2,list_currpos,player1_element,player2_element)
          return
        
        
        
def initial_board(dict1):
    for i in range(1,9):
        list2=[]
        for j in range(1,9):
            if((i==1) and (j==1 or j==8)):
                list2.append("R1")
            elif((i==1) and (j==2 or j==7)):
                 list2.append("k1")
            elif((i==1) and (j==3 or j==6)):
                 list2.append("B1")
            elif((i==1) and (j==4)):
                 list2.append("Q1")
            elif((i==1) and (j==5)):
                 list2.append("K1")
            elif((i==2)):
                 list2.append("P1")
            elif((i==8) and (j==1 or j==8)):
                list2.append("R2")
            elif((i==8) and (j==2 or j==7)):
                 list2.append("k2")
            elif((i==8) and (j==3 or j==6)):
                 list2.append("B2")
            elif((i==8) and (j==4)):
                 list2.append("Q2")
            elif((i==8) and (j==5)):
                 list2.append("K2")
            elif((i==7)):
                 list2.append("P2")
            else:
                 list2.append("_")
        dict1[i]=list2
    return

def board(dict1):
    for i in range(1,9):
        list1=dict1[i]
        for j in list1:
            if(j!='_'):
              print(j,end=" ")
            else:
              print(j,end="  ")
        print()
    print()
    return
        
            
            
            
           
    
n=8
dict1={}
player1=input("Enter the Player 1")
player2=input("Enter the Player 2")
initial_board(dict1)
board(dict1)
str1=input("Enter the String")
curr_row=int(input("Enter the current row"))
curr_column=int(input("Enter the current column"))
row=int(input("Enter the row"))
column=int(input("Enter the column"))
list_currpos=[curr_row,curr_column]
player1_element=["P1","B1","K1","k1","Q1","R1"]
player2_element=["P2","B2","K2","k2","Q2","R2"]
chessboard(dict1,str1,row,column,player1,player2,list_currpos,player1_element,player2_element)

