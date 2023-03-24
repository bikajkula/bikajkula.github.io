import random
import time
import sort as s
import search as se
'''
    Generate random list of num_of_elements unique elements.
    Element value is in range [min, max)
'''
def random_list (min, max, num_of_elements):
    list = random.sample(range(min, max), num_of_elements)
    return list


'''
    Print elements in list L
'''
def print_list(L):
    print("List: ", L)


l1 = random_list(0, 100000, 10)      # create list of 10 elements where min element value is 0, and max 19
l2 = random_list(0, 100000, 100)
l3 = random_list(0, 100000, 1000)
l4 = random_list(0, 100000, 10000)
l5 = random_list(0, 100000, 100000)

print_list(l1)

# Measure execution time:
# float value in seconds: time.perf_counter()
# integer value in nanoseconds: time.perf_counter_ns()

start_time = time.perf_counter()
# do some processing...

#l1= s.bubble(l1)

#s.merge(l1)

s.quick(l1,0,len(l1)-1)

end_time = time.perf_counter()

print('Execution time is', end_time-start_time)

print_list(l1)

#print('Pretraga:')
#print('Unesite zeljeni element')
#x = input()

'''

start_time = time.perf_counter()
d = se.linear(l1, int(x))
end_time = time.perf_counter()

for x in d:
        print('"',x,'"', "  : ",d[x])



l = se.binary(l1, int(x))
print(l)
print('Execution time is', end_time-start_time)

'''

def bucketSort(array):
    bucket = []

    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


array = [.42, .32, .33, .52, .37, .47, .51]
print("Sorted Array in descending order is")
print(bucketSort(array))

'''

'''


def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)

'''

'''

>> l = []
>> l = [1, 2, ‘a’, “b”]
• Liste se mogu menjati – mutable su
>> l[1] = 5
• Funkcije za rad sa listom:
– len(listname) # vraća dužinu prosleđene liste
– append(value) # dodaje novi element na kraj liste
– insert(index, value) # dodaje novi element
– remove(value) # briše element value iz liste
– del l[index] # briše element sa indeksom index
– clear() # briše sve elemente iz liste


'''

'''

Kolekcija koja sadrži parove tipa ključ:vrednost, gde se ključ koristi za
indeksiranje vrednosti
• Ključevi mogu biti svi tipovi koji se ne mogu menjati (immutable)
>> d = {}
>> d = {“key1” : 1, “key2” : 2}
• Rečnik se može menjati – mutable je
>> d[“key1”] = 5
• Rad sa rečnikom:
– d[“key3”] = 3 # dodavanje novog elementa
– del d[“key1”] # brisanje elementa
– list(d) # vraća listu svih ključeva u rečniku

'''


'''


Torka
• Kolekcija koja sadrži podatke tipa n-torke
>> t = ((),)
>> t = (‘a’, 2, 3)
>> t = ‘a’, 2, 3
• Torka se ne može menjati – immutable je

Napisati program koji u listu smešta četiri TORKE
formata (integer, float, string) i ispisuje ih, nakon čega
briše prvu torku koja je ubačena u listu;

'''

'''


Skup
• Kolekcija koja ne sadrži duplikate
>> s = set()
>> s = {1, 2, 2, 3, 4, 5}
• Skup se može menjati – mutable je
• Podržava matematičke operacije za rad sa skupovima:
– a = {1, 2, 3}
– b = {1, 4, 5}
– a – b # sve što je u a, a nije u b
– a | b # sve što je u a ili b ili u oba
– a & b # sve što je u a i u b
– a ^ b # sve što je u a i b, ali nije u oba


import random

def prvi(x):
    zbir =0
    i = 0
    while zbir<x:
        zbir+=i
        i+=1
    return zbir,i-1

def fakt(x):

    f = 1
    while x>0:
        f*=x
        x-=1

    return f

def pros():
    d = {}
    provera = 1
    temp = 0
    indeks = 1
    suma=0
    while provera>0:

        print('Temperatura za ',indeks,'dan je :')
        temp = input()

        if temp.isdigit():
            provera=1
            d[indeks] = temp
            suma+=int(temp)
        else:
            provera=0

        indeks+=1

    suma = suma/(indeks-2)

    print('Prosecna temperatura je ',suma)
    print(d)

def cetvrti():
    broj = random.randint(1,100)

    print('Unesite vas broj:')
    x = input()
    x=int(x)

    pokusaji = 1
    while x!=broj:
        if x>broj:
            print('Pokusajte sa manjim brojem')
        else:
            print('Pokusajte sa vecim brojem')

        print('Unesite vas broj:')
        x = input()
        x=int(x)

        pokusaji+=1

    print('Brao buraz uspeo si iz ',pokusaji,' puta')

