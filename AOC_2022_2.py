
import numpy as np

FILENAME = "input2.txt"
RPS = {
        "rock": 1,
        "paper": 2,
        "scissors": 3
    }
LDW = {
        "lose": 0,
        "draw": 3,
        "win": 6
    }
    
def checkWeight(my_choice):
    if my_choice == "X":
        weight = RPS["rock"]
        score = LDW["lose"]
    elif my_choice == "Y":
        weight = RPS["paper"]
        score = LDW["draw"]
    elif my_choice == "Z":
        weight = RPS["scissors"]
        score = LDW["win"]
        
    return weight, score

def checkScore(op_choice, my_choice):
    if (op_choice == "A" and my_choice == "X") or \
        (op_choice == "B" and my_choice == "Y") or \
        (op_choice == "C" and my_choice == "Z"):
        score = LDW["draw"]
    elif (op_choice == "A" and my_choice == "Z") or \
        (op_choice == "B" and my_choice == "X") or \
        (op_choice == "C" and my_choice == "Y"):
        score = LDW["lose"]
    elif (op_choice == "A" and my_choice == "Y") or \
        (op_choice == "B" and my_choice == "Z") or \
        (op_choice == "C" and my_choice == "X"):
        score = LDW["win"]
        
    return score

def expectedScore(op_choice, expected_result):
    if (op_choice == "A" and expected_result == "Y") or \
        (op_choice == "B" and expected_result == "X") or \
        (op_choice == "C" and expected_result == "Z"):
        weight = RPS["rock"]
    elif (op_choice == "A" and expected_result == "Z") or \
        (op_choice == "B" and expected_result == "Y") or \
        (op_choice == "C" and expected_result == "X"):
        weight = RPS["paper"]
    elif (op_choice == "A" and expected_result == "X") or \
        (op_choice == "B" and expected_result == "Z") or \
        (op_choice == "C" and expected_result == "Y"):
        weight = RPS["scissors"]
        
    return weight

def rockPaperScissors(FILENAME):
    total, t = [], []
    with open(FILENAME) as f:
        for line in f:
            weight, s = checkWeight(line[2])
            w = expectedScore(line[0], line[2])
            score = checkScore(line[0], line[2])
            total.append(weight+score)
            t.append(w+s)
            
    return np.sum(total), np.sum(t)

def main():
    t_score, t_s = rockPaperScissors(FILENAME)
    print(f'The total score if everything goes exactly according to the strategy guide is {t_score}') #Question 1
    print(f'The total score if everything goes exactly according to the 2nd rule is {t_s}') #Question 2
    
    print('done')
    
if __name__ == '__main__':
    main()

