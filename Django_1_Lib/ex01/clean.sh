#!/bin/bash

# Supprimer le répertoire 'my_directory' et tout son contenu
rm -rf my_directory

# Supprimer le répertoire 'local_lib' et tout son contenu
rm -rf local_lib

# Supprimer le fichier 'install.log'
rm -f install.log

# Vérifier que les répertoires et le fichier ont bien été supprimés
if [ ! -d "my_directory" ] && [ ! -d "local_lib" ] && [ ! -f "install.log" ]; then
    echo "Les répertoires et le fichier ont été supprimés avec succès."
else
    echo "Une erreur s'est produite lors de la suppression des répertoires et du fichier."
fi