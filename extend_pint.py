from pint.config import examplefile
from pint.models import get_model_and_toas
from pint.logging import setup as setup_log
from pint.simulation import make_fake_toas_fromtim
from copy import deepcopy
import sys
code = sys.argv[0]
par = sys.argv[1]
tim= sys.argv[2]

setup_log(level="WARNING")


m, t = get_model_and_toas(par, tim, bipm_version="BIPM2021")

span = t.get_mjds().max() - t.get_mjds().min()

t2 = deepcopy(t)

t2.adjust_TOAs(span)

t2.write_TOA_file("shifted.tim")

t2sim = make_fake_toas_fromtim("shifted.tim", m, add_noise=True)

t3 = t + t2sim

t3.write_TOA_file(f"{tim}_extend")
