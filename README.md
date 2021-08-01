# sarcov2_immunopathology
Using existing single cell RNA sequencing datasets to profile key immunopathology genes in SARS-CoV2 patients and normal controls at single cell resolution.

#### Installation
##### Requirements
-Ensure you have read and write permissions to the computer you are using.
-Enusre you have conda installed. If not, see the instructions at: https://docs.conda.io/projects/conda/en/latest/user-guide/install/

For Mac or Linux/Unix based operating systems:
Start the terminal and type in the commands below in the listed order:
1. $ cd <path to the directory containing the dowloaded folder 'sarcov2_immunopathology'>
2. $ sudo conda create -n sarcov2_immunopathology python=3.6.8
3. $ sudo conda activate sarcov2_immunopathology
4. $ sudo conda env update --file sarcov2_immunopathology.yml 

#### Source code
All source code is in the folder named notebook. You will find utility function in the python script 'utility_functions.py' and all the analysis code in the notebook named 'covid_sc_immunopathology.ipynb'.   

#### Data sets
All datasets are in the directory named 'datasets'. Use Scanpy's read_loom function to read into the expression datasets.
#### Citation
Ngara, M., and Siwo, G.H. (2021). Molecular relationships between SARS-CoV-2 Spike protein and LIFR, a pneumonia protective IL-6 family cytokine receptor. bioRxiv, 2021.2004.2018.440296.
See the full article at: https://www.biorxiv.org/content/10.1101/2021.04.18.440296v1
