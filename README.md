# Spotify Playlist Exporter

Este script de Python permite exportar una playlist de Spotify a un archivo de texto (`.txt`) con el nombre de la playlist, donde cada canción se lista junto con el artista correspondiente.

## Requisitos

Antes de ejecutar el script, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.x
- `spotipy` (librería de Python para interactuar con la API de Spotify)

Puedes instalar `spotipy` ejecutando el siguiente comando:

```bash
pip install spotipy
```
## Configuración

  1.	Crea una aplicación en el Spotify Developer Dashboard para obtener tus credenciales de API (Client ID y Client Secret).
     
  2.	En tu cuenta de desarrollador de Spotify, configura la URL de redirección (Redirect URI) como http://localhost:8888/callback.
	
  3.	En el script export_playlist.py, reemplaza los siguientes valores con tus credenciales de Spotify:

    client_id="TU_CLIENT_ID"
    client_secret="TU_CLIENT_SECRET"
    redirect_uri="TU_REDIRECT_URI"

  4.	Reemplaza 'tu_playlist_id' por el ID de la playlist que deseas exportar. Para obtener el ID de la playlist:
	•	Abre Spotify.
	•	Haz clic en los tres puntos (...) de la playlist y selecciona Compartir > Copiar enlace de la playlist.
	•	El ID es la cadena que viene después de https://open.spotify.com/playlist/.

## Uso

Una vez configurado, puedes ejecutar el script para exportar la playlist a un archivo de texto:

python export_playlist.py

El archivo generado tendrá el mismo nombre que la playlist y contendrá una lista numerada de las canciones junto con sus artistas.

## Ejemplo de salida

Si el nombre de la playlist es Mis Canciones Favoritas, se generará un archivo Mis Canciones Favoritas.txt con el siguiente formato:

1: Canción 1 - Artista 1

2: Canción 2 - Artista 2

3: Canción 3 - Artista 3

...
