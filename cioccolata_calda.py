class Calda:
    def __init__(self,densità,calda):
        self.densità=densità
        self.calda=calda
        self.qty=20*self.densità
        if self.calda==True:
            self.qty+=5
        