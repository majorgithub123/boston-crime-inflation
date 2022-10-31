import pandas
import matplotlib.pyplot as plt
import statistics

df = pandas.read_csv('crime.csv')

columnlist = sorted(list(df["OCCURRED_ON_DATE"]))
print(columnlist)

# hold values for each date, eg numbers of crime
numCrimesperDate = {}
for i in columnlist:
    try:
        numCrimesperDate[str(i)[:-9]] += 1
    except KeyError:
        numCrimesperDate[str(i)[:-9]] = 1

# makes a dictionary to hold data
dfDict = {}
dfDict['date'] = numCrimesperDate.keys()
dfDict['numCrimes'] = [numCrimesperDate[i] for i in numCrimesperDate.keys()]
dataframe = pandas.DataFrame(dfDict)


dataframe["date"]=dataframe["date"].astype("datetime64")
dataframe = dataframe.set_index(dataframe["date"])

# plots the graph
plt.plot(dataframe["numCrimes"], marker="o")
plt.title("Boston Crime in 2018")
plt.xlabel("Date")
plt.ylabel("Number of Crimes")
plt.show()

numcrimeslist = list(dataframe["numCrimes"])
# calculates the mean
print("The mean is ", round(statistics.mean(numcrimeslist)))

# calculates the mode
print("The mode is ", statistics.mode(numcrimeslist))

# calculates the median
print("The median is ", statistics.median(numcrimeslist))
