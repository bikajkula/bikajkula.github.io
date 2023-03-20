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
