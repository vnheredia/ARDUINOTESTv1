import socket
import psutil
import json

# Configura el servidor
host = '10.3.20.242'   # Escucha en todas las interfaces de red disponibles
port = 12345       # Puerto de escucha

# Crea un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlaza el socket al host y al puerto
server_socket.bind((host, port))

# Escucha hasta 1 conexión entrante
server_socket.listen(1)

print(f"El servidor está escuchando en {host}:{port}")

# Acepta la conexión entrante
client_socket, client_address = server_socket.accept()

print(f"Conexión establecida desde {client_address}")

# Obtiene estadísticas del consumo de memoria
memory_stats = psutil.virtual_memory()

# Convierte las estadísticas a un formato JSON
memory_stats_json = json.dumps({
    'total': memory_stats.total,
    'available': memory_stats.available,
    'percent': memory_stats.percent,
    'used': memory_stats.used
})

# Envía las estadísticas al cliente
client_socket.send(memory_stats_json.encode())

# Cierra la conexión
client_socket.close()
server_socket.close()
