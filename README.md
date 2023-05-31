
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
Importante: Este programa es solo para fines educativos y debe usarse de manera ética y responsable. No me hago responsable de ningún uso incorrecto o ilegal del programa.

Extensiones de archivos encriptados
Las siguientes extensiones de archivo se encriptarán si se encuentran en el directorio /home/infection:

.der, .pfx, .key, .crt, .csr, .p12, .pem, .odt, .ott, .sxw,
.stw, .uot, .3ds, .max, .3dm, .ods, .ots, .sxc, .stc, .dif,
.slk, .wb2, .odp, .otp, .sxd, .std, .uop, .odg, .otg, .sxm,
.mml, .lay, .lay6, .asc, .sqlite3, .sqlitedb, .sql, .accdb, .mdb,
.db, .dbf, .odb, .frm, .myd, .myi, .ibd, .mdf, .ldf, .sln,
.suo, .cs, .c, .cpp, .pas, .h, .asm, .js, .cmd, .bat,
.ps1, .vbs, .vb, .pl, .dip, .dch, .sch, .brd, .jsp, .php,
.asp, .rb, .java, .jar, .class, .sh, .mp3, .wav, .swf, .fla,
.wmv, .mpg, .vob, .mpeg, .asf, .avi, .mov, .mp4, .3gp, .mkv,
.3g2, .flv, .wma, .mid, .m3u, .m4u, .djvu, .svg, .ai, .psd,
.nef, .tiff, .tif, .cgm, .raw, .gif, .png, .bmp, .jpg, .jpeg,
.vcd, .iso, .backup, .zip, .rar, .7z, .gz, .tgz, .tar, .bak,
.tbk, .bz2, .PAQ, .ARC, .aes, .gpg, .vmx, .vmdk, .vdi, .sldm,
.sldx, .sti, .sxi, .602, .hwp, .snt, .onetoc2, .dwg, .pdf, .wk1,
.wks, .123, .rtf, .csv, .txt, .vsdx, .vsd, .edb, .eml, .msg,
.ost, .pst, .potm, .potx, .ppam, .ppsx, .ppsm, .pps, .pot,
.pptm, .pptx, .ppt, .xltm, .xltx, .xlc, .xlm, .xlt, .xlw,
.xlsb, .xlsm, .xlsx, .xls, .dotx, .dotm, .dot, .docm, .docb,
.docx, .doc

¡Atención!
Este programa es malicioso y se proporciona únicamente con fines educativos. No lo utilices para dañar, extorsionar o cometer actividades ilegales. El uso inapropiado de este programa es ilegal y puede tener consecuencias legales graves.

¡Utilízalo de manera ética y responsable!

css
Copy code

Recuerda que este archivo README es solo una guía básica y debes adaptarlo según tus necesidades y requisitos específicos. Además, ten en cuenta que el uso de ransomware o cualquier tipo de software malicioso está estrictamente prohibido y puede ser ilegal.