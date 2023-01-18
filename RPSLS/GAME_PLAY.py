from __future__ import print_function
import imp


#### 
# Computer Science and Software Engineering
# PLTW AP CS Principles
# (c)2014 Project Lead The Way, Inc.
#
# Activity 1.3.9 Tools for Collaboration
# Project 1.3.10 Collaborating on a Project
# 
# To run a tournament, execute this file. 
# Place each team's strategy in a file in the same directory as this file.
# Tournament results saved to tournament.txt in this directory.
#
# Rock_Paper_Scissors_Lizard_Spock.py automates competition among different strategies
# for the game, the canonical game of game-theory.
# Each strategy is pitted against each other strategy for 100 rounds.
# The results of all previous rounds within a 100 round stretch are known
# to both players. 
#
# play_tournament([team0, team1, team2]) executes a tournament and writes to tournament.txt
#
# Each team's strategy should be coded in their assigned Python file, called a module.
# Each player should have their own .py file containing 
# three strings team_name, strategy_name, and strategy_description
# and a function move(my_history, their_history, my_score, their_score)
# 
# By default, when executing this file, [example0, example1, example2, example3] 
# play a tournament. To run the tournament of [team_0, team_1, team_2, example1]:
# scores, moves, reports = main_play([team_1]*3+[example1])
# section0, section1, section2, section3 = reports
#######

import random
import os.path              
import BOT_1, BOT_2, BOT_3, BOT_4, BOT_5, BOT_6, BORRELLI


game_number = 7     #number plus one default is running only the rock, paper, scissors, lizard, and spock scenerios
rounds_min = 100    #if you want random number of battles you need to uncomment out: lines 89,92,111
rounds_max = 200
         #[player00,player01,player02,player03,player04,player05,player06,player07,player08,player09
modules = [BOT_1, BOT_2, BOT_3, BOT_4, BOT_5, BOT_6, BORRELLI]

for module in modules:
    imp.reload(module)
    print ('reloaded',module)
    for required_variable in ['team_name', 'strategy_name', 'strategy_description']:
        if not hasattr(module, required_variable):
            setattr(module, required_variable, 'missing assignment')

def main_play(modules):
    '''main_play plays a tournament and outputs results to screen and file.
    This function is called once when this file is executed.
    modules: a list of modules such as [team1, team2]    
    
    Returns:
        scores:
        moves:
        sections: a list of [str, str, str, list of str]    
            '''
    scores, moves = play_tournament(modules)
    section0, section1, section2, section3 = make_reports(modules, scores, moves)
    code = make_code_string(modules)
    # On screen, include the first three out of four sections of the report.
    print(section0+section1+section2)
    # To file output, store all teams' code and all teams' section 3 reports.
    post_to_file(section0+section1+section2 + code + ''.join(section3))
    return scores, moves, [section0, section1, section2, section3]
        
def play_tournament(modules):
    '''Each argument is a module name
    Each module must contain 
        team_name: a string
        strategy_name: a string
        strategy_description: a string
        move: A function that returns 'c' or 'b'
    '''
    zeros_list = [0]*len(modules) # to initialize each player's head-to-head scores
    scores = [zeros_list[:] for module in modules] # Copy it or it's only 1 list
    moves = [zeros_list[:] for module in modules] # Copy it or it's only 1 list
    for first_team_index in range(len(modules)):
        for second_team_index in range(first_team_index):
            player1 = modules[first_team_index]
            player2 = modules[second_team_index]
            score1, score2, moves1, moves2 = play_iterative_rounds(player1, player2)
            capitalize(moves1, moves2)
            scores[first_team_index][second_team_index] = score1#/len(moves1) # int division not an issue
            moves[first_team_index][second_team_index] = moves1
            # Redundant, but record this for the other player, from their perspective
            scores[second_team_index][first_team_index] = score2#/len(moves2) 
            moves[second_team_index][first_team_index] = moves2
        # Playing yourself doesn't do anything
        scores[first_team_index][first_team_index] = 0
        moves[first_team_index][first_team_index] = ''
    return scores, moves


