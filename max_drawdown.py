__author__ = 'Qi_He'

import random

class MaxDrawDown:

    value_list = []
    max_value = 0.0
    max_draw_down = 0.0

    def __init__(self, list_input):
        self.value_list = list_input
        self.max_value = list_input[0]

    def dp_max_draw_down(self):
        for i in self.value_list:
            self.max_value = max(self.max_value, i)
            self.max_draw_down = max(self.max_draw_down, abs(i - self.max_value))
        return self.max_draw_down

def random_list():
    out = []
    for i in range(20):
        out.append(random.randint(1, 100))
    return out

if __name__ == '__main__':
    input_list = random_list()
    print input_list
    tester = MaxDrawDown(input_list)
    print tester.dp_max_draw_down()
