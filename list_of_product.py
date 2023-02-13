import scrapy
import ast


#pour lancer le script, dans le terminal écrit:  scrapy runspider list_of_product.py
# la commande par défault: scrapy runspider le_nom_de_ton_script.py

class ListOfProduct(scrapy.Spider):

    #nom du spider
    name = "Listspider"

    #l'url du site qu'on cherche à scraper
    start_urls = ['https://615f5fb4f7254d0017068109.mockapi.io/api/v1/products/']

    def parse(self, response):

        #on récupère toute les données qui sont dans la balise body sous forme d'un string
        lis_of_products_with_tags = response.css('body')

        #on remplace les balise par une chaine vide '' pour avoir des données bien nettoyées
        list_of_products_str = lis_of_products_with_tags.get().replace('</p></body>', '').replace('<body><p>', '')

        #on transforme la liste qui contient des dictionnaires sous forme de string en un objet python de list de dictionnaires
        list_of_product = ast.literal_eval(list_of_products_str)


        cpt =1
        for product in list_of_product:

            #afficher les produits, exemple ci-dessous de product
            '''{'createdAt': '2022-07-11T14:01:29.200Z', 'name': 'Annette Sipes', 'details': {'price': '338.00', 'description': 'Ergonomic executive chair upholstered 
                in bonded black leather and PVC padded seat and back for all-day comfort and support', 'color': 'gold'}, 'stock': 71136, 'id': '99'}'''
            print("produit numéro :", cpt)
            print(product)
            cpt +=1
            #si on veut par exemple afficher le nom du produit
            #print(product["name"])
            # si on veut par exemple afficher le prix du produit
            #print(product["details"]["price"])

























