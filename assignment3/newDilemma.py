import json
import argparse
import array
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
parser = argparse.ArgumentParser()
parser.add_argument('--init', help='called when new game')
parser.add_argument('--iterations', help='number of iterations in game')
parser.add_argument('--last_opponent_move', help='last opponent move')
args = parser.parse_args()

outfile = open('dictData.json', 'r+')

data = json.load(outfile)

if args.init == "true":
    data["queue"] = ["Confess", "Silence", "Silence", "Confess"]  
    data["iterations"] =  0
    data["final"] = args.iterations
elif(args.last_opponent_move == "zero"): #First round
    data["iterations"] =  1
    print(data["queue"][0]) 
else: #Every round besides first
    data = json.load(myfile)
    if(data["iterations"]==data["final"]):#Final round
        print("Confess")
    else:#Normal Round  
        print(data["queue"].pop(0))
        data["queue"].append(args.last_opponent_move)
        data["iterations"]+=1 
with open("dictData.json", "r+") as f:
    json.dump(data, f)

