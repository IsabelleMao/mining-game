#Complete or add to the nonexistent code under any comment, or add a new comment!


#Enter the game
while True:
  enter = input("""Type start to begin the game!
  """)
  enter = enter.strip().lower()
  if enter == "start":
    break
    
while True:
  #Gets the name of the user. If empty space is returned asks for a name
  username = input("""Choose and type a name for your journey!\n""")
  if username == "":
    print("""Please enter a name!""")
  else:
    print("Welcome ",username,"!")
    break

  
#while True:
  #Tutorial
    #It can be a simple print statement of strings which explains the game
  
  #Let the player view his/her/its info
    #we might try to create a Class for info(stats, exp, etc.) arrangements
    #information can be saved into another file. This file reads and writes info from that? 
  
  #Mine
  
  #Sell things?
    #how should we set piricing model?
    #dynamic: Prices drop if you sell a lot and rise if you don't sell for a while (supply&demand relation)
    #static: Prices are always the same. At first we might start with stable pricing than for next versions might consider dynamic pricing?
  
  #Buy a mine
  
  #Buy (hire) a builder

  #Enemies? Thiefs try to rob your mines? Monsters try to eat yo in mines?

  #Exit the game