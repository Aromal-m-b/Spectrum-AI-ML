

# 7. Standard Error

The sample means themselves have variation.

The standard deviation of the sampling distribution of \(\bar X\) is:

$$
\boxed{
\sigma_{\bar X}=\frac{\sigma}{\sqrt n}
}
$$

This quantity is called the **standard error of the mean**:

$$
\boxed{
SE_{\bar X}=\frac{\sigma}{\sqrt n}
}
$$

### Important distinction

Population standard deviation:

$$
\sigma
$$

describes the spread of **individual observations**.

Standard error:

$$
\frac{\sigma}{\sqrt n}
$$

describes the spread of **sample means**.

---

# 8. Calculate the Standard Error

For our example:

$$
\sigma=10\text{ ml}
$$

and:

$$
n=4
$$

First write the equation:

$$
SE_{\bar X}=\frac{\sigma}{\sqrt n}
$$

Substitute:

$$
SE_{\bar X}=\frac{10}{\sqrt4}
$$

Calculate:

$$
SE_{\bar X}=\frac{10}{2}
$$

Therefore:

$$
\boxed{SE_{\bar X}=5\text{ ml}}
$$

### Meaning

The \(5\) ml is **not the standard deviation of individual bottles**.

It is the standard deviation of the theoretical distribution of sample means when samples contain 4 bottles.

In other words:

> If we repeatedly took samples of 4 bottles and calculated their means, those sample means would have a standard deviation of approximately 5 ml under this model.

---

# 9. Why Does the Standard Error Contain \(\sqrt n\)?

If:

$$
n=1
$$

then:

$$
SE=\frac{\sigma}{\sqrt1}=\sigma
$$

If:

$$
n=4
$$

then:

$$
SE=\frac{\sigma}{2}
$$

If:

$$
n=100
$$

then:

$$
SE=\frac{\sigma}{10}
$$

Therefore:

$$
\boxed{n\uparrow\Rightarrow SE\downarrow}
$$

A larger sample produces a more stable sample mean.

The mathematical derivation comes from:

$$
Var(\bar X)=\frac{\sigma^2}{n}
$$

Taking the square root:

$$
SD(\bar X)
=
\sqrt{\frac{\sigma^2}{n}}
$$

$$
=
\frac{\sigma}{\sqrt n}
$$

Therefore:

$$
\boxed{SE_{\bar X}=\frac{\sigma}{\sqrt n}}
$$

---

# 10. The Sampling Distribution

If the population is normally distributed:

$$
X\sim N(\mu,\sigma^2)
$$

then the sample mean is also normally distributed:

$$
\boxed{
\bar X\sim
N\left(\mu,\frac{\sigma^2}{n}\right)
}
$$

For our example:

$$
\mu=500
$$

$$
\sigma=10
$$

$$
n=4
$$

Therefore:

$$
\bar X
\sim
N\left(500,\frac{10^2}{4}\right)
$$

$$
\bar X\sim N(500,25)
$$

Since the variance is 25:

$$
SD(\bar X)=\sqrt{25}=5
$$

So:

$$
\boxed{\bar X\sim N(500,5^2)}
$$

---

# 11. From Ordinary Z-Score to Z-Test

For an individual observation:

$$
\boxed{
Z=\frac{X-\mu}{\sigma}
}
$$

We want to do the same thing to the **sample mean**.

Our random quantity is now:

$$
\bar X
$$

and the mean of its sampling distribution is:

$$
\mu
$$

and the standard deviation of its sampling distribution is:

$$
\frac{\sigma}{\sqrt n}
$$

Therefore, standardizing the sample mean gives:

$$
\boxed{
Z=
\frac{\bar X-\mu_0}
{\sigma/\sqrt n}
}
$$

This is the **one-sample Z-test statistic** when the population standard deviation is known.

Here:

* \(\bar X\) = observed sample mean
* \(\mu_0\) = population mean specified by the null hypothesis
* \(\sigma\) = known population standard deviation
* \(n\) = sample size
* \(\sigma/\sqrt n\) = standard error
* \(Z\) = Z-test statistic

---

# 12. Form the Hypotheses

The company claims:

$$
\mu=500
$$

We formulate the null hypothesis:

$$
\boxed{H_0:\mu=500}
$$

For a two-sided test, the alternative hypothesis is:

$$
\boxed{H_1:\mu\ne500}
$$

The question is:

> Is our observed sample sufficiently inconsistent with \(\mu=500\) to reject \(H_0\)?

---

# 13. Calculate the Z-Test Statistic

Our information:

$$
\mu_0=500
$$

$$
\sigma=10
$$

$$
n=4
$$

Our sample:

$$
498,\ 505,\ 493,\ 512
$$

