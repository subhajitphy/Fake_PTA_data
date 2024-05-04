import json, os, glob, argparse, subprocess, sys, pickle 
import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord
import libstempo as lst
import libstempo.plot as lstplot
import libstempo.toasim as toasim
from enterprise.pulsar import Pulsar
from numpy import log10 as lg


code = sys.argv[0]
idx = int(sys.argv[1])

#datadir="./MPTA_par/"
datadir="./"
psrlist=np.loadtxt(f'{datadir}/psrlist.txt',dtype=object)
psr=psrlist[idx]


par = glob.glob(f"{datadir}/{psr}*par")[0]
tim = glob.glob(f"{datadir}/{psr}*.tim")[0]

#print(par,tim)



psr = lst.tempopulsar(parfile=par, timfile=tim, maxobs=64000)


psr_ent = Pulsar(par, tim)


lstplot.plotres(psr, label="Residuals")




toasim.make_ideal(psr)
lstplot.plotres(psr, label="Residuals")



efac=np.random.uniform(0.8,1.1)
equad=np.random.uniform(-8,-6)
ecorr=np.random.uniform(-8,-6)
RN_Amp=np.random.uniform(-16,-13)
RN_gamma=np.random.uniform(2,6)
gwb_log10_A = lg(2.4e-15)

psrname=psr_ent.name
inj_dict={f"{psrname}_efac":efac,f"{psrname}_log10_equad":equad,f"{psrname}_log10_ecorr":ecorr,f"{psrname}_log10_RN_Amp":RN_Amp,
          f"{psrname}_RN_gamma":RN_gamma,"gwb_log10_A":gwb_log10_A}



savedir="MPTA_simulation"

if not os.path.exists(savedir):
    os.mkdir(savedir)
    
with open(f"{savedir}/{psrname}_inj_params.dat", "w") as outfile:
    json.dump(inj_dict, outfile, indent=4)




toasim.add_efac(psr, efac)




toasim.add_equad(psr, 10**equad)




toasim.add_jitter(psr, ecorr =10**ecorr,coarsegrain = 1.0/86400.0)




lstplot.plotres(psr, label="Residuals")



tmin = psr_ent.toas.min()
tmax = psr_ent.toas.max()
Tspan = tmax - tmin
toasim.add_rednoise(psr, 10**RN_Amp, RN_gamma,components = 30)

toasim.add_gwb(psr, flow=1e-9, fhigh=1e-7, gwAmp=10**gwb_log10_A)


lstplot.plotres(psr, label="Residuals")


psr.fit(iters=3)

print("Writing simulated data for", psr.name)
psr.savepar(f"{savedir}/{psr.name}_sim.par")
psr.savetim(f"{savedir}/{psr.name}_sim.tim")
lst.purgetim(f"{savedir}/{psr.name}_sim.tim")

