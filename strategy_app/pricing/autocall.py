# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:24:05 2021

@author: benja
"""
import numpy as np
import pandas as pd
# import cupy as cp
from time import time
# import matplotlib.pyplot as plt
# from math import *
from scipy.stats import norm
# import sys



cp_or_np = np
n = 10**6
r = 0.01
sigma = 0.4
maturity = 8 
S0 = 100
strike = 100
coupon = 6
barrier = 60
     
     

    
def autocall_pricing(cp_or_np, n, r, sigma, maturity, S0, strike, coupon, barrier):
    
    # if cp_or_np == cp:
    #     try:
    #         import cupy 
    #     except:
    #         return "La bibli ne peut pas etre importé"
    
    S = cp_or_np.zeros((n))
    S[:] = S0
    price = 0
    for i in range(int(maturity)):
      S[:] = S[:] * cp_or_np.exp((r - 0.5 * sigma**2) + sigma * cp_or_np.random.randn(len(S)))
      autocalled = S[S > strike]
      price += len(autocalled) * (S0 + coupon) / (1 + r)**(i + 1)
      S = S[S < S0]
    S_mid = S[S >= barrier]
    S_low = S[S < barrier]
    price += len(S_mid) * S0 / (1 + r)**maturity
    price += cp_or_np.sum(S_low) / (1 + r)**maturity
    price = price / n
    price= float(price)
    return price

def autocall_delta(cp_or_np, n, r, sigma, maturity, S0, strike, coupon, barrier):
    delta = (
             + autocall_pricing(cp_or_np, n, r, sigma, maturity, S0 * 1.01, strike, coupon, barrier) 
             - autocall_pricing(cp_or_np, n, r, sigma, maturity, S0 * 0.99, strike, coupon, barrier)
             ) / (0.02 * S0)
    return delta

def autocall_gamma(cp_or_np, n, r, sigma, maturity, S0, strike, coupon, barrier):
    gamma = (
             + autocall_pricing(cp_or_np, n, r, sigma, maturity, S0 * 1.01, strike, coupon, barrier) 
             - 2 * autocall_pricing(cp_or_np, n, r, sigma, maturity, S0, strike, coupon, barrier)
             + autocall_pricing(cp_or_np, n, r, sigma, maturity, S0 * 0.99, strike, coupon, barrier)
             ) / (0.02 * S0)
    return gamma

def autocall_vega(cp_or_np, n, r, sigma, maturity, S0, strike, coupon, barrier):
    vega = (
             + autocall_pricing(cp_or_np, n, r, sigma * 1.01, maturity, S0, strike, coupon, barrier) 
             - autocall_pricing(cp_or_np, n, r, sigma * 0.99, maturity, S0, strike, coupon, barrier)
             ) / (0.02 * sigma)
    return vega


def autocall_rho(cp_or_np, n, r, sigma, maturity, S0, strike, coupon, barrier):
    rho = (
         + autocall_pricing(cp_or_np, n, r * 1.01, sigma, maturity, S0, strike, coupon, barrier) 
         - autocall_pricing(cp_or_np, n, r * 0.99, sigma, maturity, S0, strike, coupon, barrier)
         ) / (0.02 * r)
    return rho