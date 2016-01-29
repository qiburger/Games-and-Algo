__author__ = 'Qi_He'

''' Given a log beginning at a, ending at n
    Cuts can only be made at each int in a given list
    Every time a cut is made, score += len(log)
    And two new logs are made.
    The problem repeats until there is no cut to be made.
'''

global a
a = dict()
print a

def cutting(start, end, score):
    score += end - start

def cut_log(list, start, end, cut):
    start_index = list.index(start)
    end_index = list.index(end)
    cut_index = list.index(cut)
    new_log_1 = list[start:cut]
    cut_log(new_log_1,)
    new_log_2 = list[cut:end]


def decide_cut():
    print ""


