import numpy as np 

# FG = wind speed, TG = temperature, PG = pressure 
def importOutData():
    data = np.loadtxt('tmp/out.json', delimiter=',')
    return data

def learn():
    data = importOutData()