def play_iterative_rounds(player1, player2):
    global rounds_min
    global rounds_max
    
    '''
    Plays a random number of rounds (between 100 and 200 rounds) 
    of the game between two strategies.
    player1 and player2 are modules.
    Returns 4-tuple, for example ('cc', 'bb', -200, 600) 
    but with much longer strings 
    '''
    number_of_rounds = rounds_min #random.randint(rounds_min, rounds_max)  #put this instead of rounds_min
    moves1 = ''
    moves2 = ''
    score1 = 0
    score2 = 0
    for round in range(number_of_rounds):
        score1, score2, moves1, moves2 = play_round(player1, player2, score1, score2, moves1, moves2)
    return (score1, score2, moves1, moves2)
    
def play_round(player1, player2, score1, score2, moves1, moves2):
    '''
    Calls the move() function from each module which return
    output for each player.
    The history is provided in a string, e.g. 'ccb' indicates the player
    colluded in the first two rounds and betrayed in the most recent round.
    Returns a 2-tuple with score1 and score2 incremented by this round
    '''
    global WIN
    global LOSE
    global TIE
    global ERROR
    
    WIN = 100 
    LOSE = -100 
    TIE = 0 
    ERROR = -500
    
    # Get the two players' actions and remember them.
    action1 = player1.move(moves1, moves2, score1, score2)
    #print(action1)
    action2 = player2.move(moves2, moves1, score2, score1)
    #print(action2)
    #if error
    if (type(action1) != str) or (len(action1) != 1):
        action1=' '
    if (type(action2) != str) or (len(action2) != 1):
        action2=' '
         
    # Change scores based upon player actions.
    actions = action1 + action2
    #print(actions)
    #print(type(actions))
    
####
# Rock vs
####    
    #Rock vs Rock
    if actions == 'rr':
        score1 += TIE
        score2 += TIE
    #Rock vs Paper
    elif actions == 'rp':
        score1 += LOSE
        score2 += WIN    
    #Rock vs Scissors
    elif actions == 'rs':
        score1 += WIN
        score2 += LOSE    
    #Rock vs Lizard
    elif actions == 'rl':
        score1 += WIN
        score2 += LOSE    
    #Rock vs Spock
    elif actions == 'rk':
        score1 += LOSE
        score2 += WIN 
####
# Paper vs
####    
    #Paper vs Rock
    elif actions == 'pr':
        score1 += WIN
        score2 += LOSE
    #Paper vs Paper
    elif actions == 'pp':
        score1 += TIE
        score2 += TIE    
    #Paper vs Scissors
    elif actions == 'ps':
        score1 += LOSE
        score2 += WIN   
    #Paper vs Lizard
    elif actions == 'pl':
        score1 += LOSE
        score2 += WIN    
    #Paper vs Spock
    elif actions == 'pk':
        score1 += WIN
        score2 += LOSE             
####
# Scissors vs
####    
    #Scissors vs Rock
    elif actions == 'sr':
        score1 += LOSE
        score2 += WIN
    #Scissors vs Paper
    elif actions == 'sp':
        score1 += WIN
        score2 += LOSE    
    #Scissors vs Scissors
    elif actions == 'ss':
        score1 += TIE
        score2 += TIE   
    #Scissors vs Lizard
    elif actions == 'sl':
        score1 += WIN
        score2 += LOSE    
    #Scissors vs Spock
    elif actions == 'sk':
        score1 += LOSE
        score2 += WIN   
####
# Lizard vs
####    
    #Lizard vs Rock
    elif actions == 'lr':
        score1 += LOSE
        score2 += WIN
    #Lizard vs Paper
    elif actions == 'lp':
        score1 += WIN
        score2 += LOSE    
    #Lizard vs Scissors
    elif actions == 'ls':
        score1 += LOSE
        score2 += WIN   
    #Lizard vs Lizard
    elif actions == 'll':
        score1 += TIE
        score2 += TIE    
    #Lizard vs Spock
    elif actions == 'lk':
        score1 += WIN
        score2 += LOSE    
####
# Spock vs
####    
    #Spock vs Rock
    elif actions == 'kr':
        score1 += WIN
        score2 += LOSE
    #Spock vs Paper
    elif actions == 'kp':
        score1 += LOSE
        score2 += WIN    
    #Spock vs Scissors
    elif actions == 'ks':
        score1 += WIN
        score2 += LOSE   
    #Spock vs Lizard
    elif actions == 'kl':
        score1 += LOSE
        score2 += WIN   
    #Spock vs Spock
    elif actions == 'kk':
        score1 += TIE
        score2 += TIE   
