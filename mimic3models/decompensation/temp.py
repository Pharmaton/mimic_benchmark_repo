import os
import numpy as np
import random

with open(os.path.join(r'D:\Dokumente\JKU\Masterarbeit\benchmark\mimic3-benchmarks-master\data\decompensation\train',r'1791_episode1_timeseries.csv'), "r") as tsfile:
    ret=[]
    header = tsfile.readline().strip().split(',')
    assert header[0] == "Hours"
    for line in tsfile:
        mas = line.strip().split(',')
        if np.in1d('NEG',mas):
            if mas[8] != 'NEG':
                print('no')
        t = float(mas[0])
        ret.append(np.array(mas))
    try:
       np.stack(ret)
    except ValueError:
        for i in range(0, len(ret)):
            #print(np.shape(ret[i]))
            if np.shape(ret[i]) != (18,):
                print(ret[i])
                print(np.shape(ret[i]))

        s = np.stack





