from datetime import datetime
start_time = datetime.now()

#Help
#Function to get the name of the player as registered in the team
def getPlayer(player):
	for person in all_players:
		if player in person:
			return person

def scorecard():
	#dictionary which contains the information for the scoreboard 
	innings1 = {'runs': 0, 'wickets': 0, 'balls': 0, 'batting': {player : {'runs': 0, 'balls': 0, '4s': 0, '6s': 0, 'status': ''} for player in pak_players}, 'bowling': {player : {'runs': 0, 'balls': 0, 'maidens': 0, 'wickets': 0, 'nb': 0, 'wide': 0} for player in ind_players}, 'extras': {'byes': 0, 'nb': 0, 'lb': 0, 'wide': 0, 'pty': 0}, 'dnb': pak_players.copy(), 'fow': [], 'powerplay': 0}
	innings2 = {'runs': 0, 'wickets': 0, 'balls': 0, 'batting': {player : {'runs': 0, 'balls': 0, '4s': 0, '6s': 0, 'status': ''} for player in ind_players}, 'bowling': {player : {'runs': 0, 'balls': 0, 'maidens': 0, 'wickets': 0, 'nb': 0, 'wide': 0} for player in pak_players}, 'extras': {'byes': 0, 'nb': 0, 'lb': 0, 'wide': 0, 'pty': 0}, 'dnb': ind_players.copy(), 'fow': [], 'powerplay': 0}
	#initial is a variable to store the initial run the bowler gave just before delivering the over. It is used for finding the maiden over
	initial=-1
	#Reading the innings text file of india and pakistan and craeting an output text file for displaying the scoreboard
	with open('pak_inns1.txt', 'r') as pak_inns, open('india_inns2.txt', 'r') as ind_inns, open('output.txt','w') as output:
		#Reading all the lines in the textfiles
		tot_lines1 = pak_inns.readlines()
		tot_lines2 = ind_inns.readlines()
		#Count is variable to just know who is batting
		count=0
		print("", file=output)
		#This outer for loop, has 2 loops which loops through both the country's innings
		for innings, lines in zip([innings1, innings2], [tot_lines1, tot_lines2]):
			#This loop, loops through the lines of the comment section for getting the information	
			for info in [line for line in lines if line.strip()]:
				#extracting the names of the batsmen and bowler, result and the over using the information in line
				batter = getPlayer(info.split(",")[0].split(" ", 1)[1].split("to")[1].strip())
				bowler = getPlayer(info.split(",")[0].split(" ", 1)[1].split("to")[0].strip())
				outcome = info.split(",")[1].strip()
				over=info.split(",")[0].split(" ", 1)[0].strip()
				# here when a bowler starts his over, his runs initially is stored in a variable, it is used for finding maiden over
				if innings['bowling'][bowler]['balls']%6==0:
					initial=innings['bowling'][bowler]['runs']
				# if 6 over is over, then runs for the powerplay is updated
				if(innings['balls']==36):
					innings['powerplay'] = innings['runs']
				# if a new player enters the field, that player is removed from the did not bat list
				if batter in innings['dnb']:
					innings['dnb'].remove(batter)
				# updated scoreboard for different kind of balls and runs
				if outcome == "no run":
					innings['balls']+=1
					innings['batting'][batter]['balls']+=1
					innings['batting'][batter]['status']="not out"
					innings['bowling'][bowler]['balls']+=1
				if outcome == "no ball":
					innings['runs']+=1
					innings['bowling'][bowler]['nb']+=1
					innings['bowling'][bowler]['runs']+=1
					innings['batting'][batter]['status']="not out"
					innings['extras']['nb'] += 1
				elif outcome == "wide":
					innings['runs']+=1
					innings['extras']['wide'] += 1
					innings['batting'][batter]['status']="not out"
					innings['bowling'][bowler]['runs'] += 1
					innings['bowling'][bowler]['wide'] += 1
				elif outcome == '2 wides':
					innings['runs'] += 2
					innings['extras']['wide'] += 2
					innings['bowling'][bowler]['runs'] += 2
					innings['batting'][batter]['status']="not out"
					innings['bowling'][bowler]['wide'] += 2
				elif outcome == '3 wides':
					innings['runs'] += 3
					innings['extras']['wide'] += 3
					innings['bowling'][bowler]['runs'] += 3
					innings['batting'][batter]['status']="not out"
					innings['bowling'][bowler]['wide'] += 3
				elif outcome == '4 wides':
					innings['runs'] += 4
					innings['extras']['wide'] += 4
					innings['bowling'][bowler]['runs'] += 4
					innings['batting'][batter]['status']="not out"
					innings['bowling'][bowler]['wide'] += 4
				elif outcome == '5 wides':
					innings['runs'] += 5
					innings['extras']['wide'] += 5
					innings['bowling'][bowler]['runs'] += 5
					innings['batting'][batter]['status']="not out"
					innings['bowling'][bowler]['wide'] += 5
				elif outcome == "1 run":
					innings['balls'] += 1
					innings['runs'] += 1
					innings['batting'][batter]['runs'] += 1
					innings['batting'][batter]['balls'] += 1
					innings['batting'][batter]['status']="not out"
					innings['bowling'][bowler]['runs'] += 1
					innings['bowling'][bowler]['balls'] += 1
				elif outcome == "2 runs":
					innings['balls'] += 1
					innings['runs'] += 2
					innings['batting'][batter]['runs'] += 2
					innings['batting'][batter]['balls'] += 1
					innings['batting'][batter]['status']="not out"
					innings['bowling'][bowler]['runs'] += 2
					innings['bowling'][bowler]['balls'] += 1
				elif outcome == "3 runs":
					innings['balls'] += 1
					innings['runs'] += 3
					innings['batting'][batter]['runs'] += 3
					innings['batting'][batter]['balls'] += 1
					innings['batting'][batter]['status']="not out"
					innings['bowling'][bowler]['runs'] += 3
					innings['bowling'][bowler]['balls'] += 1
				elif outcome == "FOUR":
					innings['balls'] += 1
					innings['runs'] += 4
					innings['batting'][batter]['runs'] += 4
					innings['batting'][batter]['balls'] += 1
					innings['batting'][batter]['status']="not out"
					innings['bowling'][bowler]['runs'] += 4
					innings['bowling'][bowler]['balls'] += 1
					innings['batting'][batter]['4s'] += 1
				elif outcome == "SIX":
					innings['balls'] += 1
					innings['runs'] += 6
					innings['batting'][batter]['runs'] += 6
					innings['batting'][batter]['balls'] += 1
					innings['batting'][batter]['status']="not out"
					innings['bowling'][bowler]['runs'] += 6
					innings['bowling'][bowler]['balls'] += 1
					innings['batting'][batter]['6s'] += 1
				elif outcome.split(" ")[0].strip() == "out":
					innings['balls'] += 1
					innings['wickets'] += 1	
					innings['batting'][batter]['balls'] += 1
					innings['bowling'][bowler]['wickets'] += 1
					innings['bowling'][bowler]['balls'] += 1
					innings['fow'].append(f"{innings['runs']}-{innings['wickets']} {batter}, {over}")
					if outcome.startswith('out Caught by'):
						innings['batting'][batter]['status'] = f"c {outcome.split('!!')[0].split('out Caught by', 1)[1].strip()} b {bowler}"
					elif outcome.startswith('out Bowled!!'):
						innings['batting'][batter]['status'] = f"b {bowler}"
					elif outcome.startswith('out Lbw!!'):
						innings['batting'][batter]['status'] = f"lbw b {bowler}"
				elif outcome == "byes" or outcome == "leg byes":
					innings['balls'] += 1
					innings['batting'][batter]['balls'] += 1
					innings['batting'][batter]['status']="not out"
					innings['bowling'][bowler]['balls'] += 1
					runs = info.split(",")[2].strip()
					if(runs == 'no run'):
						continue
					elif(runs == '1 run'):
						innings['runs'] += 1
						if outcome == "byes":
							innings['extras']['byes'] += 1
						else:
							innings['extras']['lb'] += 1
					elif(runs == '2 runs'):
						innings['runs'] += 2
						if outcome == "byes":
							innings['extras']['byes'] += 2
						else:
							innings['extras']['lb'] += 2
					elif(runs == '3 runs'):
						innings['runs'] += 3
						if outcome == "byes":
							innings['extras']['byes'] += 3
						else:
							innings['extras']['lb'] += 3
					elif(runs == 'FOUR'):
						innings['runs'] += 4
						if outcome == "byes":
							innings['extras']['byes'] += 4
						else:
							innings['extras']['lb'] += 4
				# Here the if condition checks if the runs given to the batsman by the bowler by the end of the over
				# is equal to runs at the starting of the over, if it is equal, then it is a maiden for that bowler
				if innings['bowling'][bowler]['balls']%6==0:
					if innings['bowling'][bowler]['runs']==initial:
						innings['bowling'][bowler]['maidens']+=1
			# From here onwards is the code to display the scoreboard
			if count==0:
				print(f"{'Pakistan Innings' : <50}{f'''{innings['runs']}-{innings['wickets']} ({over} Ov)''' : >90}", file=output)
				count+=1
			else:
				print(f"{'Indian Innings' : <50}{f'''{innings['runs']}-{innings['wickets']} ({over} Ov)''' : >90}", file=output)
			print("", file=output)
			# Display the details of all the batters
			print(f"{'': <25}{'Batter' : <25}{'' : <50}{'R' : >8}{'B' : >8}{'4s' : >8}{'6s' : >8}{'SR' : >12}", file=output)
			for batsman, data in innings['batting'].items():
				if data['status'] != '':
					print(f"{'': <25}{batsman : <25}{data['status'] : <50}{data['runs'] : >8}{data['balls'] : >8}{data['4s'] : >8}{data['6s'] : >8}{round((data['runs']/data['balls'])*100, 2) : >12}", file=output)
			print("", file=output)
			print(f"{'': <25}{'Extras' : <50}{innings['extras']['wide'] : >44}", file=output)
			print(f"{'': <25}{'Total' : <50}{f'''{innings['runs']} ({innings['wickets']} wkts, {over} Ov)''' : >44}", file=output)
			# Display the names of the batters who did not bat
			if innings['dnb']:
				print(f"{'': <25}{'Did not Bat' : <50}{', '.join(innings['dnb']) : >44}", file=output)
			print("", file=output)
			# Display the details of all the fall of wickets
			print(f"{'' :<25}""Fall of Wickets", file=output)
			wickets = ", ".join(innings['fow'])
			print(f"{'' :<25}{wickets : ^100}{'' :>25}", file=output)
			print("", file=output)
			# Display the details of all the bowlers
			print(f"{'': <25}{'Bowler' : <25}{'' : <50}{'O' : >7}{'M' : >10}{'R' : >8}{'W' : >8}{'NB' : >8}{'WD' : >8}{'ECO' : >12}", file=output)
			for bowler, data in innings['bowling'].items():
				if data['balls']:
					total_overs=data['balls']//6
					extra_balls=data['balls']%6
					overall_overs=str(total_overs)+'.'+str(extra_balls)
					print(f"{'': <25}{bowler : <25}{'' : <50}{overall_overs : >9}{data['maidens'] : >8}{data['runs'] : >8}{data['wickets'] : >8}{data['nb'] : >8}{data['wide'] : >8}{round(data['runs']/(total_overs+(extra_balls/6)),1) : >12}", file=output)
			print("", file=output)
			# Display the runs taken in powerplay
			print(f"{'': <25}{'Powerplays' : <15}{'Overs' : >15}{'Runs' : >15}", file=output)
			print(f"{'': <25}{'Mandatory' : <15}{'0.1-6' : >15}{innings['powerplay']: >15}", file=output)
			print("", file=output)



###Code

from platform import python_version
ver = python_version()

if ver == "3.8.10":
	print("Correct Version Installed")
else:
	print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

ind_players = ['Rohit Sharma (c)', 'KL Rahul', 'Virat Kohli', 'Suryakumar Yadav', 'Dinesh Karthik (w)', 'Hardik Pandya', 'Ravindra Jadeja', 'Bhuvneshwar Kumar', 'Avesh Khan', 'Yuzvendra Chahal', 'Arshdeep Singh']
pak_players = ['Babar Azam (c)', 'Mohammad Rizwan (w)', 'Fakhar Zaman', 'Iftikhar Ahmed', 'Khushdil Shah', 'Asif Ali', 'Shadab Khan', 'Mohammad Nawaz', 'Naseem Shah', 'Haris Rauf', 'Shahnawaz Dahani']
all_players = ind_players + pak_players
scorecard()

#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))