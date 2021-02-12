my_dict = {'dave':'001','ava':'002','joe':'003'}
print(my_dict)
type(my_dict)

hello = dict()
print(hello)
type(hello)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.get('ava'))

for x in my_dict:
    print(x)

for x,y in my_dict.items():
    print(x,y)