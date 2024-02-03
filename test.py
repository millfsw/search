import sys
from io import BytesIO
import requests
from PIL import Image
import geocoder

toponym_to_find = " ".join(sys.argv[1:])
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json",
}
response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    # обработка ошибочной ситуации
    pass

json_response = response.json()
toponym = json_response.get("response").get("GeoObjectCollection").get("featureMember")[0].get("GeoObject")


delta = "0.005"

ll = geocoder.get_ll(toponym)
spn = geocoder.get_spn(toponym)

map_params = {
    "ll": ll,
    "spn": spn,
    "l": "map",
    "pt": ll + ',pm2blywl',
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
print(response.url)

Image.open(BytesIO(response.content)).show()


# py "C:\Users\smila\OneDrive\Рабочий стол\папка\sublime_text\sublime_text\test.py" Череповец Сталеваров 24
