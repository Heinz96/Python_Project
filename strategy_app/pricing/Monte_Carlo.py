#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 22:52:28 2021

@author: alex
"""

import numpy as np


def Monte_Carlo(n_iter, S0, K, r, sigma, T, opt = "Call"):
    if opt == "Call": call, put = 1, 0
    else: call, put = 0, 1
    
    eps = np.random.normal(size = n_iter)
    C = np.zeros(n_iter)
    
    for j in range(n_iter):
        
        S = S0*np.exp((r - 0.5*sigma**2)*T + sigma*eps[j]*np.sqrt(T))
        C[j] = np.exp(-r*T)*(call*max(S - K, 0) + put*max(-S + K, 0))
    
    return C.mean()

