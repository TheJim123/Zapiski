import random

def Preberi(str):
    f = open(str, 'r')
    #Če je v datoteki v prvi vrstici podano vozlišče
    n = int(f.readline())
    graf = []
    for line in f:
        a = [int(i) for i in line.strip().split(" ")]
        #Sestavimo seznam sosedov za posamezno vozlišče
        t = []
        for i in range(len(a)):
            if a[i] == 1:
                t.append(i)
        graf.append(t)
    return graf

def BFS(v, graf):
    """Sprejme vozlišče grafa G in predstavitev G s seznamom sosedov ter vrne označitev l(u) = d(v, u)"""
    V = [v-1]
    #Sestavimo začetni l
    l = []
    for i in range(len(graf)):
        l.append(-1)
    l[v-1] = 0
    while V != []:
        u = V.pop(0)
        for j in graf[u]:
            #Če je l[j] nedoločen, ga določimo
            if l[j] == -1:
                l[j] = l[u] + 1
                V.append(j)
    return l

def Stevilokomponent(graf):
    #število komponent je vsaj 1
    k = 1
    # Začnemo s prvim vozliščem, poženemo BFS
    l = BFS(1, graf)
    # seznam nedefiniranih vozlišč
    n = []
    for i in range(len(l)):
        if l[i] == -1:
            n.append(i)

    #Dokler imamo vozlišča, ki nimajo definiranega l
    while n != []:
        n0 = n[0]
        nl = BFS(n0+1, graf)
        for i in range(len(nl)):
            if (i in n) and nl[i] != -1:
                n.remove(i)
        k +=1
    return k


def JeDvodelenBFS(graf):
    """Funkcija sprejme graf in pove, če je dvodelen ali ne."""
    #Spomnimo se: Graf G je dvodelen <=> ne vsebuje povezav povprek
    Dvodelen = True
    for k in range(len(graf)):
        l = BFS(k+1, graf)
        for i in range(len(l)):
            for j in range(len(l)):
                if l[i] == l[j] and i in graf[j]:
                    #Našli smo povezavo povprek
                    Dvodelen = False
    return Dvodelen

# Ker v drevesu velja: st vozlisc - st povezav = 1, bo v gozdu veljalo
# st vozlisc - st povezav = st komponent. To uporabimo v spodnji funkciji

def JeGozdBFS(graf):
    """Funkcija sprejme graf in pove, če je gozd ali ne."""
    n = len(graf) #število vozlišč
    m = 0
    jegozd = False
    for i in graf:
        m+=len(i)
    m = m // 2 #Število povezav
    #print("Število vozlišč:{}".format(n))
    #print("Število povezav:{}".format(m))
    c = Stevilokomponent(graf)
    #print("Število komponent:{}".format(c))
    if n - m == c:
        jegozd = True
    return jegozd

def DFS(graf):
    n = len(graf)
    #Izberemo naključno vozlišče
    r = random.randint(0, n-1)
    #Sestavimo sklad
    S = [r]
    #Seznam obiskanih vozlišč
    o = []
    while S != []:
        u = S.pop(-1)
        if (u not in o) and (u != None):
            print(u)
            o.append(u)
            #Dodamo sosede od u v sklad
            S = graf[u] + S
            
        
        
grf1 = Preberi("primer.txt")
#grf2 = Preberi("primer2.txt")
#grf3 = Preberi("primer3.txt")
#grf4 = Preberi("primer4.txt")
#for i in grf[1]: print(i)
#print(grf1)
#print(BFS(10, grf1))
#print(Stevilokomponent(grf1))
#print(JeDvodelenBFS(grf1))
#print(JeDvodelenBFS(grf2))
#print(JeDvodelenBFS(grf3))
#print(JeDvodelenBFS(grf4))
#print(JeGozdBFS(grf1))
#print(JeGozdBFS(grf2))
#print(JeGozdBFS(grf3))
#print(JeGozdBFS(grf4))
#print(DFS(grf1))
