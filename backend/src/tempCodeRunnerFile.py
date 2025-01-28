from backend.src.parser_generic import MedicalDocParser
# import re

# class PrescriptionParser(MedicalDocParser):
#     def __init__(self, text):
#         super().__init__(text)
        
#     def parse(self):
#         pass
    
#     def get_name(self):
#         pattern = 'Name:(.*)Date'
#         matches = re.findall(pattern,self.text)
#         if len(matches) > 0:
#             return matches[0].strip()