import json
from collections import Counter

# data = {1: 
#         {'Имя': 'СТАС',
#         'хобби': ('игры','спорт', 'днд'),
#         'возраст':20,
#         'жим лежа':50,
#         'в отношениях': False            
#     },
#     2: 
#         {'Имя': 'Дима',
#             'хобби': ('игры','чтение', 'днд'),
#             'возраст':20,
#             'жим лежа':0,
#             'в отношениях': True            
#     },
#     3: 
#         {'Имя': 'Славик',
#             'хобби': ('игры','чтение','политика'),
#             'возраст':18,
#             'жим лежа':0,
#             'в отношениях': False            
#     },
#     4: 
#         {'Имя': 'Андрей',
#             'хобби': ('игры','спорт', 'чтение'),
#             'возраст':18,
#             'жим лежа':0,
#             'в отношениях': False            
#     }
# }

# with open('data.json', 'w', encoding="utf-8") as file:
#     json.dump(data, file, indent=4, ensure_ascii=False)
with open('data.json', 'r', encoding="utf-8") as json_file:
    json_dict = json.load(json_file)  

mas = []
mas_i = []
for i, l in json_dict.items():
    mas_i.append(i)
    mas.append(l['кох'])
# хобби
# print(dict(zip(mas_i, mas)))
# print(sum(mas, []))
    
# popular_hobbi = sum(mas, [])
# print(Counter(popular_hobbi).most_common(3))
    
# возраст
# print(sum(mas) // len(mas))
    
# жим лежа 
print(sum(mas) // len(mas))

# кох

print(sum(mas) // len(mas))
