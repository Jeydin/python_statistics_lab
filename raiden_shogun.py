from data_functions import *
import os

aList = readInts("numbers.txt")

print("====== readInts ======")
print(readInts("numbers.txt"))
print()

print("====== sumValues ======")
print("Sum:", sumValues(aList))
print()

print("====== calcMean ======")
print("Average:", calcMean(aList))
print()

print("====== stdDev ======")
print("Standard Deviation:", stdDev(aList))
print()

print("====== selectionSort ======")
print(selection_sort(aList))
print()

print("====== findMedian ======")
print("Median:", findMedian(aList))
print()

print("====== findMode ======")
print("Mode:", findMode(aList))
print()

print(os.environ["YAE_MIKO"])
print(os.environ["YOUSIF"])