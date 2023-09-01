import os
import shutil

from_dir = "c:\Users\LENOVO\Downloads" 
to_dir = "c:\Users\LENOVO\Pictures\Camera Roll"

list_of_files = os.listdir(from_dir)

# Mueve todos los archivos tipo imagen de la carpeta Descargas a una nueva carpeta
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:

        path1 = from_dir + 'C:\Users\LENOVO\Downloads\App Image 2023-08-31 at 6.10.09 AM (2).jpeg' + file_name                       # Ejemplo path1 : Descargas/NombreImagen1.jpg        
        path2 = to_dir + 'c:\Users\LENOVO\Pictures\Camera Roll' + "Image_Files"                     # Ejemplo path2 : D:/Mis archivos/Archivos_imagen      
        path3 = to_dir + 'c:\Users\LENOVO\Pictures\Camera Roll' + "Image_Files" + '/' + file_name   # Ejemplo path3 : D:/Mis archivos/Archivos_imagen/Nombreimagen1.jpg
        #print("path1 " , path1)
        #print("path3 ", path3)

        # Checa si la ruta de la carpeta/directorio existen antes de moverlo
        # Si no crear una nueva carpeta/directorio y muévelo
        if os.path.exists(path2):
          print("Movviendo " + file_name + ".....")

          # Mueve de path1 ---> path3
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moviendo " + file_name + ".....")
          shutil.move(path1, path3)