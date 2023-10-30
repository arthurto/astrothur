from specutils.analysis import equivalent_width
from specutils.spectra import SpectralRegion
from specutils import Spectrum1D
from .spectrum import extract
from astropy import units as u 
from scipy.interpolate import splrep,BSpline

# A function to return the mean equivalent_width for a 
# file with a spectrum

# Smooth the spectrum
def smooth_f(x,y,s):
    tck = splrep(x,y,s=s)
    return BSpline(*tck)

def mean_ew(file,H,Δ):
    
    sr = SpectralRegion(H-Δ,H+Δ)

    wl,flx = extract(file)
    # print(wl,flx)
    f = smooth_f(wl,flx,s=100)
    flx_smooth = float(f((H+Δ)/u.AA)+f((H-Δ)/u.AA))/2
    # print(flx_smooth)
    spec = Spectrum1D(flx*u.Jy,wl*u.AA)
    return equivalent_width(spec,regions=sr,continuum=flx_smooth)/Δ