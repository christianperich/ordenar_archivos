import shutil
from pathlib import Path

ruta_inicial = Path(input('Carpeta a ordenar: '))

archivos = list(ruta_inicial.glob('*'))

imagenes = ('png', 'jpg', 'jfif', 'webp', 'ico', 'svg')
ruta_imagenes = Path(f'{ruta_inicial}/Imagenes')

documentos = ('docx', 'doc', 'rtf', 'pdf', 'txt', 'xls', 'xlsx', 'ppt', 'pptx', 'html', 'htm', 'csv', 'log')
ruta_documentos = Path(f'{ruta_inicial}/documentos')

programas = ('.exe', '.msi')
ruta_programas = Path(f'{ruta_inicial}/programas')

videos = ('mp4', 'avi', 'mpg', 'mov')
ruta_videos = Path(f'{ruta_inicial}/videos')

audios = ('mp3', 'wav', 'flac', 'ogg')
ruta_audios = Path(f'{ruta_inicial}/audios')

comprimidos = ('rar', 'zip', '7zip', 'gz')
ruta_comprimidos = Path(f'{ruta_inicial}/comprimidos')


def main():
  for archivo in archivos:  
    archivo = str(archivo).lower()
    if archivo.endswith(imagenes):
      ruta_imagenes.mkdir(parents=True, exist_ok=True)
      shutil.move(Path(archivo), ruta_imagenes)
    elif archivo.endswith(documentos):
      ruta_documentos.mkdir(parents=True, exist_ok=True)
      shutil.move(Path(archivo), ruta_documentos)
    elif archivo.endswith(programas):
      ruta_programas.mkdir(parents=True, exist_ok=True)
      shutil.move(Path(archivo), ruta_programas)
    elif archivo.endswith(videos):
      ruta_videos.mkdir(parents=True, exist_ok=True)
      shutil.move(Path(archivo), ruta_videos)
    elif archivo.endswith(audios):
      ruta_audios.mkdir(parents=True, exist_ok=True)
      shutil.move(Path(archivo), ruta_audios)
    elif archivo.endswith(comprimidos):
      ruta_comprimidos.mkdir(parents=True, exist_ok=True)
      shutil.move(Path(archivo), ruta_comprimidos)


if __name__ == '__main__':
  main()