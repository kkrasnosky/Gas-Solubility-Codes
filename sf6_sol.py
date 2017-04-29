# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 15:41:18 2017

@author: kris Krasnosky

    INPUT: T = temperature in degrees C.
%-         S = salinity in psu.
%- OUTPUT:  The units of F are mol/kg/atm
"""


def sf6_sol(S, T):

    import numpy as np

    #----------------------
    # Check input parameters
    #----------------------
    #Python Takes care of this...

    # CHECK S,T dimensions and verify consistent
    if np.size(np.shape(T))>1:
        mt,nt=np.shape(T)
    else:
        mt = np.size(T)
        nt = 0
    if np.size(np.shape(S))>1:
        ms,ns=np.shape(S)
    else:
        ms = np.size(S)
        ns = 0

    # Check that T&S have the same shape or are singular
    if (ms != mt) or (ns != nt):
        print "F12sol: S & T must have same dimensions or be singular"
        return

    #------
    # BEGIN
    #------
    
    T = np.add(273.15,T)
    a1 = -82.16390000;
    a2 = 120.15200000;
    a3 = 30.63720000;
    
    b1 = 0.02932010;
    b2 = -0.03519740;
    b3 = 0.00740056;
    
    
    lnC = a1 + np.multiply(a2,(np.divide(100,T))) + np.multiply(a3,np.log(np.divide(T,100))) + np.multiply(S,b1) + np.multiply(b2,(np.divide(T,100))) + np.multiply(b3,np.power((np.divide(T,100)),2));
    sol = np.exp(lnC);
    return sol