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
  
  '''Mine generating resources. I THINK I figured this out. Got stuck in so many infinite loops (6) trying to work this out.
  Oh, needs to generate every x seconds. Don't know how to do that.
  Here the maximum gold the player can have is 500 and the goldMine (should) generates 100 gold every (x seconds) and adds it to gold?
  The "+100" should show above the goldMine indicating that it's generating/working.
  '''
  goldMine = 0
  gold = 0
  while gold < 500:
	gold += 100
	for goldMine in range(0, 500, 100):
		print(gold, "+100")
    
  #Sell things?
    #how should we set piricing model?
    #dynamic: Prices drop if you sell a lot and rise if you don't sell for a while (supply&demand relation)
    #static: Prices are always the same. At first we might start with stable pricing than for next versions might consider dynamic pricing?
  
  #Buy a mine
  
  #Buy (hire) a builder


  #Enemies? Thiefs try to rob your mines? Monsters try to eat yo in mines?

  #Exit the game. 
while True:
	enter = input("""Do you really wish to quit the game?""")
	if enter == "no":
		#return to game
        if enter == "yes":
		sys.exit
		
   
