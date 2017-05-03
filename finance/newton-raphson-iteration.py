from math import exp, log, sqrt, erf


# Standard Normal distribution with math library only
def Phi(x):
    return .5 * ( 1. + erf(x / sqrt(2)) )



# Black-Scholes Function
def BS(S, K, T, r, sig, cp):
    d1 = (log(S/K) + r*T) / (sig*sqrt(T)) + .5 * sig*sqrt(T)
    d2 = d1 - sig*sqrt(T)
    value = 0
    if cp == 'C':
        value = S*Phi(d1) - K*exp(-r*T)*Phi(d2)
    if cp == 'P':
        value = K*exp(-r*T)*Phi(-d2) - S*Phi(-d1)
    return value


# Function to find BS Implied Vol using Bisection Method
def impvol(S, K, T, r, C, cp, tol = 1e-5, fcount = 1e3):
    sig, sig_u, sig_d = .2, 1., 1e-3
    count = 0
    err = BS(S, K, T, r, sig, cp) - C

    # repeat until error is sufficiently small or counter hits fcount
    while abs(err) > tol and count < fcount:
        if err < 0:
            sig_d = sig
            sig = (sig_u + sig)/2
        else:
            sig_u = sig
            sig = (sig_d + sig)/2
        
        err = BS(S, K, T, r, sig, cp) - C
        count += 1
    
    # return NA if counter hit fcount
    if count == fcount:
        return -1
    else:
        return sig



# # S - stock price
# # K - strike
# # T - maturity in years
# # r - log risk free rate annualized
# # sig - volatililty annualized
# # cp - call/put flag
S, K, T, r, sig, cp = 105., 100., 30./365, 0, .15, 'C'
C = BS(S, K, T, r, sig, cp)
print('Call price: %.4f' % C)


# Test code:
# S - stock price
# K - strike
# T - maturity in years
# R - risk free rate annualized
# C - option price
# cp - call/put flag
S, K, T, r, C, cp = 105., 100., 30./365, 0, 5.282, 'C'
v = impvol(S, K, T, r, C, cp)
print('Implied volatility: %.4f' % v)