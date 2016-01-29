__author__ = 'Qi_He'

'''
    n people walked into a bar with their own clothing indexed from 1 to n
    on the way out, each person picks up a random piece of clothing
    Plot the distribution of the number of people who got their own clothing

'''

import random
import matplotlib.pyplot as plt


def random_sample(n):
    matching_dict = dict(zip(range(100), random.sample(range(100), 100)))
    return sum(1 for x in matching_dict if x == matching_dict[x])

def plot_simulation(n, times):
    simulation = [random_sample(n) for i in range(times)]
    plt.hist(simulation, bins=[0,1,2,3,4,5,6,7])
    plt.title("Matching Histogram")
    plt.xlabel("# of Matches")
    plt.ylabel("Frequency")
    plt.show()

if __name__ == '__main__':
    plot_simulation(100, 10000)
