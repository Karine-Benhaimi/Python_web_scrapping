import scrapy
import json


#pour lancer le script, dans le terminal écrit:  scrapy runspider one_client.py
# la commande par défault: scrapy runspider le_nom_de_ton_script.py
num_client = input("Entrez le numéro du client à afficher (entre 1 et 73) :")

class ListOfProduct(scrapy.Spider):

    #nom du spider
    name = "Listspider"

    if (int(num_client)>73 or (int(num_client)<1)):
        print("le client n'existe pas !")

    #l'url du site qu'on cherche à scraper
    list_urls = [['https://615f5fb4f7254d0017068109.mockapi.io/api/v1/customers/1'],['https://615f5fb4f7254d0017068109.mockapi.io/api/v1/customers/2'],['https://615f5fb4f7254d0017068109.mockapi.io/api/v1/customers/3'],['https://615f5fb4f7254d0017068109.mockapi.io/api/v1/customers/4'],['https://615f5fb4f7254d0017068109.mockapi.io/api/v1/customers/5'],['https://615f5fb4f7254d0017068109.mockapi.io/api/v1/customers/6'],['https://615f5fb4f7254d0017068109.mockapi.io/api/v1/customers/7'],['https://615f5fb4f7254d0017068109.mockapi.io/api/v1/customers/8'],['https://615f5fb4f7254d0017068109.mockapi.io/api/v1/customers/9'],['https://615f5fb4f7254d0017068109.mockapi.io/api/v1/customers/10']]
    start_urls = list_urls[int(num_client)-1]

    def parse(self, response):

        #on récupère toute les données qui sont dans la balise body sous forme d'un string
        client_with_tags = response.css('body')

        #on remplace les balise par une chaine vide '' pour avoir des données bien nettoyées
        client_str = client_with_tags.get().replace('</p></body>', '').replace('<body><p>', '')

        #on transforme la liste qui contient des dictionnaires sous forme de string en un objet python de list de dictionnaires
        client = json.loads(client_str)
        print("**************** affichage du clien numéro ",num_client,"**************************")
        print(client)
