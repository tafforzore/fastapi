import requests

# URL de l'API où vous voulez envoyer la requête POST
url = "http://0.0.0.0:5000/users/"


# Données à envoyer dans la requête POST
data = {
    "id": 123,
    "nom": "Nom",
    "second_nom": "Second Nom",
    "prenom": "Prénom",
    "second_prenom": "Second Prénom",
    "username": "utilisateur123",
    "numeros": 456,
    "sexe": "Masculin",
    "email": "utilisat@example.com",
    "password": "MotDePasse123zzz",
    "pays": "Pays",
    "profession": "Profession",
    "date_de_naissance": "2000-01-01",
    "lieu_de_naissance": "Lieu de Naissance",
    "region": "Région",
    "quartier": "Quartier",
    "is_active": True,
    "publique_key": "Clé publiqddddue"
}

# Envoi de la requête POST
response = requests.post(url, json=data)

# Affichage de la réponse
print(response.status_code)  # Affiche le code d'état de la réponse
print(response.text)  # Affiche le contenu de la réponse
