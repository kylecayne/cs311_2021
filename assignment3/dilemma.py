import json
import argparse
""""
Algorithm:
1)On first round enemy move is 0:
    set up dictionary called data that includes:
      queue of 4 silences ["Silence","Silence","Silence","Silence"]
      integer for iterations
    Start with 4 silences to play nice at first
    keep track of iterations to confess on final move
2)Every round after first round we are given enemies last move:
  First we must load our data each round
    We are going to use their decisions against them on a 4 play delay, if they play mean we will start to be mean, if they are nice we will be nice
      take their last move and append to the queue and pop off the top of the queue and print that as our decision
        we are also going to add 1 to our iterations on each round so we can return confess on final round
          after each round we are going to save the state of our data
3)when current iterations == given iterations:
    print confess and exit
      dont worry about saving data or iterating
"""

def save_state(data):
  """Saves data into a file"""
  with open('dictData.txt', 'w') as file:
    json.dump(data, file)
def load_state():
  """Loads data from a file"""
  with open('dictData.txt', 'r') as file:
    return json.load(file)  
if __name__ == "__main__":
#Setting up the parser and arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--init', help='called when new game')
    parser.add_argument('--iterations', help='number of iterations in game')
    parser.add_argument('--last_opponent_move', help='last opponent move')
    args = parser.parse_args()
    iterations = args.iterations #total amount of iterations given
    if(args.init != None):
        with open('dictData.txt', 'w') as fp:
            pass
    if(args.last_opponent_move == 0): #First round
      data = {}
      data["queue"] = ["Confess", "Silence", "Silence", "Confess"] 
      data["iterations"] =  1
      save_state(data)    
    else: #Every round besides first
      data = load_state()
      if(data["iterations"]==args.iterations):#Final round
        print("Confess")
        exit(0)
      else:#Normal Round  
        print(data["queue"].pop(0))
        data["queue"].append(args.last_opponent_move)
        data["iterations"]+=1 
        save_state(data)



