#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from MySort import MySort

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()

    times = Sorter.DefaultSort(times)
    times_avg = Sorter.DefaultSort(times_avg)
    # try some other methods! see how long they take
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.QuickSort(times_avg)

    # ADD YOUR CODE TO PLOT times AND times_avg HERE

    quantile1 = np.quantile(times,0.20)
    quantile2 = np.quantile(times,0.50)
    quantile3 = np.quantile(times,0.80)

    avg_quantile1 = np.quantile(times_avg,0.20)
    avg_quantile2 = np.quantile(times_avg,0.50)
    avg_quantile3 = np.quantile(times_avg,0.80)

    #make Npass figure
    plt.figure()
    plt.hist(times,Nmeas+150,density=False,alpha=0.5)
    plt.xlabel('Times between missing cookies[days]')
    plt.ylabel('Probability')
    plt.title("rate of 2.00 cookies/day")
    plt.grid(True)
    plt.axvline(quantile1,label="20th Quantile",color="b")
    plt.axvline(quantile2,label="50th Quantile",color="g")
    plt.axvline(quantile3,label="80th Quantile",color="r")
    plt.legend()
    plt.show()


    plt.figure()
    plt.hist(times_avg,Nmeas+150,density=False,alpha=0.5,color='b')
    plt.xlabel('Average times between missing cookies[days]')
    plt.ylabel('Probability')
    plt.title("10 measurments/experiment with rate of 2.00 cookies/day")
    plt.grid(True)
    plt.axvline(avg_quantile1,label="20th Quantile",color="r")
    plt.axvline(avg_quantile2,label="50th Quantile",color="g")
    plt.axvline(avg_quantile3,label="80th Quantile",color="y")
    plt.legend()
    plt.show()
    
