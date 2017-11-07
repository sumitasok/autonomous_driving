For initialising weights, we use numpy random function.
to draw a random sample from a normal (Gaussian) distribution.

[Scipy Documentation](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.normal.html)

The probability density for the Gaussian distribution is

p(x) = \frac{1}{\sqrt{ 2 \pi \sigma^2 }}
e^{ - \frac{ (x - \mu)^2 } {2 \sigma^2} },

where \mu is the mean and \sigma the standard deviation. The square of the standard deviation, \sigma^2, is called the variance.

```
mu = 0
sigma = 0.1
s = numpy.random.normal(loc=mu, scale=std, size=1000)
```

we pass the mean and standard deviation, of the data set we give.

```
abs(mu - np.mean(s)) < 0.01
```
This returns `True`

At the same time, if we set the sigma to 2,

```
abs(mu - np.mean(s)) < 0.01
```
This returns `False`

and

```
abs(mu - np.mean(s)) < 0.2
```
This returns `True`

and

```
>>> mu, sigma = 0, 40
>>> s = np.random.normal(mu, sigma, 1000)
>>> abs(mu - np.mean(s)) < 0.2
```
Returns
```
True
```

