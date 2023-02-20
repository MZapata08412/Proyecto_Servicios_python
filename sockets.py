#!/usr/bin/python3  
#Se programa el servidor de comunicación con aplicacion servicios
# Creación del servidor 
import socket

host = socket.gethostname() #Nombre de la máquina
port = 12345
BUFFER_SIZE = 1024 


# Objeto Socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:

    socket_tcp.bind((host, port)) 
    socket_tcp.listen(3) # Tiempo de refrescamiento  
    conn, addr = socket_tcp.accept() # Comunicación con el cliente 
    with conn:
        print('[*] Conexión exitosa') 
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            else:
                print('[*] Informacion recibida: {}'.format(data.decode('utf-8'))) 
            conn.send(data)
