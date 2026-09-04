# Z-Score and One-Sample Z-Test — Detailed Notes
1. **Z-score** = A statistical measure that tells us **how many standard deviations an observed value is away from the mean**.

2. **Z-test** = A **statistical hypothesis test** that uses a Z-score to determine whether a sample result is **significantly different from a hypothesized population value**.

## 1. Ordinary Z-Score

A **Z-score** tells us how many standard deviations an individual observation is away from the population mean.

### Formula

$$
\boxed{Z=\frac{X-\mu}{\sigma}}
$$

Before substituting values, understand every symbol:

* `X` = the individual observed value
* `μ` = population mean
* `σ` = population standard deviation
* `Z` = standardized distance from the population mean

### Example

Suppose:

$$
\mu=170\text{ cm}
$$

$$
\sigma=10\text{ cm}
$$

and we observe one person whose height is:

$$
X=190\text{ cm}
$$

First write the equation:

$$
Z=\frac{X-\mu}{\sigma}
$$

Now substitute:

$$
Z=\frac{190-170}{10}
$$

$$
Z=\frac{20}{10}
$$

$$
\boxed{Z=2}
$$

### Interpretation

The value \(190\) cm is:

$$
\boxed{2\text{ standard deviations above the population mean}}
$$

The Z-score itself is **not a probability**.

It is a standardized distance.

---

# 2. From Z-Score to Probability

Suppose the population is normally distributed:

$$
\boxed{X\sim N(\mu,\sigma^2)}
$$

For example:

$$
\boxed{X\sim N(170,10^2)}
$$

This means:

* \(X\) = random variable representing an individual observation
* \(N\) = Normal distribution
* \(170\) = population mean \(\mu\)
* \(10^2=100\) = population variance \(\sigma^2\)
* therefore population standard deviation is:

$$
\sigma=\sqrt{100}=10
$$

If:

$$
X=190
$$

then:

$$
Z=2
$$

We can now ask for a probability.

For example:

$$
P(Z\ge2)
$$

This means:

> Probability of getting a Z-score of 2 or greater.

For the standard normal distribution:

$$
Z\sim N(0,1)
$$

The standard normal cumulative distribution function is:

$$
\Phi(z)=P(Z\le z)
$$

From a standard normal table/calculator:

$$
\Phi(2)\approx0.9772
$$

Therefore:

$$
P(Z\ge2)=1-P(Z\le2)
$$

$$
=1-0.9772
$$

$$
\boxed{P(Z\ge2)=0.0228}
$$

or:

$$
\boxed{2.28\%}
$$

The value \(0.9772\) ultimately comes from evaluating the standard normal density:

$$
f(z)=\frac{1}{\sqrt{2\pi}}e^{-z^2/2}
$$

and integrating:

$$
P(Z\le2)
=
\int_{-\infty}^{2}
\frac{1}{\sqrt{2\pi}}e^{-z^2/2}\,dz
$$

which gives approximately:

$$
0.97725
$$

---

# 3. Why Do We Need a Sample?

Usually we cannot measure an entire population.

Suppose a company produces millions of bottles.

The company claims:

$$
\boxed{\mu=500\text{ ml}}
$$

We cannot measure every bottle, so we take a sample.

Suppose we take:

$$
n=4
$$

bottles.

Our sample is:

$$
498,\ 505,\ 493,\ 512
$$

Here:

$$
\boxed{n=4}
$$

means the sample contains 4 observations.

---

# 4. Sample Mean

The mean of the sample is called the **sample mean** and is represented by:

$$
\boxed{\bar X}
$$

The formula is:

$$
\boxed{
\bar X=
\frac{X_1+X_2+\cdots+X_n}{n}
}
$$

where:

* \(X_1,X_2,\ldots,X_n\) = individual observations in the sample
* \(n\) = number of observations
* \(\bar X\) = average of the sample

For our sample:

$$
498,\ 505,\ 493,\ 512
$$

First write the equation:

