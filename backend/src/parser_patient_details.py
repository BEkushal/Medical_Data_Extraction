from backend.src.parser_generic import MedicalDocParser
import re

class PatientDetailsParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self,text)
        
    def parse(self):
        return{
            'patient name':self.get_patient_name(),
            'phone number':self.get_patient_phone_number(),
            'medical issues':self.get_medical_problems(),
            'hepatitis b vaccination':self.get_hepatitis_b_vaccination()
        }
        
    def get_patient_name(self):
        pattern = 'Patient Information(.*?)\(\d{3}\)'
        matches = re.findall(pattern,self.text,flags=re.DOTALL)
        name = ""
        if matches:
            name = self.ext_name(matches[0])
        return name
    
    def get_patient_phone_number(self):
        pattern = 'Patient Information(.*?)(\(\d{3}\) \d{3}-\d{4})'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0][-1]
    
    def ext_name(self,name):
        # remove birth date
        name = name.replace("Birth Date","").strip()
        # remove date
        date_pattern = '((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[ \d]+)'
        date_matches = re.findall(date_pattern,name)
        
        if date_matches:
            date = date_matches[0][0]
            name = name.replace(date,'').strip()
        return name
    
    def get_hepatitis_b_vaccination(self):
        pattern = 'Have you had the Hepatitis B vaccination\?.*(Yes|No)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0].strip()
        
    def get_medical_problems(self):
        pattern = 'List any Medical Problems .*?:(.*)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0].strip()