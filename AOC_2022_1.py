import math
import os
import sys
import numpy as np

FILENAME = "input.txt"

def delElf(fElf):
    cal = []
    for _ in range(3):
        n = fElf.index(np.max(fElf))
        cal.append(np.max(fElf))
        fElf.pop(n)
    return np.sum(cal)

def readInput(FILENAME):
    Elf, fElf = 0,[]
    with open(FILENAME) as f:
        for line in f:
            if not line == "\n": 
                Elf += int(line)
            else:
                fElf.append(int(Elf))
                Elf = 0        
        fElf.append(int(Elf))
        return fElf

def main():
    Elf = readInput(FILENAME)
    print(f'Elf number {Elf.index(np.max(Elf))+1} has the most calories of {np.max(Elf)} ') #Question 1
    cal = delElf(Elf)
    print(f'Top three Elves have a total calories of {cal} ') #Question 2
    
    print('done')
    
if __name__ == '__main__':
    main()

