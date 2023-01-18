####
# Each team's file must define four tokens:
#     team_name: a string no more than 10 charactors long
#     strategy_name: a string no more than 10 charactors long
#     strategy_description: a string
#     move: A function that returns 'r', 'p', 's', 'l', or 'k'
####

import random

team_name = 'Borrelli'
strategy_name = 'The Thing'
strategy_description = 'Does The Thing.'
'''
                            O   P   P   O   N   E   N   T
    ||----------||----------||----------||----------||----------||----------||
    ||          || Rock     || Paper    || Scissors || Lizard   || spock    ||
    ||----------||----------||----------||----------||----------||----------||   
    || Rock     ||    0 pts || -100 pts ||  100 pts ||  100 pts || -100 pts ||
  Y ||----------||----------||----------||----------||----------||----------||
    || Paper    ||  100 pts ||    0 pts || -100 pts || -100 pts ||  100 pts ||                                                    
  O ||----------||----------||----------||----------||----------||----------||
    || Scissors || -100 pts ||  100 pts ||    0 pts ||  100 pts || -100 pts ||                                         
  U ||----------||----------||----------||----------||----------||----------|| 
    || Lizard   || -100 pts ||  100 pts || -100 pts ||    0 pts ||  100 pts ||                               
    ||----------||----------||----------||----------||----------||----------||
    || spock    ||  100 pts || -100 pts ||  100 pts || -100 pts ||    0 pts ||              
    ||----------||----------||----------||----------||----------||----------||
    Rock = 'r'
    Paper = 'p'
    Scissors = 's'
    Lizard = 'l'
    spock = 'k'      
    
    Make my move based on the history with this player.
    
    history: a string with one letter (r, p, s, l, or k) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns a 'r', 'p', 's', 'l', or 'k' for Rock, Paper, Scissors, Lizard, Spock
'''

pattern = False
realpattern = ''
patterndebounce = False
solutionstr = ''
iteration = 0

def rand_move():
  determiner = random.randint(0, 4)
  if determiner == 0:
    return "r"
  elif determiner == 1:
    return "p"
  elif determiner == 2:
    return "s"
  elif determiner == 3:
    return "l"
  elif determiner == 4:
    return "k"

def move(my_history, their_history, my_score, their_score):
    global pattern, realpattern, patterndebounce, solutionstr, iteration
    if pattern == False:
      print('nopattern')
      if len(their_history) == 0:
        patterndebounce = False
        pattern = False
        solutionstr = ''
        iteration = 0
        realpattern = ''
        randomplay = rand_move()
        return randomplay
      else:
        if len(their_history) >= 3:
          print("longer or equal 2 3")
          for i in "rpslk":
            if their_history[-1] == i and their_history[-2] == i and their_history[-3] == i:
              print("triple equality")
              patterndebounce = True
              if i == "r":
                return "p"
              elif i == "p":
                return "s"
              elif i == "s":
                return "k"
              elif i == "l":
                return "s"
              elif i == "k":
                return "p"
          print(patterndebounce)
          if patterndebounce == False:
            pattern = True
            print("we got a pattern chief")
            # make a random play if the pattern is true and let the other half of the code do the thinking
            randplay = rand_move()
            return randplay
        else:
          for i in "rpslk":
            if their_history[-1] == i:
              if i == "r":
                return "p"
              elif i == "p":
                return "s"
              elif i == "s":
                return "k"
              elif i == "l":
                return "s"
              elif i == "k":
                return "p"
    else:
      if solutionstr != '':
        print('solution isnt empty')
        print(realpattern)
        print(solutionstr)
        iteration += 1
        if iteration > len(solutionstr) - 1:
          iteration = 0
        print("their last was " + their_history[-1])
        print("im playing " + solutionstr[iteration])
        return solutionstr[iteration]
      elif their_history[-1] != their_history[-2]:
        if their_history[-1] == their_history[-3]:
          realpattern = their_history[-1] + their_history[-2]
          for i in realpattern:
            if i == "r":
              solutionstr += "p"
            elif i == "p":
              solutionstr += "s"
            elif i == "s":
              solutionstr += "k"
            elif i == "l":
              solutionstr += "s"
            elif i == "k":
              solutionstr += "p"
          print(solutionstr)
          return solutionstr[0]
        elif their_history[-1] != their_history[-3] and their_history[-2] != their_history[-3]:
          # im gonna take a crack at a triple
          print(their_history)
          realpattern = their_history[-1] + their_history[-3] + their_history[-2]
          print("THE ONE PATTERN IS REAL " + realpattern)
          for i in realpattern:
            if i == "r":
              solutionstr += "k"
            elif i == "p":
              solutionstr += "s"
            elif i == "s":
              solutionstr += "k"
            elif i == "l":
              solutionstr += "s"
            elif i == "k":
              solutionstr += "p"
          iteration = 1
          return solutionstr[iteration]
        else:
          nomoves = rand_move()
          return nomoves
        