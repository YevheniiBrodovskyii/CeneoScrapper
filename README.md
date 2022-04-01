# CeneoScrapper

## Struktura opinii w serwisie [ceneo.pl](https://www.ceneo.pl/101052360#tab=reviews)

|Skłądowe opinii|Selector|Nazwa zmiennej|Typ danych|
|---------------|--------|--------------|----------|
|opinia|div.js_product-review|user-post__card|| 
|identyfikator opinii|.js_product-review\[data-entry-id\]|||
|autor opinii|span.user-post__author-name"|||
|rekomendacja autora|span.user-post__author-recomendation > em|||
|liczba gwiazdek|span.user-post__score-count|||
|treść opinii|div.user-post__text|||
|lista zalet|class=|||
|lista wad||||
|dla ilu osób przydatna|button.vote-yes > span|||
|dla ilu osób nieprzydatna|button.vote-no > span|||
|data wystawienia opinii|span.user-post__published > time:nth-child(1)\["datetime"\]|||
|data zakupu produktu|span.user-post__published > time:nth-child(2)\["datetime"\]|||           