import json
import requests


with open('image_white.json') as f:
    templates = json.load(f)

for i,img_link in enumerate(templates):
    print(i)
    if i > 181:
        img_save = requests.get(img_link)
        img_optional = open('nigger_white_man/white_' + str(i) + ".jpg", 'wb')
        img_optional.write(img_save.content)
        img_optional.close()