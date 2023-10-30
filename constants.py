from astropy import units as u 

# Constants 
c = 2.99792458e18 # Å/s
h = 6.626070e-14  # kg Å / s
k_B = 1.380649e-3 # Å^2 kg / K s 

SpectralBands = {
    'O':{'range':[30000,50000],'color':'#196ffa'},
    'B':{'range':[10000,30000],'color':'#4287f5'},
    'A':{'range':[7500,10000],'color':'#73a5f5'},
    'F':{'range':[6000,7500],'color':'#c9d8f0'},
    'G':{'range':[5200,6000],'color':'#f0edc9'},
    'K':{'range':[3700,5200],'color':'#e8c258'},
    'M':{'range':[2400,3700],'color':'#fc9003'}
}

# Hα = 4383.0*u.AA
Hα = 6562.5*u.AA
Hβ = 4861.3*u.AA
Hγ = 4340.4*u.AA
Hδ = 4101.7*u.AA
Hϵ = 3970.0*u.AA