####
# Error vs
#### 
    else:
        # Both players get the "error score" if someone's code returns an improper action.
        print ('In Error')
        score1 += ERROR
        score2 += ERROR
    
    # Append the actions to the previous histories.
    if action1 in 'rpslk':
        moves1 += action1
    else:
        moves1 += ' '
    
    if action2 in 'rpslk':
        moves2 += action2
    else:
        moves2 += ' '
    
    print(score1,score2)               
    # Return scores incremented by this round's results.
    return (score1, score2, moves1, moves2)  
      
          
def make_reports(modules, scores, moves):
    section0 = make_section0(modules, scores)
    section1 = make_section1(modules, scores)
    section2 = make_section2(modules, scores)
    
    section3 = []
    for index in range(len(modules)):
        section3.append(make_section3(modules, moves, scores, index))
    return section0, section1, section2, section3

#################################
# Sections in the Python Window #
#################################      
                        
def make_section0(modules, scores):
    '''
    Produce the following string:
    ----------------------------------------------------------------------------
    Section 0 - Line up
    ----------------------------------------------------------------------------
    Player 0 (P0): Team name 0, Strategy name 0,
         Strategy 0 description
    Player 1 (P1): Team name 1, Strategy name 1, 
         Strategy 1 description
    ''' 
    section0 = '-'*80+'\n'
    section0 += 'Section 0 - Line up\n'
    section0 += '-'*80+'\n'
    for index in range(len(modules)):
        section0 += 'Player ' + str(index) + ' (P' + str(index) + '): '
        section0 += str(modules[index].team_name) + ', ' + str(modules[index].strategy_name) + '\n'
        strategy_description = str(modules[index].strategy_description)
        # Format with 8 space indent 80 char wide
        while len(strategy_description) > 1:
            newline = strategy_description[:72].find('\n')
            if newline> -1:
                section0 += ' '*8 + strategy_description[:newline+1]
                strategy_description = strategy_description[newline+1:]
            else:
                section0 += ' '*8 + strategy_description[:72] + '\n'
                strategy_description = strategy_description[72:]
    return section0
    
def make_section1(modules, scores):
    '''
    --------------------------------------------------------------------------------
    Section 1 - Player vs. Player
    --------------------------------------------------------------------------------
    Each column shows pts/round earned against each other player:
                P0     P1     P2     P3     P4
    vs. P0 :      0  10000 -10000 -10000  10000
    vs. P1 : -10000      0  10000  10000 -10000
    vs. P2 :  10000 -10000      0 -10000  10000
    vs. P3 :  10000 -10000  10000      0 -10000
    vs. P4 : -10000  10000 -10000  10000      0
    TOTAL  :      0      0      0      0      0
    '''
    # First line
    section1 = '-'*80+'\nSection 1 - Player vs. Player\n'+'-'*80+'\n'
    section1 += 'Each column shows pts/round earned against each other player:\n'
    # Second line
    section1 += '        '
    for i in range(len(modules)):
          section1 += '{:>7}'.format('P'+str(i))
    section1 += '\n'
    # Add one line per team
    for index in range(len(modules)):
        section1 += 'vs. P' + str(index) + ' :'
        for i in range(len(modules)):
            section1 += '{:>7}'.format(scores[i][index])
        section1 += '\n'

    # Last line
    section1 += 'TOTAL  :'
    for index in range(len(modules)):
        section1 += '{:>7}'.format(sum(scores[index]))     
    return section1+'\n'
    
def make_section2(modules, scores):
    '''
    --------------------------------------------------------------------------------
    Section 2 - Leaderboard
    --------------------------------------------------------------------------------
    Average points per round:
    Team name (P#):  Score      with strategy name
    Rock      (P0):          0 points with Rock                                    
    Paper     (P1):          0 points with Paper                                   
    Scissors  (P2):          0 points with Scissors                                
    Lizard    (P3):          0 points with Lizard                                  
    Spock     (P4):          0 points with Spock 
    ''' 
    section2 = '-'*80+'\nSection 2 - Leaderboard\n'+'-'*80+'\n'
    section2 += 'Average points per round:\n'
    section2 += 'Team name (P#):  Score      with strategy name\n'
    
    # Make a list of teams' 4-tuples
    section2_list = []
    for index in range(len(modules)):
        section2_list.append((modules[index].team_name,
                              'P'+str(index),
                              str(sum(scores[index])),
                              str(modules[index].strategy_name)))
    section2_list.sort(key=lambda x: int(x[2]), reverse=True)
    
    # Generate one string per team
    for team in section2_list:
        team_name, Pn, n_points, strategy_name = team
        section2 += '{:<10}({}): {:>10} points with {:<40}\n'.format(team_name[:10], Pn, n_points, strategy_name[:40])                       
    return section2 
    
