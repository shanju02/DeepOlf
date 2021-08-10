**DeepOlf: DNN based architecture for predicting odorants and their interacting Olfactory Receptors**

DeepOlf identifies an odorant molecule (Problem A) and predicts its interaction Olfactory Receptors (Problem B). A chemical compound is represented as a vector of 1622 properties for Problem A and 1547 properties for Problem B. Total 179 OR sequences are used, each encoded by a vector of 9,920 physiochemical properties calculated using 'protr' package.

**DeepOlf Tutorial**

Step 1: Install Anaconda3-5.2 or above

Step 2: Install or upgrade following libraries (python, numpy, tensorflow, keras, scikit-learn)

Step 3: Download and extract zipped file

Step 4: Uncompress problemA_data.zip and problemB_data.zip files

Step 5: Prepare input file (user_input.csv)

Calculate molecular properties and fingerprints from SMILES or sdf format of a chemical compound using software’s like PaDel, alvaDesc (recommended), DRAGON, etc. and save as user_input.csv. 

Keep the header information (first row) as such in input file.

Step 6: Change value of path variable in DeepOlf_script.py to the extracted folder and execute the script


**List of Files:**
1.	DeepOlf_script.py : Python script implementing DeepOlf Architecture to predict odorant molecules and their interacting Olfactory Receptors (OR)
2.	Examples.xlsx : Molecular properties and fingerprints of few odorants and odorless compounds
3.	problemA_data.csv : Training dataset used for Problem A 
4.	problemB_data.csv : Training dataset used for Problem B
5.	problemA_model.h5 : Prediction model for Problem A
6.	problemB_model.h5 : Prediction model for Problem B
7.	protein_features.csv : Pre-calculated molecular properties of OR’s using ‘protr’ package
8.	protein_names.csv : List of OR’s known to bind with odorants
9.	user_input.csv : Input file for DeepOlf_script.py
