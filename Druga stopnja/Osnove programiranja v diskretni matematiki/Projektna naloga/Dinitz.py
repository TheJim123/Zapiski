import math
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

#Priredimo razširjene sezname sosedov tako, da vsebujejo še podatek o uteži na povezavi
class Element:
    def __init__(self, vi = -1, vj = -1, c=None, f=None, p = None, n = None, s=None):
        self.vi = vi # Začetno krajišče
        self.vj = vj # Končno krajišče
        self.c = c # Kapaciteta povezave
        self.f = f # Pretok povezave
        self.p = p # Predhodnik v seznamu sosedov vi
        self.n = n # Nadlednjik v seznamu sosedov vi
        self.s = s # Sorodna povezava, ki gre iz vj v vi, če obstaja

    def izpisi(self):
        print("[({},{}),c={},f={},{},{},{}]".format(self.vi, self.vj,
                                        "none" if self.c == None else "{}".format(self.c),
                                        "none" if self.f == None else "{}".format(self.f),
                                        "none" if self.p == None else "[{}, {}]".format(self.p.vi, self.p.vj),
                                        "none" if self.n == None else "[{}, {}]".format(self.n.vi, self.n.vj),
                                        "none" if self.s == None else "[{}, {}]".format(self.s.vi, self.s.vj)))

# Naj bo H poljuben končen povezan usmerjen utežen graf in izberimo poljubni različni vozlišči s in t. Naj bo P(s, t) množica vseh vozlišč na vseh (s, t)-poteh v G
# Naj bo G povezan usmerjen utežen podgraf H induciran z neko podmnožico P(s, t) (G je torej sestavljen iz nekega nabora (s, t)-poti). Naše omrežje N je potem (V(G), E(G), s, t, c(G)), kjer so c(G) uteži grafa H zožene na G

#Omrežje N = (V, E, s, t, c) bo v datoteki (matriki C) zapisano na naslednji način
        # s = 0, t = (n-1) (|V| = n)
        # c_ij = 0 če v grafu ni povezave med vozliščema vi in vj
        # c_ij = c(vi, vj) kapaciteta povezave med vi in vj

# Dodatno v vse funkcije vstavljamo omrežja, ki nimajo "odvečnih" vozlišč in povezav na njih, torej "oklestimo" vse "slepe ulice".

#Vse funkcije na razširjenih seznamih sosedov iz vaj priredimo, da delujejo za usmerjene grafe (torej da ne predpostavijo, da za vsako povezavo od vi do vj obstaja recipročna povezava od vj do vi)

def preberi(str):
    f = open(str, 'r')
    graf = []
    C = []
    n = int(f.readline()) #Zapiše število vozlišč
    #Najprej bomo sestavili matriko, ker bo na matriki lažje dostopati do posameznih elementov
    a = [line.strip().split(" ") for line in f] #Vrstice matrike
    for i in range(n): #V graf dodamo prazne sezname sosedov in pripravimo matriko C
        graf.append([])
        C.append([int(j) for j in a[i]])
    for i in range(n):
        for j in range(i, n): #Da se ne ponavljamo, ker gledamo stvari simetrično
            if C[i][j] > 0:
                el1 = Element(i, j, C[i][j], 0)
                if graf[i] == []:
                    graf[i] = el1
                else:
                    graf[i].p = el1
                    el1.n = graf[i]
                    graf[i] = el1
                if C[j][i] > 0:
                    el2 = Element(j, i, C[j][i], 0)
                    #Spremenimo soseda
                    el1.s = el2
                    el2.s = el1
                    #Preverimo, če v seznamu že imamo kako polje
                    if graf[j] == []:
                        graf[j] = el2
                    else:
                        graf[j].p = el2
                        el2.n = graf[j]
                        graf[j] = el2
            else: #C[i][j] == 0
                if C[j][i] > 0:
                    el1 = Element(j, i, C[j][i], 0)
                    #Preverimo, če v seznamu že imamo kako polje
                    if graf[j] == []:
                        graf[j] = el1
                    else:
                        graf[j].p = el1
                        el1.n = graf[j]
                        graf[j] = el1            
    return graf

