import requests
import os


url = "https://avatars.githubusercontent.com/u/128254439?v=4" # URL de l'image à télécharger
filename = "image.jpg"                                        # Nom du fichier à enregistrer
folder_path = r"C:\Users\Arthur\Desktop\img"                  # Répertoire de destination pour l'image téléchargée

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file_path = os.path.join(folder_path, filename)
response = requests.get(url)
if response.status_code == 200:
    with open(file_path, 'wb') as f:
        f.write(response.content)
    print("L'image a été téléchargée avec succès.")
else:
    print("La requête a échoué avec le code d'erreur :", response.status_code)
