import numpy as np
import matplotlib.pyplot as plt
import scipy.special

def main():
    plot_f()

def plot_e():
    n = np.arange(1,100)
    nlogn = n*np.log(n)
    fact = scipy.special.factorial(n)
    logn = np.log(fact)

    plt.plot(n,nlogn, color = 'black', linestyle = "--", label="n log n")
    plt.plot(n,logn, color = 'black', linestyle = "-", label="log(n!)")
    plt.plot(n,nlogn / 2, color = 'black', linestyle = "--", label="n/2 log n")
    plt.legend()
    plt.show()

def plot_f():
    n = np.arange(1,100)
    f = np.exp(1)**np.sqrt(np.log(n))
    g = np.sqrt(n)

    plt.plot(n,f, color = 'black', linestyle = "--", label=r"$ 2^\sqrt{log_2 n}$")
    plt.plot(n,g, color = 'black', linestyle = "-", label=r"$\sqrt{n}$")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
    