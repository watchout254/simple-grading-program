
phone_no = {
    'dan':11,
    'bruh':50,
    'maah':34,
    'rech':45,
    'bruh':60 #does not allow duplicates, the last value assigned is the one that will be printed out
}
print(phone_no)
for i in phone_no.items():
    print(i)
phone_no2=phone_no.copy()
print(phone_no2)
print(len(phone_no))

print(phone_no) #case sensitive
phone_no['maah'] = 67
phone_no['zozaa'] = {1111,2222,3333,4444,5555}
phone_no['dan'] = {'dan home':33333,'dan work':78899}
print(phone_no['dan'] ['dan work'])
print(phone_no.get('maah'))


del phone_no['bruh'] #clear, pop, popitem
print(phone_no)
print(phone_no.keys())
print(phone_no.values())
print(phone_no.items())

data = {
   1: 'Jenny',
   2: 'Ram',
   0: 'Mohan'
}
print(data[0]) #keys are immutable