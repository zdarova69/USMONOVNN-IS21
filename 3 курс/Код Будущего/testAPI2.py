from serpapi import GoogleSearch
import os, json

def search_api(a):
  print(f'получено {a}')
  params = {
    "api_key": "",
    "engine": "google",
    "q": a,
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
          print(len(image_result_json), image['original'])
      params["ijn"] = +1
    else:
      image_in_present = False
      print(results['error'])
    if len(image_result_json)  > 100:
      len(image_result_json)
      break

  with open('result.json', 'w') as file:
    json.dump(image_result_json, file)
