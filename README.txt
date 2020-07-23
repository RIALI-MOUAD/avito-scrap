#MOUAD RIALI

*Bibliotheques a avoir*
    -bs4
    -requests
    -scrapy
    -pandas
    -matplotlib
    -seaborn
    -geopy
    -plotly
    -numpy
    -wordcloud

*Description*

Ce projet a pour but de collecter des differentes donnees a partir de site "http//:avito.ma"
ainsi de les presenter sous formes des graphes,des maps,des Wordcloud,Pie chart ....
pour la premiere partie de projet -la collection de donnees- j'utilise la bibliotheque "Scrapy"
en faisant appel a "bs4" pour faire des specifiques objectifs.Alors je cree 3 "Spiders" :
      ->la premiere c'est:"avito_categ.py",qui retourne des database par categories(produit,ville,prix,vues,image)
      ->la deuxieme c'est:"avito_spider.py",parlaquelle j'essaie de 'parse' avito dans une seule fois 
      ->la troisieme c'est:"avito_contact.py",a l'aide des url collecter par la deuxieme spider,j'reussit a collecter 
                          les coordonnees(nom,num de tel,adresse...)

Apres la collection des donnes j'ai pu avoir les bases csv suivantes:
      ->avito_big_%.csv(par categorie)
      ->avito_cat.csv(general scraping)
      ->avito_contact.csv(contacts)
Ensuite,a l'aide de bibliotheque plotly et d'autres,j'ai pu finaliser mon projet par presenter les donnees sous forme de graphes,pie chart,wordcloud et une carte de positionnement a l'aide de geopy:
      ->perso_staff.ipynb
      ->avito_categorie.ipynb
      ->avito_general.ipynb
      