def make_section3(modules, moves, scores, index):
    '''Return a string with information for the player at index, like:
    Section 3 - Game Data for Team Rock
    --------------------------------------------------------------------------------
    -10000 pt/round: Rock(P0) "Rock"
    10000 pt/round: Paper(P1) "Paper"
    rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
    pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
    
    rrrrrrrrrrrrrrrrrrrr
    pppppppppppppppppppp
    
    --------------------------------------------------------------------------------
    '''
    section3 = '-'*80+'\nSection 3 - Game Data for Team '
    section3 += modules[index].team_name + '\n'
    section3 += '-'*80+'\n'
    # Make 4 lines per opponent
    for opponent_index in range(len(modules)):
        if opponent_index != index:
            # Line 1
            section3 += str(scores[index][opponent_index])
            section3 += ' pt/round: ' + modules[index].team_name +'(P'
            section3 += str(index)+') "'+modules[index].strategy_name + '"\n'
            # Line 2
            section3 += str(scores[opponent_index][index])
            section3 += ' pt/round: ' + modules[opponent_index].team_name +'(P'
            section3 += str(opponent_index)+') "'+modules[opponent_index].strategy_name + '"\n'
            # Lines 3-4
            hist1, hist2 =  capitalize(moves[index][opponent_index], moves[opponent_index][index])
            while len(hist1) > 1:
                section3 += hist1[:80] + '\n'
                section3 += hist2[:80] + '\n\n'
                hist1 = hist1[80:]
                hist2 = hist2[80:]
            section3 += '-'*80 + '\n'
    return section3

############################
# Fixing Students mistakes #
############################                                                   
                                                                                                                                                     
def capitalize(history1, history2):
    '''Accept two strings of equal length.
    Return the same two strings but capitalizing the opponent of 'c' each round.
    '''
    caphistory1, caphistory2 = '', ''
    for i in range(len(history1)):
        p1 = history1[i]
        p2 = history2[i]
        if p1 == 'c':
            p2 = p2.upper()
        if p2 in 'cC':
            p1 = p1.upper()
        caphistory1 += p1    
        caphistory2 += p2  
    return caphistory1, caphistory2
    


def make_code_string(modules):
    '''Returns a string of the code from each file.
    '''
    code = '-'*80 + '\n'
    code += 'Code of each player\'s algorithm\n'
    code = '-'*80 + '\n'
    for index in range(len(modules)):
        players_code_filename = str(modules[index]).split(' ')[1].replace('\'','')
        directory = os.path.dirname(os.path.abspath(__file__))  
        filename = os.path.join(directory, players_code_filename)
        players_code_file = open(filename+'.py', 'r')
        code += '-'*80 + '\n'
        code += players_code_filename
        code +='-'*80 + '\n'
        code += ''.join(players_code_file.readlines())
    return code

def copy_template():
    '''Transfer code in team0.py to team1.py though team14.py
    '''
    directory = os.path.dirname(os.path.abspath(__file__))  
    with open(os.path.join(directory, 'team0.py'), 'r') as sourcefile:
        source = sourcefile.readlines()
    for i in range(1, 15):
        target = 'team'+str(i)+'.py'
        filename = os.path.join(directory, target)
        with open(filename, 'w') as target_file:
            target_file.write(''.join(source))                                   
                     
def post_to_api():
    pass

def post_to_local_html():
    pass
    
def post_to_file(string, filename='tournament.txt', directory=''):
    '''Write output in a txt file.
    '''
    # Use the same directory as the python script
    if directory=='':
        directory = os.path.dirname(os.path.abspath(__file__))  
    # Name the file tournament.txt
    filename = os.path.join(directory, filename)
    # Create the file for the round-by-round results
    filehandle = open(filename,'w')
    filehandle.write(string)
 
### Call main_play() if this file is executed
if __name__ == '__main__':
    scores, moves, reports = main_play(modules[0:game_number])   
    section0, section1, section2, section3 = reports