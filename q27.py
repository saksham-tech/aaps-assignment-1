from collections import Counter

def maxFrequencyElement(nums):
    freq = Counter(nums)
    return max(freq, key=freq.get)
