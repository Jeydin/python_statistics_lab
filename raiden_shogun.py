from data_functions import *
import os

crimson_witch_of_flames = readInts("numbers.txt")

print("====== readInts ======")
print(readInts("numbers.txt"))
print()

print("====== sumValues ======")
print("Sum:", sumValues(crimson_witch_of_flames))
print()

print("====== calcMean ======")
print("Average:", calcMean(crimson_witch_of_flames))
print()

print("====== stdDev ======")
print("Standard Deviation:", stdDev(crimson_witch_of_flames))
print()

print("====== selectionSort ======")
print(selection_sort(crimson_witch_of_flames))
print()

print("====== findMedian ======")
print("Median:", findMedian(crimson_witch_of_flames))
print()

print("====== findMode ======")
print("Mode:", findMode(crimson_witch_of_flames))
print()

print(os.environ["YAE_MIKO"])
print(os.environ["YOUSIF"])