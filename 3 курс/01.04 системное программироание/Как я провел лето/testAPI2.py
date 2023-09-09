from serpapi import GoogleSearch
import json, os

from serpapi import GoogleSearch

params = {
  "api_key": "35ad8f3f0a6df240bab8ad52165ba01f5c004d1a60b70c8552cb0e9c236265ff",
  "engine": "google",
  "q": "black man",
  "tbm": "isch",
  "num": "100",
  'ijn': 0
}

search = GoogleSearch(params)
image_result_json = []
image_in_present = True
while image_in_present:
  results = search.get_dict()

  if 'error' not in results:
    for image in results['images_results']:
      if image['original'] not in image_result_json:
        image_result_json.append(image['original'])
        print(image['original'])
    params["ijn"] = +1
  else:
    image_in_present = False
    print(results['error'])
  if len(image_result_json) == 198:
    len(image_result_json)
    break

with open('image.json', 'w') as file:
  json.dump(image_result_json, file)