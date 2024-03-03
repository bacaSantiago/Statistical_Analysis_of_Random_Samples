# Required Librerías
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


    # Exercise 1: Random sample of 20 values that is distributed in N(15,49)

# Generate sample of random values in a normal distribution with mean 0 and variance 1
M = 20 # Number of elements
mu = 15 # Mean 
u = np.random.randn(M)
    
# We transform our sample to mean 15 and variance 49
v = mu + 7*u
    
# Calculate mean and sample st deviation
vbar = np.mean(v)
vstd = np.std(v, ddof=1)



    # Exercise 2: 95% confidence interval
    
t = abs(stats.t.ppf(0.025,M-1)) # Find the X that satisfies cdf(x) = 0.025
print(t)



    # Exercise 3: 100 random samples of 20 values that are distributed in N(15,49)

# Generate 100 samples of random values in a normal distribution with mean 0 and variance 1
data = {"samples":[],"vbar":[], "vstd":[], "upper":[], "lower":[], "color":[]}
for i in range(100):
    u = np.random.randn(M) # 20 is the number of elements
    
    # We transform our sample to mean 15 and variance 49
    v = mu + 7*u
    data["samples"].append(list(v))
    
    # Calculate mean and sample st deviation
    data["vbar"].append(np.mean(v))
    data["vstd"].append(np.std(v, ddof=1))
    
    # Calculate the tails of each v bar with the value of t_α/2,M-1
    data["upper"].append((data["vbar"][i] + t * data["vstd"][i] / np.sqrt(M)))
    data["lower"].append((data["vbar"][i] - t * data["vstd"][i] / np.sqrt(M)))
    
    # Check if the confidence interval includes the true mean
    if data["lower"][i] <= mu <= data["upper"][i]:
        data["color"].append('dodgerblue')  # Assign blue color if the interval includes it
    else:
        data["color"].append('deeppink')  # Assign pink color if the interval does not include it
        
        
        
    # Exercise 4: Compare sample means against the real one

# Plot sample means with confidence intervals
plt.figure(figsize=(8, 10))
for i in range(100):
    plt.errorbar(data["vbar"][i], i, xerr=[data["vbar"][i] - data["lower"][i]], fmt='o', color=data["color"][i])
plt.axvline(x=15, color='darkorchid', linestyle='--')
plt.ylabel('Sample number', fontstyle='italic')
plt.xlabel('Sample Mean (x_bar)', fontstyle='italic')
plt.legend([plt.Line2D([0], [0], marker='o', color='dodgerblue', label=''),
            plt.Line2D([0], [0], marker='o', color='deeppink', label=''),
            plt.Line2D([0], [0], linestyle='--', color='darkorchid', label='')],
           ['Confidence interval includes µ', 'Confidence interval does not include µ', 'True Mean (µ = %d)'%mu], loc='upper right')
plt.title('Sample Means with 95% Confidence Intervals', fontweight="bold")
plt.grid(True)
plt.show()



    # Exercise 5: Compare sample means against the real one with different levels of confidence

# Function to generate 100 samples of random values in a normal distribution with mean 0 and variance 1
def generateSample(M,mu,t):
    data = {"samples":[],"vbar":[], "vstd":[], "upper":[], "lower":[], "color":[]}
    for i in range(100):
        u = np.random.randn(M) # 20 is the number of elements
        
        # We transform our sample to mean 15 and variance 49
        v = mu + 7*u
        data["samples"].append(list(v))
        
        # Calculate mean and sample st deviation
        data["vbar"].append(np.mean(v))
        data["vstd"].append(np.std(v, ddof=1))
        
        # Calculate the tails of each v bar with the value of t_α/2,M-1
        data["upper"].append((data["vbar"][i] + t * data["vstd"][i] / np.sqrt(M)))
        data["lower"].append((data["vbar"][i] - t * data["vstd"][i] / np.sqrt(M)))
        
        # Check if the confidence interval includes the true mean
        if data["lower"][i] <= mu <= data["upper"][i]:
            data["color"].append('dodgerblue')  # Assign blue color if the interval includes it
        else:
            data["color"].append('deeppink')  # Assign pink color if the interval does not include it
    return data

# Function to graph sample means with confidence intervals
def plotSample(data,mu,ic):
    plt.figure(figsize=(8, 10))
    for i in range(100):
        plt.errorbar(data["vbar"][i], i, xerr=[data["vbar"][i] - data["lower"][i]], fmt='o', color=data["color"][i])
    plt.axvline(x=15, color='darkorchid', linestyle='--')
    plt.ylabel('Sample number', fontstyle='italic')
    plt.xlabel('Sample Mean (x_bar)', fontstyle='italic')
    plt.legend([plt.Line2D([0], [0], marker='o', color='dodgerblue', label=''),
                plt.Line2D([0], [0], marker='o', color='deeppink', label=''),
                plt.Line2D([0], [0], linestyle='--', color='darkorchid', label='')],
            ['Confidence interval includes µ', 'Confidence interval does not include µ', 'True Mean (µ = %d)'%mu], loc='upper right')
    plt.title('Sample Means with %s Confidence Intervals'%ic, fontweight="bold")
    plt.grid(True)
    plt.show()

# Define the parameters   
M = 20
mu = 15
t99_7, t80 = abs(stats.t.ppf(0.0015,M-1)), abs(stats.t.ppf(0.1,M-1))

# Obtain the samples for confidence intervals at 99.7% and 80%
data99_7 = generateSample(M,mu,t99_7)
data80 = generateSample(M,mu,t80)

# Plot the samples
plotSample(data99_7,mu,"99.7%")
plotSample(data80,mu,"80%")