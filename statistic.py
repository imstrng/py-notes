import statistics


data = list(range(11))
data = [1023,104,17,2]
print(data)
print('mean:    ',statistics.mean(data))     # Average
print('stdev:   ',statistics.stdev(data))    # Average distance from the mean
print('variance:',statistics.variance(data)) # Average distance from the mean Squared
print('median  :',statistics.median(data))   # Median
print('median L:',statistics.median_low(data))
print('median H:',statistics.median_high(data))