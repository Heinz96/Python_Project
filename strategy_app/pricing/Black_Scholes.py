#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 22:07:10 2021

@author: alex
"""

import numpy as np
import scipy.stats as stats


def ds(S, K, sigma, r, T):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return d1, d2

def call(S, K, sigma, r, T):
    d1, d2 = ds(S, K, sigma, r, T)[0], ds(S, K, sigma, r, T)[1]
    return S*stats.norm.cdf(d1) - K*np.exp(-r*T)*stats.norm.cdf(d2)

def put(S, K, sigma, r, T):
    d1, d2 = ds(S, K, sigma, r, T)[0], ds(S, K, sigma, r, T)[1]
    return -S*stats.norm.cdf(-d1) + K*np.exp(-r*T)*stats.norm.cdf(-d2)

def delta(S, K, sigma, r, T, opt = "call"):
    d1 = ds(S, K, sigma, r, T)[0]
    if opt == "call":
        return stats.norm.cdf(d1)
    return stats.norm.cdf(d1) - 1

def gamma(S, K, sigma, r, T):
    d1 = ds(S, K, sigma, r, T)[0]
    n = 1/np.sqrt(2*np.pi)*np.exp(-d1**2/2)
    return n/(S*sigma*np.sqrt(T))

def vega(S, K, sigma, r, T):
    d1 = ds(S, K, sigma, r, T)[0]
    n = 1/np.sqrt(2*np.pi)*np.exp(-d1**2/2)
    return S*n*np.sqrt(T)

def theta(S, K, sigma, r, T, opt = "call"):
    d1, d2 = ds(S, K, sigma, r, T)[0], ds(S, K, sigma, r, T)[1]
    n = 1/np.sqrt(2*np.pi)*np.exp(-d1**2/2)
    
    if opt == "call": 
        return -S*n*sigma/(2*np.sqrt(T)) - r*K*np.exp(-r*T)*stats.norm.cdf(d2)
    return -S*n*sigma/(2*np.sqrt(T)) + r*K*np.exp(-r*T)*stats.norm.cdf(-d2)