$$
\bar X=
\frac{X_1+X_2+X_3+X_4}{4}
$$

Substitute:

$$
\bar X=
\frac{498+505+493+512}{4}
$$

Calculate:

$$
\bar X=\frac{2008}{4}
$$

Therefore:

$$
\boxed{\bar X=502\text{ ml}}
$$

### Meaning

The **average of the four bottles we actually measured** is 502 ml.

It does not mean the population mean is definitely 502 ml.

---

# 5. Why Multiple Samples?

Imagine repeatedly taking samples of the same size:

$$
n=4
$$

For example:

$$
\text{Sample 1}\rightarrow\bar X_1=502
$$

$$
\text{Sample 2}\rightarrow\bar X_2=500
$$

$$
\text{Sample 3}\rightarrow\bar X_3=506.5
$$

$$
\text{Sample 4}\rightarrow\bar X_4=497
$$

$$
\text{Sample 5}\rightarrow\bar X_5=501
$$

The sample means are different because every sample contains different observations.

If we repeatedly took samples and calculated their means, those sample means would form their own probability distribution.

This is called the:

$$
\boxed{\text{Sampling distribution of }\bar X}
$$

The ordering of the sample means is only useful for visualization; the mathematical object is the **distribution of the sample means**.

---
## Standard Error When Population Standard Deviation Is Unknown

In real-world data science, we usually **do not know the population standard deviation `σ`**.

Instead, we calculate the **sample standard deviation `s`** from the data we have and use it to estimate the standard error.

### Example: Customer Spending

Suppose we want to estimate the average amount customers spend on an online store.

We collect a sample of 8 customers:

```
120, 150, 130, 160, 140, 135, 155, 110
```

### Step 1: Calculate the Sample Mean

The sample mean is:

$$
\bar X = \frac{\sum X_i}{n}
$$

Substitute the values:

$$
\bar X =
\frac{120+150+130+160+140+135+155+110}{8}
$$

$$
\bar X = 137.5
$$

Therefore:

* `X̄` = 137.5
* `n` = 8

### Step 2: Calculate the Sample Standard Deviation

Since the population standard deviation `σ` is unknown, we calculate the **sample standard deviation `s`**.

The formula is:

$$
s =
\sqrt{
\frac{\sum (X_i-\bar X)^2}{n-1}
}
$$

For our sample:

$$
s =
\sqrt{
\frac{
(120-137.5)^2+
(150-137.5)^2+
(130-137.5)^2+
(160-137.5)^2+
(140-137.5)^2+
(135-137.5)^2+
(155-137.5)^2+
(110-137.5)^2
}{8-1}
}
$$

After calculation:

$$
s \approx 17.64
$$

Therefore:

* `s` ≈ 17.64
* `s` = sample standard deviation

### Step 3: Calculate the Standard Error

Because the population standard deviation `σ` is unknown, we use the sample standard deviation `s`.

The formula is:

$$
SE = \frac{s}{\sqrt n}
$$

Substitute:

$$
SE = \frac{17.64}{\sqrt 8}
$$

$$
SE \approx 6.24
$$

Therefore:

* `SE` ≈ 6.24

### What Does This Mean?

Our sample mean is:

$$
\bar X = 137.5
$$

Our estimated standard error is:

$$
SE \approx 6.24
$$

The standard error tells us approximately **how much the sample mean would vary from sample to sample** if we repeatedly took samples of the same size from the same population.

### Important Distinction

If the population standard deviation is known:

$$
SE = \frac{\sigma}{\sqrt n}
$$

If the population standard deviation is unknown:

$$
SE = \frac{s}{\sqrt n}
$$

Where:

* `σ` = population standard deviation
* `s` = sample standard deviation
* `n` = number of observations in the sample
* `SE` = standard error of the sample mean

In real-world data science, `σ` is usually unknown, so we use `s` as an estimate of `σ`.

> **Note:** When `σ` is unknown and we are performing inference about a population mean, the usual method is to use the **t-distribution** rather than the classical Z-test.