def peti():

    tacni = 0
    netacni = 0
    provera = 1
    while provera>0:
        sab1 = random.randint(10,100)
        sab2 = random.randint(10, 100)

        zbir = sab1+sab2

        print(sab1,' + ',sab2,' = ')
        x=input()

        if x.isdigit():

            x=int(x)

            if x == zbir:
                print('TACNO!')
                tacni+=1
            else:
                print('NETACNO!')
                netacni+=1
        else:
            provera = 0

    print('tacni :',tacni,'   , netacni: ',netacni, ' , procenat uspesnosti je :', (tacni/(tacni+netacni))*100,' %')

def randomList(N):
    l = []

    i=0

    while i<N:

        temp = random.randint(1,500)
        l.append(temp)
        i+=1

    return l

def divisibleBy():

    print('Duzina niza:')
    duzina = input()
    duzina = int(duzina)
    l = randomList(duzina)
    ln = []
    print("Broj X:")
    X = input()

    X=int(X)

    for x in l:
        if x%X ==0:
            ln.append(x)

    print(l)
    print('medzik')
    print(ln)


def delioc():
    print("Broj X:")
    X = input()

    X = int(X)
    l = []

    for i in range(1,X+1):
        if X%i ==0:
            l.append(i)

    print(l)

def ChooseNumbers():

    k = False
    i=0
    while k == False:
        x1 = random.randint(0,100)
        x2 = random.randint(0, 100)
        x3 = random.randint(0, 100)

        if x1==x2==x3:
            k=True

            print(x1,x2,x3)

        i+=1

    print('Bilo je potrebno ',i,' testiranja')


def CalculateSum():
    d = {}

    l = []
    provera = 1

    while provera>0:
        unos = input()

        if unos.isdigit():
            l.append(unos)

        else:
            provera = 0


    for x in l:
        zb = 0
        for y in str(x):
            zb += int(y)
        d[x]= (zb, isPrime(x))


    print(d)

def isPrime(x):
    l = []
    x=int(x)
    for i in range(1, x + 1):
        if x % i == 0:
            l.append(i)

    if len(l) == 2:
        return True
    else:
        return False

def pkm():

    d = {}
    regular = 1
    counter = 0
    izbor = 'neutral'
    while regular > 0:
        igrac = counter%2
        if igrac==0:
            print('Prvi igrac bira:')
            izbor = input()

            if izbor == 'papir' or izbor== 'kamen' or izbor=='makaze':
                d[igrac] = izbor
            elif izbor =='predaja':
                print('Drugi igrac pobedjuje jer se prvi igrac predao')
                regular = 0
            else:
                regular = 0
        else:
            print('Drugi igrac bira:')
            izbor = input()
            if izbor == 'papir' or izbor == 'kamen' or izbor == 'makaze':
                d[igrac] = izbor
            elif izbor =='predaja':
                print('Prvi igrac pobedjuje jer se prvi igrac predao')
                regular = 0
            else:
                regular = 0

        #aj da izvidimo situaciju
        if igrac == 1 and regular == 1:
            if d[0]=='papir':
                if d[1] =='kamen':
                    print('Prvi igrac pobedjuje jer papir pobeduje kamen')
                elif d[1] =='makaze':
                    print('Drugi igrac pobedjuje jer makaze pobedjuju papir')
                else:
                    print('Nereseno')
            elif d[0]=='kamen':
                if d[1] =='kamen':
                    print('Nereseno')
                elif d[1] =='makaze':
                    print('Prvi igrac pobedjuje jer kamen pobedjuje makaze')
                else:
                    print('Drugi igrac pobedjuje jer papir pobedjuje kamen')
            else:
                if d[1] =='kamen':
                    print('Drugi igrac pobedjuje jer kamen pobedjuje makaze')
                elif d[1] =='makaze':
                    print('Nereseno')
                else:
                    print('Prvi igrac pobedjuje jer makaze pobedjuju papir')

        counter+=1


def paskal(h):

    i = 0
    t=[]

    for i in range(h):
        t.append([])

    for i in range(h):
        t[i].append(1)
        if i == 0:
            continue
        for j in range(i-1):
            t[i].append(t[i-1][j]+ t[i-1][j+1])
        t[i].append(1)


    for x in t:
        n = len(x)
        print(' '*(8-n),x)

