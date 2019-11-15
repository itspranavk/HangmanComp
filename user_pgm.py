import sys
import fileinput
import re
import collections
import os
import subprocess

def get_input():
    input = sys.stdin.readlines()[0].split()
    if len(input) == 2:
        input.append(input[1])
        input[1] = ""
    return input

def print_char(to_send):
    print(to_send.lower())
    sys.exit()

def prob_char(r):
    prob = collections.defaultdict(float)
    with open('words.txt', 'r') as f:
        matches = []
        for l in f:
            matches.append(re.findall(r, l))
        matches = [x[0] for x in matches if x != []]
        for m in matches:
            for c in m:
                if c.isalpha():
                    prob[c] += 1
    t = float(sum(prob.values()))
    for k in prob.keys():
        prob[k] = prob[k]/t
    return prob
    
# You should write your code in this function. input is a list of 3 items. input[0] is
# the current state. This is in the form of a string in which each character is either
# a '_' character if the letter has not been guessed or the correct character. Example:
# if the word to be guessed is "apple" and you have previously guessed 'a' and 'l', then
# state will appear as "a__l_"
def user_code(input):
    s = input[0]
    g = input[1]
    n = input[2]
    r = re.compile("^" + s.replace("_", "."))
    prob = prob_char(r)
    for c in g:
        try:
            del prob[c]
        except:
            pass
    # subprocess.call(["rm", "cache.txt"])
    return sorted(prob.items(), reverse=True, key=lambda x: x[1])[0][0]

print_char(user_code(get_input()))
