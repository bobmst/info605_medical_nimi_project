from . import tables
from datetime import datetime

vw_allergy = tables.vw_patient_allergy


class Allergy:
    def __init__(
        self,
        code,
        start,
        stop,
        description,
        encounter,
    ):
        self.CODE = code
        self.START = start
        self.STOP = stop
        self.ENCOUNTER = encounter
        self.DESCRITPION = description

    def get_duration():
        # TODO check data type
        # If there is no end time, maybe the shouldn't return with the duration until now
        if self.STOP:
            return self.START - self.STOP
        else:
            return datetime.now() - self.START


class Allergies:
    def __init__(self, id):
        self.PatientId = id

        self.allergies = []
        # TODO query the allergy table and get back a list of results
        # select * from allergies where Id == ""
        ls_allergies = (
            vw_allergy[vw_allergy.Id == id].reset_index(drop=True).to_numpy().tolist()
        )
        # TODO will reture None if we use a real query, change the if statement
        # allergy id
        if ls_allergies[0][-2] is not None:
            for a in ls_allergies:
                self.allergies.append(Allergy(a[-2],a[-6],a[-5],a[-1],a[-3]))

    def get_n_allergies(self):
        return len(self.allergies)
