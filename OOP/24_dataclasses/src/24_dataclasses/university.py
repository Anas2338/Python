from dataclasses import dataclass

@dataclass
class Criminology:
    name:str
    rollno:str
    
    def fees(self):
        return f"{self.name} semester fee is 2000"
    

@dataclass
class Business(Criminology):
    pass

