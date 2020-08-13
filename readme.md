# Cómo usar

Para realizar la búsqueda de las keywords dentro de una carpeta dada, el programa se debe correr dentro de dicha carpeta. 

Por ejemplo, si queremos analizar los archivos contenidos dentro de la carpeta T02, tanto el archivo *keywords.json* como el archivo *alerta.py* deben estar ubicados en la misma carpeta T02.

Para correr el programa, es necesario utilizar el comando

```
python alerta.py nombre_carpeta_base
```

En el caso de querer analizar los archivos del directorio T02:
```
python alerta.py T02
```


Esto generará un archivo de *output* llamado *_usernames.txt*, donde se encuentran los nombres de usuario de les alumnes a los que uno querría darle una mirada más detallada a sus archivos.