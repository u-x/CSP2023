####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'r', 'p', 's', 'l', or 'k'
####

team_name = 'Alternator'
strategy_name = 'Alternator'
strategy_description = 'Alternates between 2 choices.'

iteration = 0
    
def move(my_history, their_history, my_score, their_score):
    global iteration
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
    '''
    '''Make my move based on the history with this player.
    
    history: a string with one letter (r, p, s, l, or k) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns a 'r', 'p', 's', 'l', or 'k' for Rock, Paper, Scissors, Lizard, Spock
    '''
    
    # This player will always choose spock.
    iteration += 1
    if len(my_history) == 0:
      iteration = 0
    if iteration > 2:
      iteration = 0
    
    if iteration == 0:
      return "s"
    elif iteration == 1:
      return "k"
    else:
      return "p"
    
    