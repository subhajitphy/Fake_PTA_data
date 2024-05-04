# Create Pickled Fake_PTA_data from a subset of 78 MPTA Pulsar

* ```create_par.py``` selects a subset of pulsars from the real 78 [MPTA](https://dmc.datacentral.org.au/dataset/meerkat-pulsar-timing-array-mpta-first-data-release) pulsar list.
* ```MPTA_par/create_tim.sh``` creates fake TOAs from the selected `par` file list.
* ```MPTA_par/inj_run.sh``` performs the injection, with the output stored inside `MPTA_par/MPTA_simulation`.
* ```MPTA_par/MPTA_simulation/pickle_all.sh``` pickles the psr object, while ```MPTA_par/MPTA_simulation/Pickles/combined_pkl.py``` combines all the pickle files and gives a single output (```combined_58psr.pkl```) which may be of interest to you.


