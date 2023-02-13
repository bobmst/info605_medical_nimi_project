import pandas as pd
import numpy as np

# a sample
# tb: abbreviation of table
# vw: abbreviation of view

data_file = "./data/"
tb_patient = pd.read_csv(data_file + "patients.csv")
tb_allery = pd.read_csv(data_file + "allergies.csv")

tb_patient = tb_patient.replace({np.nan: None})
tb_allery = tb_allery.replace({np.nan: None})

vw_patient_allergy = pd.merge(
    tb_patient, tb_allery, how="left", left_on="Id", right_on="PATIENT"
).replace({np.nan: None})
