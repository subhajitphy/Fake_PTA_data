# Fake_PTA_data
## Instructions
* Store all the pulsars along with their precise RA and Dec obtained from the output of the ```random_psr.ipynb``` notebook.
* Let's say you intend to generate 10 years of fake data for an arbitrary pulsar. First, change the name of the pulsar and set the corresponding RA and Declination Dec properly in the arbitrary parameter (par) file.
* Then create fake TOAs using the following script for Tempo2 (refer to tempo2 -gr fake -h for the corresponding documentation).
  ``` tempo2 -gr fake -f psr.par -nobsd 1 -ndobs 10 -randha y  -start 50000 -end 53652 -rms 1e-3 ``` . If you desire to extend the duration of the data span, adjust the ```-end``` parameter for the object accordingly.  This will generate a psr.simulate file. Change the name to psr_sim.tim; otherwise, it will not be acceptable by the Enterprise Pulsar object.
* Now, execute the ```inj.ipynb``` notebook for each pulsar, which will then store the injected parameters along with data files in the newly created directory.

## Required PTA environment
* The complete PTA environment installation instructions with all packages required for recent PTA analysis can be found [here](https://docs.google.com/document/d/13QHfcqVMBhYbE-bt_qSMlhcDBkS0wYEd60VNhlae26A/edit?usp=sharing).
