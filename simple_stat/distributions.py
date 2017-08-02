import numpy as np
import matplotlib.pyplot as plt




df=2
num_samples=100000
mu=0
sigma=1
standart_samples=np.random.normal(mu,sigma,num_samples)
# t_dist=np.random.standard_t(df,num_samples)
# plt.hist(standart_samples, bins=50, normed=True)
# plt.axvline(sigma,linewidth=4, color='black')
# plt.axvline(-sigma,linewidth=4, color='black')
#
# plt.axvline(2*sigma,linewidth=4, color='red')
# plt.axvline(-2*sigma,linewidth=4, color='red')
#
# plt.show()
print "-sigma,+sigma :" ,len(filter(lambda  x: x<=sigma and x >=-sigma,standart_samples))*1.0/num_samples*100.0, "% "
print "-2sigma,+2sigma :" ,len(filter(lambda  x: x<=2*sigma and x >=-2*sigma,standart_samples))*1.0/num_samples*100.0, "% "
print "-3sigma,+3sigma :" ,len(filter(lambda  x: x<=3*sigma and x >=-3*sigma,standart_samples))*1.0/num_samples*100.0, "% "

from  scipy.stats import norm
loc=45
sigma=12
scale=sigma
x=np.linspace(0,100,10000)
y=norm.rvs(loc,scale,size=10000)
standart_samples_norm=norm.pdf(x, loc, scale)
print standart_samples_norm
plt.plot(x,standart_samples_norm,lw=3)
plt.hist(y,normed=True,bins=50)
plt.show()