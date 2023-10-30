import numpy as np
import pandas as pd
import linecache
from .constants import *
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt 
from os import listdir

def filenames(dir='espectros'):
    return ['espectros/'+f for f in listdir(dir)]

# Now extracting the information from the files
# we are defining a function that extracts the file's data
# into two arrays
def extract(file):
    # Returning λ[Å],I
    return np.loadtxt(file,unpack=True,skiprows=32)

# This function reads the line 24 of the file 
# and returs it as a string, this line contains the 
# information on the effective temperature
def get_temp(file):
    return linecache.getline(file,24)

# Defining the planck distribution function 
# as a function of wavelength λ[Å]
def Bλ(λ,A,T):
    a = 2*h*(c**2)/(λ**5)
    b = np.exp(h*c/(λ*k_B*T)) - 1
    return (A*a/b)

# This function returns the values for the constant A 
# and the parametrized T for a given spectrum within a file 

def fit_planck(file):
    x,y = extract(file)
    
    # Data handling 
    # Some specters have failing 
    # this will be fixed by dropping the values with 
    # y < 1e-3
    
    df = pd.DataFrame()
    df['x'] = x 
    df['y'] = y 
    df = df[df.y > 1e-3]

    # reassigning x,y as the new values
    x,y = df.x,df.y


    # performing the fit with the new values 
    popt,pcov = curve_fit(Bλ,x,y,p0=[1e-3,5000.0])

    return x,y,popt

# This function returns the color temperature of each file 
# 
def get_color_temperature(files):
    Tc = []
    for file in files:
        x,y,[A,T] = fit_planck(file)
        Tc.append(T)
    return Tc

def plot_curves(
        files,ymax=1.2,legend=True,xlim = None,ylim = None,scatter=True,fit=True,
                figsize=(10,4),smooth = None):

    fig, ax = plt.subplots(figsize=figsize)
    
    for file in files:
        if fit:
            x,y,[A,T] = fit_planck(file)
            ax.plot(x,Bλ(x,A,T),label = f"T = {T:.0f}K")
        else:
            x,y = extract(file)

        if smooth:
            ax.plot(x,np.convolve(y,np.ones(50),'same'))

        if scatter:
            ax.scatter(x,y,label = file,s=0.01)
        else:
            ax.plot(x,y,label = file)
        
    
    ax.set_xlabel('λ [Å]')
    ax.set_ylabel('I [Arbitrary]')
    ax.set_ylim(0.0,ymax)
    
    if ylim:
        ax.set_ylim(ylim)

    if xlim:
        ax.set_xlim(xlim)

    if legend:
        ax.legend()
    fig.show()