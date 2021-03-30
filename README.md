# CeneoScraper
## Stage 1 - extraction of all componetnts for single opinion 
1. extraction of single web page content
2. analysis of single structure

|Component|CSS selector|Variable name|Data type|
|---------|------------|-------------|---------|
|Opinion|div.user-post__card|opinion||
|Opinion id|["data-entry-id"]|opinion_id||
|Author|span.user-post__author-name|author||
|Recomandation|span.user-post__author-recomendation > em|recommendation||
|Star rating|span.user-post__score-count|stars||
|Verfication|div.review-pz|verified||
|Post date|span.user-post__published > time:nth-child(1)["datetime"]|post_date||
|Purchase date|span.user-post__published > time:nth-child(2)["datetime"]|purchase_date||
|Usefulness count|span[id^="votes-yes"]|usefulness||
|Uselessness count|span[id^="votes-no"]|uselessness||
|Content|div.user-post__text|content||
|Advantages|div.review-feature__col:has(> div[class$="positives"] > div.review-feature__item|pros||
|Disadvantagesdiv.review-feature__col:has(> div[class$="negatives"] > div.review-feature__item|cons||
3. extraction of single opinion 
4. transformation of extracted data to given data types