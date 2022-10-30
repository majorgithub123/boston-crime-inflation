import pandas
import matplotlib.pyplot as plt
import statistics

df = pandas.read_csv('data.csv')
print(df)
df["date"]=df["date"].astype("datetime64")
df = df.set_index(df["date"])

# plots the graph
plt.plot(df["rate"], marker="o")
plt.title("US Inflation Rate in 2018")
plt.xlabel("Date")
plt.ylabel("Rate")
plt.show()

rate = [2.1, 2.2, 2.4, 2.5, 2.8, 2.9, 2.9, 2.7, 2.3, 2.5, 2.2, 1.9]
# calculates the mean
print("The mean is ", round((statistics.mean(rate))))

# calculates the mode
print("The mode is ", statistics.mode(rate))

# calculates the median
print("The median is ", statistics.median(rate))

