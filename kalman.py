import numpy as np
import matplotlib.pyplot as plt

def main(args):
    for x in range(args.states): 
        filter()

def filter():
    plt.rcParams['figure.figsize'] = (8, 4)

    # intial parameters
    x = -0.14 # truth
    n_iter = 50
    size = (n_iter,) # size of the array
    z = np.random.normal(x,0.2,size=size) # normal about x, sigma=0.2

    R = 0.1**2 # estimate of measurement variance
    Q = 1e-5 # process variance

    P=np.zeros(size)         # error estimate
    Pm=np.zeros(size)    # error estimate
    xhm=np.zeros(size) # estimate of x
    xh=np.zeros(size)      # estimate of x
    K=np.zeros(size)         # gain

    #init guess of truth
    xh[0] = 1.0
    P[0] = 1.0

    for k in range(1,n_iter):
        # time update
        xhm[k] = xh[k-1]
        Pm[k] = P[k-1]+Q

        # measurement update
        K[k] = Pm[k]/( Pm[k]+R )
        xh[k] = xhm[k]+K[k]*(z[k]-xhm[k])
        P[k] = (1-K[k])*Pm[k]

    plt.figure()
    plt.plot(z,'k+',label='noise plus measurements')
    plt.plot(xh,'b-',label='estimate of truth')
    plt.axhline(x,color='g',label='truth')
    plt.legend()
    plt.title('Estimate vs. time', fontweight='bold')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.show()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--states', type=int, default=1)

    args = parser.parse_args()
    main(args)
