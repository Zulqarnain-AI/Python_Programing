dctry={
    'id':1,
    'name':'ali',
    'age':23,
    'address':'XYZ'
}

print(f'length of dictionary: {len(dctry)}')

print(f'get method of dictionary: {dctry.get("name",None)}')

print(f'keys method of dictionary: {dctry.keys()}')

print(f'values method of dictionary: {dctry.values()}')

print(f'items method of dictionary: {dctry.items()}')

dctry.pop("name")
print(f'pop method of dictionary: {dctry}')

print(f'popitem method of dictionary: {dctry.popitem()}')

dctry.update({"name":"qasim"})
print(f'update method of dictionary: {dctry}')

dctry.clear()
print(f'clear method of dictionary: {dctry}')
