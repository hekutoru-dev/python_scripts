import os;
import time;
import datetime;

path = '';

# Simple script to change and format filenames.

# Reorder filename, date of creation and extention.
for archivo in os.listdir(path):
    # Get date creation of file
    status_archivo = os.stat(archivo);
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(archivo);
    
    # datetime file creation
    date_time = datetime.datetime.strptime(time.ctime(ctime), "%a %b %d %H:%M:%S %Y");
    
    # Get only YMD
    fecha_creacion = date_time.strftime("%d%m%Y");

    # Separate name and extention of the files
    filename, file_extension = os.path.splitext(archivo);
    
    # Title format
    filename = filename.title();
    
    # Change spaces by _
    espacio = " "; guion = "_";       
    nArchivo = filename.replace(espacio,guion);
    
    print nArchivo + "_" + fecha_creacion + file_extension;
    
   
