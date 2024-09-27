import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Configuración de la autenticación
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="", 
                                               client_secret="",
                                               redirect_uri="",
                                               scope="playlist-read-private"))

# ID de la playlist
# Selecciona “Compartir” > “Copiar enlace de la playlist”.
# Extrae el ID de la playlist de este enlace. El ID es la parte que viene después de /playlist/ y antes de ?si=:
playlist_id = ''

# Obtener la información de la playlist (incluyendo su nombre)
playlist_info = sp.playlist(playlist_id)
playlist_name = playlist_info['name']

# Limpiar el nombre de la playlist para usarlo como nombre de archivo
# Elimina caracteres especiales no válidos en nombres de archivos
playlist_name = re.sub(r'[\\/*?:"<>|]', "", playlist_name)

# Obtener la playlist
results = sp.playlist_tracks(playlist_id)

# Abrir el archivo en modo escritura
with open('playlist.txt', 'w') as file:
    for idx, item in enumerate(results['items']):
        track = item['track']
        # Escribir en el archivo 
        file.write(f"{idx + 1}: {track['name']} - {track['artists'][0]['name']}\n")

print(f"Playlist exportada correctamente a '{playlist_name}.txt'")