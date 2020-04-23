import random

oneToTen = random.randrange(1,11) #generates random number between 1-10 inclusive
oneToTwenty = random.randrange(1,21) #generates number between 1-20 inclusive
oneToFifty = random.randrange(1,51)#generates number between 1-50 inclusive
g= list() #empty array to keep track of number of trials 

def easy(g,one2ten):
      if len(g)==6: #checks if all six chances have been exhausted
        print("Game Over!")
        print ("the number is: "+str(one2ten))
        print ("Refresh to play again")
      else: 
        chances = str(6-len(g)) #determines number of chances left
        print ("you have "+chances+" chance(s) left")
        print ("My number is between 1-10 inclusive, enter your guess below: ")
      try: #checks for wrong input in the block of code below
        x = input();
        g.append(x) #adds to the array to keep track of number of trials
        if int(x)==one2ten:
          print("You got it right!")
          print ("Refresh to play again")
        else:
          print("That was wrong!")
          print()
          easy(g,one2ten)
      except:
        print("Wrong input!")
        print()
        print("The input must be an integer, please try again")
        easy(g,one2ten)
def medium(g,one2twenty):
      if len(g)==4:
        print("Game Over!")
        print ("the number is: "+str(one2twenty))
        print ("Refresh to play again")
      else: 
        chances = str(4-len(g))//
        print ("you have "+chances+" chance(s) left")
        print ("My number is between 1-20 inclusive, enter your guess below: ")
      try:
        x = input();
        g.append(x)
        if int(x)==one2twenty:
          print("You got it right!")
          print ("Refresh to play again")
        else:
          print("That was wrong!")
          print()
          medium(g,one2twenty)
      except:
        print("Wrong input!")
        print()
        print("The input must be an integer, please try again")
        medium(g,one2twenty)
def hard(g,one2fifty):
      if len(g)==3:
        print("Game Over!")
        print ("the number is: "+str(one2fifty))
        print ("Refresh to play again")
      else: 
        chances = str(3-len(g))
        print ("you have "+chances+" chance(s) left")
        print ("My number is between 1-50 inclusive, enter your guess below: ")
      try:
        x = input();
        g.append(x)
        if int(x)==one2fifty:
          print("You got it right!")
          print ("Refresh to play again")
        else:
          print("That was wrong!")
          print()
          hard(g,one2fifty)
      except:
        print("Wrong input!")
        print()
        print("The input must be an integer, please try again")
        hard(g,one2fifty)

 #determines the level of difficult of game the user wants to play       
def chooseLevel():
        print("Hello! this is a number guessing game!")
        print ("Enter 1 for level one, 2 for level two or 3 for level three")
        level= str(input())
        if level=='1': 
                  print("Easy Level selected")
                  easy(g,oneToTen)
        elif level=='2':
                  print("Medium Level selected")
                  medium(g, oneToTwenty)
        elif level=='3':
                  print("Hard Level selected")
                  hard(g, oneToFifty)
        else:
          print ("wrong input!")
          print("try again")
          chooseLevel()

chooseLevel()#calls the chooselevel function to start the program
