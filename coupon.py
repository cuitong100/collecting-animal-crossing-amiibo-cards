import random
import scipy.stats as st
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

n = 400 # number of distinct cards
list = [i for i in range(1,n+1)]
pack = 6 #number of cards in one package

X = 1000 #runtimes of Monte Carlo simulation

cost = [0]*X
for i in range(X):
    s = set(list)
    while True:
        cards = random.sample(range(1, n+1), pack)
        cost[i] += pack
        s = s - set(cards)
        if len(s) == 0:
            break
    if i % (100) == 0:
        print(str(i/X*100) + "'%' finished")
    
sum(cost)/X

from scipy.stats import kurtosis,skew,variation

np.std(cost)
np.mean(cost)
np.median(cost)
kurtosis(cost)
skew(cost)

def mean_confidence_interval(data, confidence=0.99):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

print(mean_confidence_interval(cost))
cost_sort = sorted(cost)
cost_sort[50]
cost_sort[1000-50]


from scipy.stats import gaussian_kde
 
density = gaussian_kde(cost)
x_vals = np.linspace(1000,5000) # Specifying the limits of our data
density.covariance_factor = lambda : .3 #Smoothing parameter
density._compute_covariance()
plt.plot(x_vals,density(x_vals))
plt.show()