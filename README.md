
# Stockholm Ransomware

Este es un programa de ransomware que utiliza cifrado AES para encriptar archivos en el directorio /home/infection.

## Requisitos previos

- Python 3.x
- Paquete `cryptography` (instalable a través de pip)

## Uso

Ejecuta el programa con los siguientes argumentos:

```shell
python stockholm.py [-h] [-r REVERSE] [-k GENKEY] [-s] [-v]
-r REVERSE o --reverse REVERSE: Proporciona la clave para desencriptar los archivos. Debe ser utilizado junto con el modo de desencriptación.
-k GENKEY o --genkey: Genera una nueva clave de cifrado y la guarda en el archivo cif.key.
-s o --silent: Modo silencioso. Ejecuta el programa sin mostrar mensajes.
-v o --version: Muestra la versión del programa.
---
