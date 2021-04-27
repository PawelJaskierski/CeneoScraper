# CeneoScraper
## Stage 1 - extraction of all componetnts for single opinion 
1. extraction of single web page content
2. analysis of single structure

|Component|CSS selector|Variable name|Data type|
|---------|------------|-------------|---------|
|Opinion|div.js__product_review|opinion|dict|
|Opinion id|["data-entry-id"]|opinion_id|str|
|Author|span.user-post__author-name|author|str|
|Recomandation|span.user-post__author-recomendation > em|recommendation|bool|
|Star rating|span.user-post__score-count|stars|float|
|Verfication|div.review-pz|verified|str|
|Post date|span.user-post__published > time:nth-child(1)["datetime"]|post_date|str|
|Purchase date|span.user-post__published > time:nth-child(2)["datetime"]|purchase_date|str|
|Usefulness count|span[id^="votes-yes"]|usefulness|int|
|Uselessness count|span[id^="votes-no"]|uselessness|int|
|Content|div.user-post__text|content|str|
|Advantages|div.review-feature__col:has(> div[class$="positives"]) > div.review-feature__item|pros|list(str)|
|Disadvantages|div.review-feature__col:has(> div[class$="negatives"]) > div.review-feature__item|cons|list(str)|
3. extraction of single opinion  components
4. transformation of extracted data to given data types

## Stage 2 - extractioin of all opnions from single page
1. definition of dictionary to store all components of single opinion
2. definition od list for opinions' dictionaries storing 
3. implemetation of loop traversing through all opinions from single page 

## Stage 3 - extraction on all opinions 
1. implementation of loop traversing through consecutive pages with opinions 
2. loading extracted opinions to .json file
3. parametrization of product id and reading product id from standard input

## Stage 4 - code refactoring 
1. implementation of component extraction function
2. using dictionary with components selctors and comprehension for single opinion represnatation

## Stage 5 - statistical analysis of extracted opinion
1. displaying listo of products for wchich opinions have been extracted
2. 

## Stage 6 - drawing charts based on given data