def narisi(graf):
    G = nx.DiGraph()
    for i in range(len(graf)):
        el = graf[i]
        if el != []:
            while el != None:
                G.add_edge(str(el.vi), str(el.vj), weight=el.c)
                el = el.n
    layout = nx.spring_layout(G)
    nx.draw(G, layout, with_labels=True)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, layout, edge_labels)
    plt.show()

def izpisiGraf(graf):
    for i in graf:
        el = i
        if el != []:
            while el != None:
                el.izpisi()
                el = el.n

def obstajaPovezava(graf, a, b):
    """Funkcija prejme graf predstavljen z razširjenimi seznami in dve vozlišči ter pove, če sta vozlišči v grafu povezani"""
    if a< 0 or b < 0 or a>= len(graf) or b >= len(graf):
        return False
    if graf[a] == [] or graf[b] == []:
            return False
    el = graf[a]
    while el != None:
        if el.vj == b: #V omrežju bo vedno el.c > 0, zato tukaj tega ne bomo preverjali
            return True
        el = el.n
    return False

def sosedi(graf, a):
    """Funkcija prejme graf podan z razširjenimi seznami sosedov in vozlišče ter vrne ločen seznam sosedov v grafu."""
    sosed = [[], []]
    for i in range(len(graf)): #sosedi po povezavah, ki se končajo v a
            el = graf[i]
            if el != []:
                while el != None:
                    if el.vi != a:
                        if el.vj == a:
                            sosed[0].append(el.vi)
                    else: # i == a
                        sosed[1].append(el.vj)
                    el = el.n
    return sosed

def dodajPovezavo(graf, a, b, c=1, f=0):
    """Doda v graf usmerjeno povezavo od a do b s kapaciteto c in pretokom f"""
    sosa = sosedi(graf, a)
    sosb = sosedi(graf, b)
    if b in sosa[1]:
        print("Vozlišči sta že povezani!")
    else:
        el1 = Element(a, b, c, f)
        if a in sosb[1]: #Če že obstaja povezava od b do a, označimo sorodnost
            el2 = graf[b]
            while el2 != None:
                if el2.vj == a:
                    el2.s = el1
                    el1.s = el2
                el2 = el2.n
        if graf[a] == []:
            graf[a] = el1
        else:
            graf[a].p = el1
            el1.n = graf[a]
            graf[a] = el1

def odstraniPovezavo(graf, a, b):
    """Funkcija sprejme graf in par vozlišč in iz grafa odstrani povezavo od vozlišča a do vozlišča b, če obstaja"""
    el1 = graf[a]
    #Iz seznamov odstranimo tistega, ki predstavlja povezavo med a in b
    while el1 != None:
        if el1.vj == b:
            el1.izpisi()
            # Uredimo kazalce za povezavo za a
            el1.n.p = el1.p
            el1.p.n = el1.n
            #odstranimo polja
            graf.remove(el1)
            return graf
        el1 = el1.n
    print("Vozlišči nista povezani!")

def OdstraniPovezave(graf, a):
    """Sprejme graf in vozlišče in iz grafa odstrani vse povezave, ki imajo kako krajišče v a."""
    el = graf[a]
    sos = sosedi(graf, a)
    for vi in sos[0]: #Odstranimo povezave, ki se končajo v a
        odstraniPovezavo(graf, vi, a)
    for vj in sos[1]: #Odstranimo povezave, ki se začnejo v a
        odstraniPovezavo(graf, a, vj)
    #Toda vozlišča a ne odstranimo
    return graf

def Uredi(graf):
    """Uredi povezave grafa tako, da naraščajo glede na končno vozlišče."""
    new = [[] for i in range(len(graf))]
    for i in range(len(graf)):
        [_, S] = sosedi(graf, i)
        S.sort()
        while S != []:
            el = graf[i]
            if el != []:
                while el != None:
                    if el.vj == S[-1]:
                        dodajPovezavo(new, el.vi, el.vj, el.c, el.f)
                        break
                    el = el.n
            S.pop(-1)
    return new

def Povezave(graf):
    povezave = []
    for i in range(len(graf)):
        el = graf[i]
        if el != []:
            while el != None:
                povezave.append(el)
                el = el.n
    return povezave

