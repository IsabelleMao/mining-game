#Complete or add to the nonexistent code under any comment, or add a new comment!


#Enter the game
while True:
  enter = input("""Type start to begin the game!
  """)
  enter = enter.strip().lower()
  if enter == "start":
    break
    
while True:
  #Get the name of the user.
  
while True:
  #Tutorial
  
  #Let the player view his/her/its info
  
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
  
  #Buy a mine
  
  #Buy (hire) a builder
  
  #Exit the game

  
