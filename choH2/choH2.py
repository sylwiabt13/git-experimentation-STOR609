#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 10:37:04 2026

@author: bathetay
"""

import scipy
from math import log
from functools import reduce

def compose(*funcs):
    return reduce(lambda f,g : lambda x : f(g(x)), funcs, lambda x : x)

def choH(data) : return list(map(compose(float,log,lambda i : scipy.stats.kstest(data[-i:],data[:-i]).pvalue),range(1,len(data))))
