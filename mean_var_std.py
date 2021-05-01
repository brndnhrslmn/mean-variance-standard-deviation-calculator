import numpy as np


def calculate(list):
    calculations = {}

    # check if list is less than 9 characters long
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    # reshape list to a 3 x 3 numpy array
    arr = np.array(list).reshape(3, 3)

    # mean
    mean1 = np.mean(arr, axis=0).tolist()
    mean2 = np.mean(arr, axis=1).tolist()
    meanf = np.mean(arr).tolist()
    calculations.update({'mean': [mean1, mean2, meanf]})

    # variance
    var1 = np.var(arr, axis=0).tolist()
    var2 = np.var(arr, axis=1).tolist()
    varf = np.var(arr)
    calculations.update({'variance': [var1, var2, varf]})

    # standard deviation
    std1 = np.std(arr, axis=0).tolist()
    std2 = np.std(arr, axis=1).tolist()
    stdf = np.std(arr)
    calculations.update({'standard deviation': [std1, std2, stdf]})

    # max
    max1 = np.max(arr, axis=0).tolist()
    max2 = np.max(arr, axis=1).tolist()
    maxf = np.max(arr)
    calculations.update({'max': [max1, max2, maxf]})

    # min
    min1 = np.min(arr, axis=0).tolist()
    min2 = np.min(arr, axis=1).tolist()
    minf = np.min(arr)
    calculations.update({'min': [min1, min2, minf]})

    # sum
    sum1 = np.sum(arr, axis=0).tolist()
    sum2 = np.sum(arr, axis=1).tolist()
    sumf = np.sum(arr)
    calculations.update({'sum': [sum1, sum2, sumf]})

    return calculations
