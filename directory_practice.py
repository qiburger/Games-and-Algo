__author__ = 'QHe'


'''Print all files locations under a directory - walk a directory'''

import os

def walk(directory_name):
    for root, dirs, files in os.walk(directory_name):
         for filename in files:
            print os.path.join(root, filename)


