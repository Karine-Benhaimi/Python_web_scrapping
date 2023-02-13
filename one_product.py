#AFFICHER UN PRODUIT SELON SON NUMERO
import scrapy
import json


# la commande par défault: scrapy runspider le_nom_de_ton_script.py
num_product = input("Entrez le numéro du produit à afficher (entre 1 et 100) :")

class OneProduct(scrapy.Spider):

    #nom du spider
    name = "Listspider"

    if (int(num_product)>100 or (int(num_product)<1)):
        print("le client n'existe pas !")

    #l'url du site qu'on cherche à scraper
    start_urls = ['https://615f5fb4f7254d0017068109.mockapi.io/api/v1/products/'+str(num_product)]

    def parse(self, response):

        #on récupère toute les données qui sont dans la balise body sous forme d'un string
        product_with_tags = response.css('body')

        #on remplace les balise par une chaine vide '' pour avoir des données bien nettoyées
        product_str = product_with_tags.get().replace('</p></body>', '').replace('<body><p>', '')

        #on transforme la liste qui contient des dictionnaires sous forme de string en un objet python de list de dictionnaires
        product = json.loads(product_str)
        print("**************** affichage du produit numéro ",num_product,"**************************")
        print(product)