We already calculated:

$$
\bar X=502
$$

and:

$$
SE=5
$$

The Z-test equation is:

$$
Z=
\frac{\bar X-\mu_0}
{\sigma/\sqrt n}
$$

Substitute:

$$
Z=
\frac{502-500}
{10/\sqrt4}
$$

Calculate the denominator:

$$
\sqrt4=2
$$

$$
\frac{10}{2}=5
$$

Therefore:

$$
Z=
\frac{502-500}{5}
$$

$$
Z=\frac{2}{5}
$$

$$
\boxed{Z=0.4}
$$

### Meaning of \(Z=0.4\)

Our observed sample mean:

$$
502
$$

is:

$$
\boxed{0.4\text{ standard errors above }500}
$$

It is not 0.4 ml.

It is not a probability.

It is a standardized distance.

---

# 14. Convert Z into a Probability

We now have:

$$
Z=0.4
$$

For a two-sided test, we care about values at least as far from zero in either direction:

$$
\boxed{P(|Z|\ge0.4)}
$$

The standard normal distribution is:

$$
Z\sim N(0,1)
$$

From the standard normal CDF:

$$
\Phi(0.4)\approx0.6554
$$

The probability of being above \(0.4\) is:

$$
P(Z\ge0.4)
=
1-\Phi(0.4)
$$

$$
=1-0.6554
$$

$$
=0.3446
$$

Because this is a two-sided test, there is an equal tail on the negative side:

$$
P(Z\le-0.4)=0.3446
$$

Therefore:

$$
P(|Z|\ge0.4)
=
0.3446+0.3446
$$

$$
\boxed{p\approx0.6892}
$$

So the p-value is approximately:

$$
\boxed{68.92\%}
$$

---

# 15. What Does the P-Value Mean?

The p-value is **not**:

$$
P(H_0\text{ is true})
$$

It is not:

> "There is a 68.92% chance that the company is telling the truth."

Instead, under \(H_0\):

$$
\boxed{
p=
P(\text{result at least this extreme}\mid H_0\text{ is true})
}
$$

In our example:

$$
p\approx0.689
$$

means:

> If the true population mean really is 500 ml, the probability of obtaining a sample mean at least this far from 500, in either direction, is approximately 68.9%.

Therefore, a sample mean of 502 ml is not particularly surprising under the assumption that:

$$
\mu=500
$$

---

# 16. Significance Level \(\alpha\)

Before making the decision, we choose a significance level.

A common choice is:

$$
\boxed{\alpha=0.05}
$$

This is a threshold for deciding when the evidence against \(H_0\) is sufficiently strong.

The decision rule is:

$$
\boxed{
p<\alpha
\Rightarrow
\text{Reject }H_0
}
$$

and:

$$
\boxed{
p\ge\alpha
\Rightarrow
\text{Fail to reject }H_0
}
$$

For:

$$
\alpha=0.05
$$

this becomes:

$$
\boxed{
p<0.05
\Rightarrow
\text{Reject }H_0
}
$$

$$
\boxed{
p\ge0.05
\Rightarrow
\text{Fail to reject }H_0
}
$$

---

# 17. Apply the Decision Rule

Our p-value is:

$$
p=0.6892
$$

Our significance level is:

$$
\alpha=0.05
$$

Compare:

$$
0.6892>0.05
$$

Therefore:

$$
\boxed{\text{Fail to reject }H_0}
$$

### Correct interpretation

> We do not have sufficient statistical evidence to reject the company's claim that the population mean is 500 ml.

### Incorrect interpretation

Do **not** say:

> "We proved the company is telling the truth."

Failing to reject \(H_0\) does not prove \(H_0\) is true.

It means the observed data does not provide sufficient evidence against it.

---

# 18. What Would Make Us Reject \(H_0\)?

For a two-sided Z-test with:

$$
\alpha=0.05
$$

the critical Z-values are approximately:

$$
\boxed{-1.96\quad\text{and}\quad+1.96}
$$

Therefore:

$$
\boxed{|Z|>1.96\Rightarrow\text{Reject }H_0}
$$

Our current result:

$$
Z=0.4
$$

is inside the non-rejection region:

```text
Reject              Fail to reject              Reject

←───────────────────────┬───────────────────────→
       -1.96            0             +1.96
                         ↑
                       Z = 0.4
```

Therefore:

$$
\boxed{\text{Fail to reject }H_0}
$$

---

# 19. Example Where We Reject

Keep the same company claim:

$$
H_0:\mu=500
$$

and same population SD:

$$
\sigma=10
$$

and same sample size:

$$
n=4
$$

But suppose the sample is:

$$
520,\ 518,\ 522,\ 520
$$