#Pretok f bomo zapisali kot seznam vrednosti v enakem vrstnem redu kot seznam, ki nam ga vrne funkcija Povezave (za vse indekse i: povezavi Povezave(graf)[i] pripada pretok f[i])

def rezidual(graf, f=[]):
    """Sprejme omrežje "graf" in pretok "f" ter vrne rezidualno omrežje."""
    SezPov = Povezave(graf) #Sestavimo seznam povezav grafa
    NovPov = [] #Seznam novih povezav, ki jih bomo dodali na koncu
    RezOm = [[] for i in range(len(graf))] #Naredimo kopijo začetnega omrežja
    for i in range(len(graf)):
        el = graf[i]
        while el != None and el != []:
            if f == []: #Če f ni posebej podan, vzamemo trenutnega (privzet pretok je ničelni)
                if el.f < el.c:
                    dodajPovezavo(RezOm, el.vi, el.vj, el.c - el.f)
                if el.f > 0:
                    NovPov.append([el.vj, el.vi, el.f]) #Dodamo obratno povezavo s kapaciteto el.f v seznam
            else:
                j = SezPov.index(el) #Določimo kje se nahaja povezava v seznamu povezav
                if f[j] < el.c:
                    dodajPovezavo(RezOm, el.vi, el.vj, el.c - f[j]) #Dodamo vse povezave iz vhodnega grafa s posodobljenimi kapacitetami
                if 0 < f[j]:
                    NovPov.append([el.vj, el.vi, f[j]]) #Dodamo obratno povezavo s kapaciteto f[j] v seznam
            el = el.n
    for p in NovPov: #Dodamo vse nove povezave
        dodajPovezavo(RezOm, p[0], p[1], p[2])
    return RezOm

def BFS(v, graf):
    """Sprejme vozlišče grafa G in predstavitev G s seznamom sosedov ter vrne označitev l(u) = d(v, u)"""
    V = [v]
    #Sestavimo začetni l
    l = []
    for i in range(len(graf)):
        l.append(-1)
    l[v] = 0
    while V != []:
        u = V.pop(0)
        sos = sosedi(graf, u)
        for j in sos[1]:
            #Če je l[j] nedoločen in je kapaciteta povezave od u do j večja od 0, določimo l[j]
            if l[j] == -1:
                el = graf[u]
                if el != []:
                    while el != None:
                        if el.vj == j and el.c > 0:
                            l[j] = l[u] + 1
                            V.append(j)
                            break
                        el = el.n
    return l

def plasti(rezom):
    """Dano rezidualno omrežje rezom razbije na plasti s pomočjo BFS algoritma. Dodatno, zadnje vozlišče, če je doseženo, da v lastno plast."""
    bfs = BFS(0, rezom)
    t = len(rezom)-1
    if bfs[t] == -1: #Če BFS ne doseže t
        return "Pretok f je maksimalen"
    else: #dosežemo t -> bfs[t] != -1
        l = max(bfs)
        P = [[] for _ in range(l+1)]
        for i in range(t):
            if bfs[i] != -1:
                if bfs[i] != bfs[t]: #Če je i označen in nima enake oznake kot t, ga damo v primerno plast
                    P[bfs[i]].append(i)
        P[-1].append(t)
    return P

def stratificiraj(rezom):
    """S pomočjo danega rezidualnega omrežja rezom sestavi stratificirano omrežje stratom."""
    # Vozlišča so V = sum(plasti(rezom), [])
    # Povezave so ravno povezave navzdol (torej se lahko premaknemo le v sloj z večjim indeksom)
    # kapacitete ne spremenimo
    stratom = [[] for i in range(len(rezom))]
    P = plasti(rezom)
    t = len(rezom)-1
    if P != "Pretok f je maksimalen":
        for i in range(len(rezom)):
            el = rezom[i]
            for j in range(len(P)-1):
                if i in P[j] and el != []: #Če vozlišče je označeno preverimo, če je krajišče kakih povezav navzdol
                    while el != None:
                        if el.vj in P[j+1]: #Vsako najdeno povezavo navzdol dodamo stratificiranemu omrežju
                            dodajPovezavo(stratom, el.vi, el.vj, el.c, el.f)
                        el = el.n
    return stratom

