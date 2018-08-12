
def redraw():
	print ("======================")
	print ("	"+loc[0]+"|"+loc[1]+"|"+loc[2]+"")
	print ("   -------------")
	print ("	"+loc[3]+"|"+loc[4]+"|"+loc[5]+"")
	print ("   -------------")
	print ("	"+loc[6]+"|"+loc[7]+"|"+loc[8]+"")
loc = ['1','2','3','4','5','6','7','8','9']

def check_win(loc):
	if ( (loc[0] =='X' and loc[1] =='X' and loc[2] =='X')
	  or (loc[3] =='X' and loc[4] =='X' and loc[5] =='X')
	  or (loc[6] =='X' and loc[7] =='X' and loc[8] =='X')
	  or (loc[0] =='X' and loc[3] =='X' and loc[6] =='X')
	  or (loc[1] =='X' and loc[4] =='X' and loc[7] =='X')
	  or (loc[2] =='X' and loc[5] =='X' and loc[8] =='X')
	  or (loc[0] =='X' and loc[4] =='X' and loc[8] =='X')
	  or (loc[2] =='X' and loc[4] =='X' and loc[6] =='X') ) :
		return 'Player_1'

	elif ( (loc[0] =='O' and loc[1] =='O' and loc[2] =='O')
	  or (loc[3] =='O' and loc[4] =='O' and loc[5] =='O')
	  or (loc[6] =='O' and loc[7] =='O' and loc[8] =='O')
	  or (loc[0] =='O' and loc[3] =='O' and loc[6] =='O')
	  or (loc[1] =='O' and loc[4] =='O' and loc[7] =='O')
	  or (loc[2] =='O' and loc[5] =='O' and loc[8] =='O')
	  or (loc[0] =='O' and loc[4] =='O' and loc[8] =='O')
	  or (loc[2] =='O' and loc[4] =='O' and loc[6] =='O') ) :
		return 'Player_2' 	
	else : 
		return 'None'	

def handel_choice(player, choice):
	if (not(choice > 9 or choice < 0  )):
		print ('Wrong Choice')

		if (player == 'player_1'):
			loc[choice] = 'X'
	   
		elif(player == 'player_2') :
	   		loc[choice] = 'O'	
		else :
			print ('Error')   				  						

redraw()

turn = 0 

while (turn < 9) :
	print ("Player 1  :")
	p1c = int(input('Make Choice please  : '))
	choice = p1c -1
	turn = turn+1
	print ("the turn now is "+str(turn))
	handel_choice('player_1', choice)
	redraw()

	if (check_win(loc) == 'Player_1') :
		print(' ---------- Playe 1 Won ----------')
		redraw()
		break
	elif(check_win(loc) == 'Player_2') :
		print(' ---------- Playe 2 Won ----------')
		redraw()
		break	

	if (turn == 9) :
		print('---------- Draw ----------')
		break


	print ("Player 2  :")
	p2c = int(input('Make Choice please  : '))
	choice = p2c -1
	turn = turn+1
	print ("the tuen now is "+str(turn))
	handel_choice('player_2', choice)
	redraw()

	check_win(loc)


