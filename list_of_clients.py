#AFFICHER LA LISTE DE TOUS LES CLIENTS
import scrapy
import ast



#ouvrir anaconda terminal ensuite tapper conda activate test0 pour se mettre dans notre environnement ou scrapy est installé
#se mettre dans le dossier Scrapper, utiliser la commande dir au lieu de ls
#pour lancer le script, dans le terminal écrit:  scrapy runspider list_of_clients.py
# la commande par défault: scrapy runspider le_nom_de_ton_script.py

class ListOfClient(scrapy.Spider):

    #nom du spider
    name = "Listspider"

    #l'url du site qu'on cherche à scraper
    start_urls = ['https://615f5fb4f7254d0017068109.mockapi.io/api/v1/customers/']

    def parse(self, response):

        #on récupère toutes les données qui sont dans la balise body sous forme d'un string
        list_of_clients_with_tags = response.css('body')

        #on remplace les balise par une chaine vide '' pour avoir des données bien nettoyées
        list_of_clients_str = list_of_clients_with_tags.get().replace('</p></body>', '').replace('<body><p>', '')

        #on transforme la liste qui contient des dictionnaires sous forme de string en un objet python de list de dictionnaires
        list_of_clients = ast.literal_eval(list_of_clients_str)

        cpt = 1

        for client in list_of_clients:

            #afficher les clients, exemple ci-dessous de product
            '''{{'createdAt': '2022-07-11T15:40:40.388Z', 'name': 'Nichole Bashirian I', 'username': 'Eldridge96', 'firstName': 'Makayla', 'lastName': 'Beier',
                'address': {'postalCode': '01783', 'city': 'Adeleton'}, 'profile': {'firstName': 'Rosina', 'lastName': 'Jacobs'}, 'company': {'companyName': 'Daniel - Turner'}, 'id': '62', 'orders': [{'createdAt': '2022-07-11T22:51:54.292Z', 'id': '62', 'customerId': '62'}]}
'''
            print("****************************************************")
            print("Client numéro: ", cpt)
            print(client)
            print("****************************************************")

            cpt+=1

























