# sarcov2_immunopathology
Using existing single cell RNA sequencing datasets to profile key immunopathology genes in SARS-CoV2 patients and normal controls at single cell resolution.

#### Installation
For Mac or Linux/Unix based operating systems:
Start the terminal and type in the commands below in the listed order:
1. $ cd <path to the directory containing the dowloaded folder 'sarcov2_immunopathology'>
2. $ sudo conda create -n sarcov2_immunopathology python=3.6.8
3. $ conda activate sarcov2_immunopathology
4. $ conda env update --file sarcov2_immunopathology.yml 

#### Source code
All source code is in the folder named notebook. You will find utility function in the python script 'utility_functions.py' and all the analysis code in the notebook named 'covid_sc_immunopathology.ipynb'.   

#### Data sets
All datasets are in the directory named 'datasets'.
