import shutil
from pathlib import Path

EXTENSIONS = {
  'imagenes': ('.png', '.jpg', '.jfif', '.webp', '.ico', '.svg'),
  'documentos': ('.docx', '.doc', '.rtf', '.pdf', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.html', '.htm', '.csv', '.log'),
  'programas': ('.exe', '.msi'),
  'videos': ('.mp4', '.avi', '.mpg', '.mov'),
  'audios': ('.mp3', '.wav', '.flac', '.ogg'),
  'comprimidos': ('.rar', '.zip', '.7zip', '.gz')
}


def ordenar_archivos(ruta_inicial):
  archivos = list(ruta_inicial.glob('*'))
  
  for categoria, extensiones in EXTENSIONS.items():
    
    for archivo in archivos:
      if str(archivo).endswith(extensiones):
        ruta = Path(f'{ruta_inicial}/{categoria}')
        ruta.mkdir(parents=True, exist_ok=True)
        shutil.move(Path(archivo), ruta)
    

def main():
  ruta_inicial = Path(input('Carpeta a ordenar: '))  
  ordenar_archivos(ruta_inicial)
  

if __name__ == '__main__':
  main()