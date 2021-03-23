import requests

respons = requests.get("https://www.ceneo.pl/91715703#tab=reviews")
print(respons.text)