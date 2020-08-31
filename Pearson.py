import numpy
import pandas
import csv


df = pandas.read_csv("/Users/tammob/Desktop/toy-example.csv")

h  = df["Height"]
hmin = min(h)
hmax = max(h)
w= df["Weight"]
n = len(h)

for i in range(n):
    h[i] = ((h[i] - hmin)/(hmax - hmin)) * (100 - 0)+ 0 #MinMax Normalisierung auf Werte zwischen 0 - 100

heightStd = numpy.std(h) #Standartwert festlegen
weightStd = numpy.std(w)

heightMean = numpy.mean(h) #Mittellwert festlegen
weightMean = numpy.mean(w)



sum = 0
for i in range(n):
    sum += (h[i] * w[i]) # ∑(xi * yi)

correl = (sum - (n * heightMean * weightMean)) / (n * heightStd * weightStd) 

print("Die Korrelation ist:")
print(correl)


