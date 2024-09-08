import json
 
class Model:
   title = '1'
   text = '2'
   author = '3'

   def save(self):
        dct = {n: str(s) for n, s in vars(Model).items()}
        with open('file_json.txt', 'w', encoding='utf-8') as fout:
            json.dump(dct, fout)

 
x = Model()
x.save()

print(dir(x))
print()
print(list(filter(lambda x: not x.startswith('_'), dir(Model))))

