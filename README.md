# Statistical Analysis of Random Samples

## Overview

This Python program conducts a comprehensive statistical analysis of random samples drawn from a normal distribution. It explores fundamental concepts such as generating random samples, calculating confidence intervals, and comparing sample means with the true mean. Utilizing the power of NumPy, Matplotlib, and SciPy, the program provides visual insights into the variability and reliability of sample statistics.

## Required Libraries
- **NumPy:** Utilized for numerical operations and array manipulations.
- **Matplotlib:** Employed for graphical representation of data.
- **SciPy (scipy.stats):** Utilized for statistical calculations.

## Exercise 1: Random Sample from Normal Distribution

A random sample of 20 values is generated from a normal distribution with a mean (\( \mu \)) of 15 and a variance (\( \sigma^2 \)) of 49. The program transforms the sample to have a mean of 15 and calculates the mean and sample standard deviation.

## Exercise 2: 95% Confidence Interval

The program calculates the critical value (\( t \)) for a 95% confidence interval using the t-distribution.

## Exercise 3: 100 Random Samples of 20 Values

One hundred random samples, each containing 20 values, are generated from a normal distribution with a mean (\( \mu \)) of 15 and a variance (\( \sigma^2 \)) of 49. For each sample, the program calculates the sample mean, sample standard deviation, 95% confidence interval, and checks if the interval includes the true mean.

## Exercise 4: Compare Sample Means with True Mean

The sample means with their 95% confidence intervals are plotted for all 100 samples. The true mean (\( \mu \)) is represented by a dashed line, and the confidence intervals are color-coded to indicate whether they include the true mean or not.

## Exercise 5: Compare Sample Means with Different Confidence Levels

The program defines a function to generate 100 samples with different confidence intervals based on user-defined confidence levels. Two scenarios with confidence levels of 99.7% and 80% are presented, and the samples are plotted similarly to Exercise 4.

### Conclusion

This Python program provides a hands-on exploration of statistical concepts, including the generation of random samples, calculation of confidence intervals, and comparison of sample means with the true mean. The visualizations aid in understanding the variability and reliability of sample statistics in different scenarios.