class Tavoletta:
    def __init__(self,peso,aggiunte_nocciole,aggiunte_mandorle,aggiunte_biscotti):
        self.peso=peso
        self.aggiunte=0
        if aggiunte_nocciole==True:
          self.aggiunte+=2
        if aggiunte_mandorle==True:
          self.aggiunte+=1
        if aggiunte_biscotti==True:
          self.aggiunte+=1
        self.qty=self.peso*4+self.aggiunte