import requests
import re
import json
from bs4 import BeautifulSoup

respons = requests.get("https://www.ceneo.pl/91715703#tab=reviews")

page_dom = BeautifulSoup(respons.text,'html.parser')


opinions = page_dom.select("div.js_product-review")
all_opinions=[]
for opinion in opinions:
    opinon_id = opinion["data-entry-id"]
    author = opinion.select("span.user-post__author-name").pop(0).get_text().strip()
    try:
        recomendation=opinion.select("span.user-post__author-recomendation > em").pop(0).get_text().strip()
        recomendation = True if recomendation=="Polecam" else False
    except IndexError:
        recomendation = None
    stars=opinion.select("span.user-post__score-count").pop(0).get_text().strip()
    stars = float(stars.split("/")[0].replace(",","."))
    try:
        verified=bool(opinion.select("div.review-pz").pop(0).get_text().strip())
    except IndexError:
        verified = False
    post_date=opinion.select("span.user-post__published > time:nth-child(1)").pop(0)["datetime"].strip()
    try:
        purchase_date=opinion.select("span.user-post__published > time:nth-child(2)").pop(0)["datetime"].strip()
    except IndexError:
        purchase_date = None
    usefulness=int(opinion.select("span[id^=\"votes-yes\"]").pop(0).get_text().strip())
    uselessness=int(opinion.select("span[id^=\"votes-no\"]").pop(0).get_text().strip())
    content=opinion.select("div.user-post__text").pop(0).get_text().strip()
    content = re.sub("\\s"," ",content)
    pros=opinion.select("div.review-feature__col:has(> div[class$=\"positives\"]) > div.review-feature__item")
    pros =[item.get_text().strip() for item in pros]
    cons=opinion.select("div.review-feature__col:has(> div[class$=\"negatives\"]) > div.review-feature__item")
    cons =[item.get_text().strip() for item in cons]
    single_opinon={
        "opinon_id":opinon_id,
        "author":author,
        "recomendation":recomendation,
        "stars":stars,
        "content":content,
        "pros":pros,
        "cons":cons,
        "verified":verified,
        "post_date":post_date,
        "purchase_date":purchase_date,
        "usefulness":usefulness,
        "uselessness":uselessness
    }

    all_opinions.append(single_opinon)
print(json.dumps(all_opinions,ensure_ascii=False, indent=4))
#print(opinon_id, author, recomendation, stars, verified, content)
#print (author)
