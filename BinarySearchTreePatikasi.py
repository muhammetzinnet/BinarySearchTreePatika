class Ikladim:
    def __init__(self, key):
        self.sol = None
        self.sag = None
        self.deger = key



def ekle(asil, key):
    if asil is None:
        return Ikladim(key)
    else:
        if asil.deger == key:
            return asil
        elif asil.deger < key:
            asil.sag = ekle(asil.sag, key)
        else:
            asil.sol = ekle(asil.sol, key)
    return asil




def sirala(asil):
    if asil:
        sirala(asil.sol)
        print(asil.deger)
        sirala(asil.sag)


liste = [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]

br = Ikladim(6)
br = ekle(br,5)
br = ekle(br,1)
br = ekle(br,8)
br = ekle(br,3)
br = ekle(br,0)
br = ekle(br,9)
br = ekle(br,4)
br = ekle(br,2)

print(sirala(br))
