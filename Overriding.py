class Animal:
    #Properties
    multicellular = True
    #Eukaryotic means Cells with Nucles
    eukaryotic = True
    #Function breathe
    def breathe(self):
        print("I breathe oxygen.")
    
    #Function feed
    def feed(self):
        print("I eat food.")
    
class Herbivorous(Animal):
    #Function feed
    def feed(self):
        print("I eat only plants. I am avegetarian.")
        
herbi = Herbivorous()
herbi.feed()
#Calling some other function
herbi.breathe()
