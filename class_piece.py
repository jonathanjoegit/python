import random
class Piece :
    def tirage_aleatoire(self) :
        return random.randint(0,1)
    def moyenne_tirage(self, n):
        tirage = [ ]
        for i in range (n) :
            tirage.append( self.tirage_aleatoire () )
        s = sum(tirage)
        return s * 1.0 / len(tirage)

p = Piece()
print (p.moyenne_tirage(100))

class PieceTruquee1 (Piece) :
# A vous de jouer !
  
p = PieceTruquee1()
print (p.moyenne_tirage(100))

class PieceTruquee2(Piece):
#  A vous de jouer !

p = PieceTruquee2()
print(p.moyenne_tirage(100))

