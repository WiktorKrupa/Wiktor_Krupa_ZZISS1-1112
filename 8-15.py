import json
Student ={
    "name" :'Wiktor','birth' : '11.05.03',
    'married' : 'False', 'phone':{'mobile':8798, 'landline':98789}
    }
file = open('stud.json','w')
file.write(json.dumps(Student, indent = 4))

file.close()