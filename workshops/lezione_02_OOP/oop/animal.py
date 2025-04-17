# ================================
# Classe ANIMAL
# ================================

class Animal:
    
    def __init__(self, name: str):
        self.name = name
    
    def speak(self):
        print(f"{self.name} produce un suono")