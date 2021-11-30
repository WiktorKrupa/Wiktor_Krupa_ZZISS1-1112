
>>> person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }
>>> person
{'name': 'Marek', 'surname': 'Banach', 'age': 25, 'hobby': ['swimming', 'excursions'], 'married': True, 'phone': {'landline': '123444321', 'mobile': '777888999'}}
>>> person[name]
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'name' is not defined
>>> person"name"]
  File "<pyshell>", line 1
    person"name"]
               ^
SyntaxError: invalid syntax
>>> person["name"]
'Marek'
>>> person[0]
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
KeyError: 0
>>> person['hobby']
['swimming', 'excursions']
>>> person['surname']= 'Nowak'
>>> person
{'name': 'Marek', 'surname': 'Nowak', 'age': 25, 'hobby': ['swimming', 'excursions'], 'married': True, 'phone': {'landline': '123444321', 'mobile': '777888999'}}
>>> person['married']=False
>>> person
{'name': 'Marek', 'surname': 'Nowak', 'age': 25, 'hobby': ['swimming', 'excursions'], 'married': False, 'phone': {'landline': '123444321', 'mobile': '777888999'}}
>>> person['gender']=male
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'male' is not defined
>>> person['married']= not person['married']
>>> person
{'name': 'Marek', 'surname': 'Nowak', 'age': 25, 'hobby': ['swimming', 'excursions'], 'married': True, 'phone': {'landline': '123444321', 'mobile': '777888999'}}
>>> person ['gender']= 'male'
>>> person
{'name': 'Marek', 'surname': 'Nowak', 'age': 25, 'hobby': ['swimming', 'excursions'], 'married': True, 'phone': {'landline': '123444321', 'mobile': '777888999'}, 'gender': 'male'}
>>> person['hobby'].append("bicycle")
>>> person
{'name': 'Marek', 'surname': 'Nowak', 'age': 25, 'hobby': ['swimming', 'excursions', 'bicycle'], 'married': True, 'phone': {'landline': '123444321', 'mobile': '777888999'}, 'gender': 'male'}
>>> person['phone']['work_phone']=313131444
>>> person
{'name': 'Marek', 'surname': 'Nowak', 'age': 25, 'hobby': ['swimming', 'excursions', 'bicycle'], 'married': True, 'phone': {'landline': '123444321', 'mobile': '777888999', 'work_phone': 313131444}, 'gender': 'male'}
