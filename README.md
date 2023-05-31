
# Stockholm Ransomware

Este es un programa de ransomware que utiliza cifrado AES para encriptar archivos en el directorio /home/infection. Sigue el siguiente proceso:

1. Generación de una clave de encriptación: Antes de iniciar el proceso de encriptación, se genera una clave secreta utilizando el algoritmo Fernet de la biblioteca de criptografía de Python. Esta clave se guarda en un archivo llamado `cif.key`.

2. Encriptación de archivos: Cuando se ejecuta el programa en modo de encriptación, todos los archivos con las extensiones especificadas en el directorio `/home/infection` serán encriptados. El programa lee cada archivo, lo cifra utilizando la clave generada y sobrescribe el archivo original con el archivo encriptado. Además, se cambia la extensión del archivo a `.ft` para indicar que ha sido encriptado.

3. Desencriptación de archivos: Si se proporciona la clave de desencriptación utilizando el argumento `-r` o `--reverse`, el programa puede desencriptar los archivos encriptados previamente. Al ejecutar el programa en modo de desencriptación, se lee cada archivo encriptado, se utiliza la clave proporcionada para desencriptarlo y se guarda como un archivo sin encriptar, restaurando la extensión original.

Es importante tener en cuenta que la clave de encriptación/desencriptación (`cif.key`) es fundamental para poder desencriptar los archivos. Asegúrate de guardar esta clave de forma segura, ya que sin ella no podrás recuperar los archivos encriptados.

## Requisitos previos

- Python 3.x
- Paquete `cryptography` (instalable a través de pip)

## Uso

Ejecuta el programa con los siguientes argumentos:

```
python stockholm.py [-h] [-r REVERSE] [-k GENKEY] [-s] [-v]
-r REVERSE o --reverse REVERSE: Proporciona la clave para desencriptar los archivos. Debe ser utilizado junto con el modo de desencriptación.
-k GENKEY o --genkey: Genera una nueva clave de cifrado y la guarda en el archivo cif.key.
-s o --silent: Modo silencioso. Ejecuta el programa sin mostrar mensajes.
-v o --version: Muestra la versión del programa.
```

