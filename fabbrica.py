from tavoletta import Tavoletta
from cioccolata_calda import Calda
from cioccolatino import Cioccolatino 

class Fabbrica_cioccolato:
    def __init__(self,tipo,percentuale):
        self.qty=0
        self.tipo=tipo
        self.percentuale=percentuale
    def is_producing(self,prodotto):
        print(f'La fabbrica sta producendo {prodotto} con cioccolato {self.tipo} con il {self.percentuale}% di cacao')
    def controllo_produzione(self,prodotto):
        if self.qty+prodotto.qty>100:
            risposta=input('Richiesta produzione eccessiva,continuare con nuova operazione? s n')
            if risposta=='s':
                continua=True
            else:
                continua=False
        elif self.qty+prodotto.qty<100:
            self.qty+=prodotto.qty
            risposta=input('Richiesta effettuata, continuare la produzione? s n')
            if risposta=='s':
                continua=True
            else:
                continua=False
        else:
            self.qty+=prodotto.qty
            print('Produzione massima giornaliera raggiunta, fine giornata')
            self.qty=0
            continua=False
        return continua


tipo=input('Tipo cioccolato prodotto')
percentage=input('Percentuale')
fabbrica=Fabbrica_cioccolato(tipo,percentage)
produzione=True
while produzione==True:
    prodotto=input('Cosa vuoi produrre? 1)cioccolatino\n2)Tavoletta\n3)cioccolata calda')
    if prodotto=='1':
        forma=input('di che forma vuoi i cioccolatini?')
        ripieno=input('che ripeno vuoi?')
        numero=int(input('quanti ne vuoi produrre?'))
        cioccolatino=Cioccolatino(forma,ripieno,numero)
        nome='cioccolatino'
        fabbrica.is_producing(nome)
        print(f'i cioccolatini sono a forma di {cioccolatino.forma} e sono ripieni alla {cioccolatino.ripieno}')
        fabbrica.controllo_produzione(cioccolatino)
    elif prodotto=='2':
        b,m,n=False,False,False
        biscotto=input('Ci sono biscotti? s n')
        if biscotto=='s':
            b=True
        mandorle=input('Ci sono mandorle? s n')
        if mandorle=='s':
            m=True
        nocciole=input('Ci sono nocciole? s n')
        if nocciole=='s':
            n=True
        peso=float(input('quanti etti ne vuoi produrre(numero tra 1 e 5)?'))
        if peso<=5 and peso>1:
         nome='tavoletta'
         fabbrica.is_producing(nome)
         tavoletta=Tavoletta(peso,n,m,b)
         fabbrica.controllo_produzione(tavoletta)
        else:
            print('Peso non conforme alla produzione')
        
    elif prodotto=='3':
        c=False
        densità=float(input('densità del prodotto()cifra compresa tra 0 e 1'))
        caldo=input('Calda? s n')
        if caldo=='s':
            c=True
        ciocco_calda=Calda(densità,caldo)
        nome='cioccolata calda'
        fabbrica.is_producing(nome)
        fabbrica.controllo_produzione(ciocco_calda)
    else:
        print('Scelta non valida')

