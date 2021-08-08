#Program implementing DeepOlf architecture
#problemA: Determines molecule is odorant or odorless
#   Molecule is represented as a vector of 1622 molecular properties
#problemB: Determine interacting olfactory receptors (OR) for a odorant
#   Moleucle is reprsented as a vector of 1547 molecular properties
#   Interacting OR's 179
#   Each OR is encoded by a vector of 9,920 physiochemical properties calculated using 'protr' package

import numpy as np
import pandas as pd
import seaborn as sns
import os
import sys
from keras.utils.np_utils import to_categorical
from sklearn.preprocessing import StandardScaler
from keras.models import load_model
from keras.optimizers import Adam
from keras.utils import np_utils
from keras.wrappers.scikit_learn import KerasClassifier

path="C:/Users/Rajnish Kumar/Desktop/DeepOlf/"

def problemA(input_A, input_B, path):
    
    #Upload Train dataset
    problemA_data = pd.read_csv("problemA_data.csv")
    
    #Normalize data
    sc = StandardScaler()  
    problemA_data = sc.fit_transform(problemA_data)  
    problemA_user_input = sc.transform(input_A)
    
    #Model run: Predicting molecule is odorant or odorless
    modelA=load_model("problemA_model.h5")
    modelA.compile(loss='categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])
    problemA_prediction=(modelA.predict(problemA_user_input)).round()
    resultA=problemA_prediction[:,0].astype(int)
    
    if (resultA == 1):
        Y = problemB(input_B, path)
        print ('\n Interacting proteins are :')
        print (Y)
    else:
        print ('\n Molecule is Odorless \n')

def problemB(input_B, path):
    
    #Training data and required files
    problemB_data = pd.read_csv("problemB_data.csv")
    protein_features = pd.read_csv("protein_features.csv")
    protein_names = pd.read_csv("protein_names.csv")
    problemB_input=pd.concat([protein_features, input_B], axis =1).ffill()
    
    #Normalizing data    
    sc1 = StandardScaler()  
    problemB_data = sc1.fit_transform(problemB_data)  
    problemB_user_input = sc1.transform(problemB_input)
    
    #ModelB Run: Predicting interacting proteins
    modelB=load_model("problemB_model.h5")
    modelB.compile(loss='categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])
    problemB_prediction=(modelB.predict(problemB_user_input))
    xyz=np.append(protein_names,problemB_prediction,axis=1) 
    dataframe=pd.DataFrame({'Proteins':xyz[:,0], 'Interacting': xyz[:,1]})
    convert_dict={'Proteins':str, 'Interacting': float}
    dataframe = dataframe.astype(convert_dict)
    resultB=dataframe.nlargest(2,'Interacting')
   
    return resultB
    
## User Input 
user_input=(pd.read_csv("user_input.csv"))
input_A =user_input
input_B = user_input.drop(['nRSCN','nRNCS','nRCOSR','nArCOSR','nArNHO','nRNO2','nSO','nSO3','nR=CHX','ntH-Thiophenes','nOxazoles','I-104','SsNH3+','SssNH2+','SsssNH+','SddsP','SdssSe','NsNH3+','NssNH2+','NsssNH+','NddsP','NdssSe','CATS2D_01_AL','CATS2D_00_PN','T(Cl..I)','B01[O-Cl]','B01[O-Br]','B01[O-I]','B01[S-X]','B02[P-P]','B04[O-F]','B04[B-B]','B05[O-B]','B06[N-I]','B06[Br-Br]','B07[N-I]','B07[O-Br]','B07[S-S]','B07[S-Br]','B07[F-Cl]','B08[N-Br]','B08[O-Br]','B08[O-I]','B09[C-I]','B09[S-Cl]','B09[S-Br]','B10[C-I]','B10[O-F]','B10[O-I]','B10[S-S]','F01[O-Cl]','F01[O-Br]','F01[O-I]','F01[S-X]','F02[P-P]','F04[O-F]','F04[B-B]','F05[O-B]','F06[N-I]','F06[Br-Br]','F07[N-I]','F07[O-Br]','F07[S-S]','F07[S-Br]','F07[F-Cl]','F08[N-Br]','F08[O-Br]','F08[O-I]','F09[C-I]','F09[S-Cl]','F09[S-Br]','F10[C-I]','F10[O-F]','F10[O-I]','F10[S-S]'], axis = 1)

problemA(input_A, input_B, path)





        