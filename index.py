#!/usr/bin/python

import getopt, sys

def convertJsonToArrays(currentValue):
    # replace objects with arrays, and save them to a file

def loopArguments():
    argumentList = sys.argv[1:]
    # options help convert learn and show
    options = "hcls"
    long_options = ["help", "convert", "learn", "show"]
    arguments, values = getopt.getopt(argumentList, options)
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--help"):
            print("Usage:\n -h --help\n -c --convert\n -l --learn\n -s --show\n\nThis application is an AI which can give you weather forecasts based on the given input file.")
        elif currentArgument in ("-c", "--convert"):
            convertJsonToArrays(currentValue)
        elif currentArgument in ("-l", "--learn"):
            learnConvertedArrays()
        elif currentArgument in ("-s", "--show"):
            showForecast()

if __name__ == "__main__":
    loopArguments()




# import json
# import numpy as np

# f = open('data.json')

# data = json.load(f)

# print(data[0])

# for i 