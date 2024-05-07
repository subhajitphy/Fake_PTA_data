import pickle, sys,os, numpy as np, glob, libstempo as lst
from enterprise.pulsar import Pulsar


code = sys.argv[0]
idx = int(sys.argv[1])

#datadir="./MPTA_par/"
datadir="./"
psrlist=np.loadtxt(f'{datadir}/psrlist.txt',dtype=object)
psr=psrlist[idx]

par_ent = glob.glob(f"{datadir}/{psr}*par")[0]
tim_ent = glob.glob(f"{datadir}/{psr}*.tim")[0]

psr_ent = Pulsar(par_ent, tim_ent)


savedir="./Pickles"

if not os.path.exists(savedir):
    os.mkdir(savedir)

pickle_loc=f"./{savedir}/{psr}.pkl"

with open(pickle_loc, 'wb') as f:
    pickle.dump(psr_ent, f)