def NajdiPot(stratom, o=[]):
    """Poskusi najti pot od izvora do ponora stratificiranega omrežja po povezavah, ki še niso bile blokirane (o je seznam blokiranih povezav). Vrne par [S, o], kjer je o posodobljen seznam blokiranih povezav, S pa bodisi seznam parov (p, p.vj), ki sestavljajo (s, t)- pot, ali pa [], če v omrežju več ni možno najti poti."""
    t = len(stratom)-1
    S = [(None, 0)]
    while S != [] and S[-1][1] != t:
        T = S.copy() #Naredimo kopijo za kasnejšo primerjavo
        u = S[-1]
        v = u[1] #Koncno vozlisce povezave v paru
        sosv = sosedi(stratom, v)
        #print("Sosedi od {}:{}".format(v, sosv))
        if (sosv[1] != []): #Če obstajajo povezave iz v
            el = stratom[v]
            while el != None:
                if el not in o: #in če najdemo med temi povezavami kako, ki še ni bila blokirana, jo dodamo v sklad
                    #el.izpisi()
                    S.append((el, el.vj))
                    break
                el = el.n
        if S == T: #Če nismo dodali nobenega para, u odstranimo iz sklada
            if u[0] != None:
                o.append(u[0])
            S.pop(-1)
    return [S, o]

def povecajpretok(stratom, P, o):
    """Funkcija sprejme stratificirano omrežje stratom, seznam P v katerega je zapisana neka (s,t)-pot in seznam blokiranih povezav o ter vrne poveča pretok f (po dani poti) v omrežju in vrne posodobljen seznam blokiranih povezav v katerega da vse povezave, ki imajo zapolnjeno kapaciteto."""
    S = []
    d = -1
    while P[-1] != (None, 0):
        (e, v) = P.pop(-1)
        # Poiščemo za največ koliko lahko povečamo pretok -> d
        if d == -1:
            d = e.c - e.f
        else:
            d = min([d, e.c - e.f])
        S.append(e)
    while S != []:
        p = S.pop(-1)
        p.f += d #Povečamo pretok za d
        if p.f == p.c:
            o.append(p)
    return o

def maksimalenpretok(stratom):
    """Funkcija v stratificiranem omrežju stratom poišče maksimalen pretok."""
    o = [] #Seznam blokiranih povezav na začetku
    # pretok na vsaki povezavi je na začetku 0
    [P, _] = NajdiPot(stratom)
    while P != []:
        o = povecajpretok(stratom, P, o)
        [P, o] = NajdiPot(stratom, o)
    return stratom

def DinitzAlg(graf):
    """Sprejme omrežje graf in vrne maksimalen pretok po njem."""
    rezom = rezidual(graf)
    while plasti(rezom) != "Pretok f je maksimalen": #Dokler nimamo maksimalnega pretoka
        stratom = maksimalenpretok(stratificiraj(rezom)) #Sestavimo stratificirano omrežje in določimo njegov maksimalen pretok
        for i in range(len(stratom)):
            p = stratom[i]
            if p != []:
                while p != None:
                    #Poiščemo povezave v omrežju graf
                    for j in range(len(graf)):
                        q = graf[j]
                        if q != []:
                            while q != None:
                                #Če je povezava p v stratom istoležna in enako usmerjena kot povezava q v graf pretok na q povečamo za pretok na p (torej q.f += p.f)
                                if q.vi == p.vi and q.vj == p.vj:
                                    q.f += p.f
                                #Če je povezava p v stratom istoležna in obratno usmerjena kot povezava q v graf pretok na q zmanjšamo za pretok na p (torej q.f -= p.f)
                                elif q.vi == p.vj and q.vj == p.vi:
                                    q.f -= p.f
                                #q.izpisi()
                                q = q.n
                    #p.izpisi()
                    p = p.n
        rezom = rezidual(graf) #Ponovno sestavimo rezidualno omrežje s posodobljenim pretokom
    F = 0 #Poračunamo skupni pretok f v omrežju
    for e in Povezave(graf):
        if e.vj == len(graf)-1: # Če je končno vozlišče t
            F += e.f
    return [Povezave(graf), F]
    
            
grf1 = Uredi(preberi("primer.txt"))
grf2 = Uredi(preberi("primer2.txt"))
grf3 = Uredi(preberi("primer3.txt"))
