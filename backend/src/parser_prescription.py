from backend.src.parser_generic import MedicalDocParser
import re

class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        super().__init__(text)
        
    def parse(self):
        pass
    
    def get_name(self):
        pattern = 'Name:(.*)Date'
        matches = re.findall(pattern,self.text)
        if len(matches) > 0:
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

    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))



    pp = PrescriptionParser(doc_text)
    print(pp.get_name())
        
    
    

        