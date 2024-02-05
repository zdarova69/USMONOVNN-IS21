# import json

# # a = 'играть, нету, 20:00'

# # b = a.split(',')
# # print(len(b))

# # c = ['дело', 'описание', 'дедлайн']

# # g = dict(zip(b,c))

# # data = {1:g}
# # print(data)

# # with open('data_3.json', 'r', encoding="utf-8") as json_file:
# #     json_dict = json.load(json_file)
# #     print(json_dict)

# # with open('data_3.json', 'a', encoding='utf-8') as file:
# #     json.dump(g, file, indent=4, ensure_ascii=False)

# a = '{"дело":"дело", "время":"время"}'

# b = a.split(',')

# data_dict = json.loads(a)
# print(data_dict)
# import json

# data_dict = json.loads('{"name":"Иван Иванов","ids":[1,2,3],"balance":12345}')

import re
text = "Привет, hello123! Как дела? hello Здравст Здар"
text2 = 'Hello'
pattern = r"\b(Прив|Здравст|Здар|Hello|Hi)\w*\b"
pattern2 = r"\bПривет\w*\b"
matches = re.findall(pattern, text, flags=re.IGNORECASE)
print(type(matches))
print(matches)

if len(matches) >= 1:
    print('Привет')