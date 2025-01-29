from backend.src.parser_generic import MedicalDocParser
import re

class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self,text)
        
    def parse(self):
        return{
            'patient_name': self.get_name(),
            'patient_address': self.get_address(),
            'medicines': self.get_medicine().replace('\n',',').strip(),
            'directions': self.get_directiions(),
            'refill': self.get_refill()
        }
        
    # Above function needs to be modified if below function is utilized
    def parser(self):
        return{
            'patient name': self.get_field('patient name'),
            'patient address': self.get_field('patient address'),
            'medicines': self.get_field('medicines').replace('\n',',').strip(),
            'directions': self.get_field('directions'),
            'refill': self.get_field('refill')
        }
        
    # This function can replace the below 5 functions if format is ignored
    def get_field(self,field):

        info = {
                'patient name': {'pattern':'Name:(.*)Date', 'flags': 0},
                'patient address': {'pattern':'Address:(.*)\n', 'flags': 0},
                'medicines': {'pattern':'Address:[^\n]*(.*)Directions', 'flags': re.DOTALL},
                'directions': {'pattern':'Directions:(.*)Refill', 'flags': re.DOTALL},
                'refill': {'pattern':'Refill:(.*)times', 'flags': 0},
                }
        
        field_name = info.get(field)
        if field_name:
            matches = re.findall(field_name['pattern'],self.text,flags=field_name['flags'])
            if len(matches) > 0:
                return matches[0].strip()
    
    def get_name(self):
        pattern = 'Name:(.*)Date'
        matches = re.findall(pattern,self.text)
        if len(matches) > 0:
            return matches[0].strip()
        
    def get_address(self):
        pattern = 'Address:(.*)\n'
        matches = re.findall(pattern,self.text)
        if len(matches) > 0:
            return matches[0].strip()
        
    def get_medicine(self):
        pattern = 'Address:[^\n]*(.*)Directions'
        matches = re.findall(pattern,self.text,flags=re.DOTALL)
        if len(matches) > 0:
            return "\n".join(line.strip() for line in matches[0].split("\n")).strip()
            
        
    def get_directiions(self):
        pattern = 'Directions:(.*)Refill'
        matches = re.findall(pattern,self.text,flags=re.DOTALL)
        if matches:
            return " ".join(line.strip() for line in matches[0].split("\n")).strip()
        
    def get_refill(self):
        pattern = 'Refill:(.*)times'
        matches = re.findall(pattern,self.text)
        if matches:
            return matches[0].strip()

    
    
if __name__ == "__main__":
    
    doc_text = """
    Dr John Smith, M.D
    2 Non-Important Street,
    New York, Phone (000)-111-2222
    Name: Marta Sharapova Date: 5/11/2022
    Address: 9 tennis court, new Russia, DC
    Prednisone 20 mg
    Lialda 2.4 gram
    Directions:
    Prednisone, Taper 5 mig every 3 days,
    Finish in 2.5 weeks a
    Lialda - take 2 pill everyday for 1 month
    Refill: 2 times
    """



    pp = PrescriptionParser(doc_text)
    print(pp.parser())
    
    
    
        

    

        