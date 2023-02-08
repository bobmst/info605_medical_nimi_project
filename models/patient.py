from . import tables
from datetime import datetime

tb_patient = tables.tb_patient


class Patient:
    def __init__(self, id):
        self.Id = id
        self.FIRST = tb_patient[tb_patient.Id == id].FIRST.values[0]
        self.LAST = tb_patient[tb_patient.Id == id].LAST.values[0]
        self.BIRTHDATE = tb_patient[tb_patient.Id == id].BIRTHDATE.values[0]
        self.DEATHDATE = tb_patient[tb_patient.Id == id].DEATHDATE.values[0]
        self.SSN = tb_patient[tb_patient.Id == id].SSN.values[0]
        self.DRIVERS = tb_patient[tb_patient.Id == id].DRIVERS.values[0]
        self.PASSPORT = tb_patient[tb_patient.Id == id].PASSPORT.values[0]
        self.PREFIX = tb_patient[tb_patient.Id == id].PREFIX.values[0]
        self.SUFFIX = tb_patient[tb_patient.Id == id].SUFFIX.values[0]
        self.MAIDEN = tb_patient[tb_patient.Id == id].MAIDEN.values[0]
        self.MARITAL = tb_patient[tb_patient.Id == id].MARITAL.values[0]
        self.RACE = tb_patient[tb_patient.Id == id].RACE.values[0]
        self.ETHNICITY = tb_patient[tb_patient.Id == id].ETHNICITY.values[0]
        self.GENDER = tb_patient[tb_patient.Id == id].GENDER.values[0]
        self.BIRTHPLACE = tb_patient[tb_patient.Id == id].BIRTHPLACE.values[0]
        self.ADDRESS = tb_patient[tb_patient.Id == id].ADDRESS.values[0]
        self.CITY = tb_patient[tb_patient.Id == id].CITY.values[0]
        self.STATE = tb_patient[tb_patient.Id == id].STATE.values[0]
        self.COUNTY = tb_patient[tb_patient.Id == id].COUNTY.values[0]
        self.ZIP = tb_patient[tb_patient.Id == id].ZIP.values[0]
        self.LAT = tb_patient[tb_patient.Id == id].LAT.values[0]
        self.LON = tb_patient[tb_patient.Id == id].LON.values[0]
        self.HEALTHCARE_EXPENSES = tb_patient[
            tb_patient.Id == id
        ].HEALTHCARE_EXPENSES.values[0]
        self.HEALTHCARE_COVERAGE = tb_patient[
            tb_patient.Id == id
        ].HEALTHCARE_COVERAGE.values[0]

    def get_age(self):
        # TODO check the birthdate/deathdate format
        if self.DEATHDATE:
            return (
                datetime.strptime(self.DEATHDATE, "%Y-%m-%d")
                - datetime.strptime(self.BIRTHDATE),
                "%Y-%m-%d",
            )
        else:
            return datetime.now() - datetime.strptime(self.BIRTHDATE, "%Y-%m-%d")
