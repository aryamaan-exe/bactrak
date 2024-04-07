import requests, json, base64

url = "https://api.edenai.run/v2/image/generation"

payload = {
    "response_as_dict": True,
    "attributes_as_list": False,
    "show_original_response": False,
    "resolution": "1024x1024",
    "num_images": 4,
    "providers": "openai",
    "fallback_providers": "deepai",
    "text": "A black cat walking on a rainy road"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNGNhZTIzZTQtNjJhMS00Y2VmLTkxMGEtNWIzZTZkZDgyM2IzIiwidHlwZSI6InNhbmRib3hfYXBpX3Rva2VuIn0.ehQ3l8JvrYunvEXM4GF_DXK22XOWdAQ-g2Hb8N3sN-c"
}

response = requests.post(url, json=payload, headers=headers)
res_json = json.loads(response.text)
image_data = res_json['openai']['items'][0]['image']
image_url = res_json['openai']['items'][0]['image_resource_url']
with open(image_data[:10] + '.png', 'wb') as f:
    image_code = base64.b64decode(image_data)
    f.write(image_code)

import requests

url = 
data = {"imageUrl": image_url}

rev_response = requests.post(url, json=data)

if rev_response.ok:
    print(rev_response.json())
else:
    print(rev_response.status_code)


with open('rev.json', 'w') as f:
    json.dump(rev_response.json(), f)

    