Calculate the sample mean:

$$
\bar X=
\frac{520+518+522+520}{4}
$$

$$
\bar X=\frac{2080}{4}
$$

$$
\boxed{\bar X=520}
$$

Standard error remains:

$$
SE=\frac{\sigma}{\sqrt n}
$$

$$
SE=\frac{10}{\sqrt4}
$$

$$
\boxed{SE=5}
$$

Now calculate the Z statistic:

$$
Z=
\frac{\bar X-\mu_0}
{\sigma/\sqrt n}
$$

Substitute:

$$
Z=
\frac{520-500}{5}
$$

$$
Z=\frac{20}{5}
$$

$$
\boxed{Z=4}
$$

For a two-sided test:

$$
p=P(|Z|\ge4)
$$

which is approximately:

$$
\boxed{p\approx0.000063}
$$

Compare:

$$
0.000063<0.05
$$

Therefore:

$$
\boxed{\text{Reject }H_0}
$$

Here the observed sample mean is sufficiently far from 500 that the result would be extremely unlikely under the assumption:

$$
H_0:\mu=500
$$

---

# 20. Complete Z-Test Workflow

The entire process can now be represented as:

```text
                POPULATION
                    │
             μ and σ are defined
                    │
                    ↓
             Company claims
                μ = 500
                    │
                    ↓
          Form H₀ and H₁
                    │
                    ↓
             Take a sample
                    │
                    ↓
          X₁, X₂, ..., Xₙ
                    │
                    ↓
          Calculate sample mean
                    │
                    ↓
                  X̄
                    │
                    ↓
          Calculate standard error
                    │
                    ↓
             σ / √n
                    │
                    ↓
          Calculate Z statistic
                    │
                    ↓
       Z = (X̄ - μ₀)/(σ/√n)
                    │
                    ↓
             Calculate p-value
                    │
                    ↓
             Compare p with α
                    │
             ┌──────┴──────┐
             ↓             ↓
          p < α          p ≥ α
             ↓             ↓
          Reject       Fail to reject
             H₀             H₀
```

---

# 21. Symbols — Quick Reference

| Symbol                 | Meaning                                  |
| ---------------------- | ---------------------------------------- |
| \(X\)                  | One individual observation               |
| \(X_1,X_2,\ldots,X_n\) | Observations in a sample                 |
| \(\mu\)                | True population mean                     |
| \(\mu_0\)              | Mean specified by the null hypothesis    |
| \(\sigma\)             | Population standard deviation            |
| \(\sigma^2\)           | Population variance                      |
| \(n\)                  | Number of observations in the sample     |
| \(\bar X\)             | Sample mean                              |
| \(SE\)                 | Standard error of the sample mean        |
| \(Z\)                  | Standardized Z-score or Z-test statistic |
| \(H_0\)                | Null hypothesis                          |
| \(H_1\) / \(H_a\)      | Alternative hypothesis                   |
| \(p\)                  | P-value                                  |
| \(\alpha\)             | Significance level                       |

---

# 22. The Most Important Distinctions

### Individual observation

$$
\boxed{
Z=\frac{X-\mu}{\sigma}
}
$$

You are asking:

> How many population standard deviations away is this individual value?

---

### Sample mean

$$
\boxed{
Z=\frac{\bar X-\mu_0}
{\sigma/\sqrt n}
}
$$

You are asking:

> How many standard errors away is this observed sample mean from the mean specified by \(H_0\)?

---

### Standard deviation vs standard error

$$
\boxed{\sigma}
$$

describes variation among **individual observations**.

$$
\boxed{\frac{\sigma}{\sqrt n}}
$$

describes variation among **sample means**.

---

### P-value vs \(\alpha\)

$$
\boxed{p}
$$

comes from the observed data and tells us how extreme the result is **assuming \(H_0\)**.

$$
\boxed{\alpha}
$$

is the threshold we choose before making the decision.

Decision:

$$
\boxed{p<\alpha\Rightarrow\text{Reject }H_0}
$$

$$
\boxed{p\ge\alpha\Rightarrow\text{Fail to reject }H_0}
$$

---

# 23. One-Line Mental Model

The entire idea can be reduced to:

$$
\boxed{
\text{Sample}
\rightarrow
\bar X
\rightarrow
SE
\rightarrow
Z
\rightarrow
p
\rightarrow
\text{compare with }\alpha
\rightarrow
\text{decision}
}
$$

The key conceptual shift is:

> **We don't use the Z-test to prove whether a company's claim is true. We assume the claim represented by \(H_0\), determine how probable our observed sample result would be under that assumption, and decide whether the evidence is sufficiently inconsistent with \(H_0\) to reject it.**
