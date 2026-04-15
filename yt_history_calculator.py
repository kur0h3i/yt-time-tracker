import re
import os
import sys

BANNER = """
╔══════════════════════════════════════════╗
║      YouTube History Calculator          ║
║  Descubre cuánto tiempo llevas en YT     ║
╚══════════════════════════════════════════╝
"""

INSTRUCCIONES = """
¿No sabes dónde está tu archivo? Sigue estos pasos:
  1. Ve a https://takeout.google.com
  2. Selecciona solo "YouTube y YouTube Music"
  3. En opciones, marca solo "Historial"
  4. Descarga el archivo ZIP y extráelo
  5. La ruta al archivo será algo como:
     Takeout/YouTube y YouTube Music/historial/historial-de-reproducciones.html
"""

def pedir_ruta_archivo():
    print(INSTRUCCIONES)
    while True:
        ruta = input("  Pega aquí la ruta completa al archivo HTML: ").strip().strip('"').strip("'")
        if os.path.isfile(ruta):
            return ruta
        print(f"\n  No se encontró el archivo en: '{ruta}'")
        print("   Asegúrate de que la ruta es correcta e inténtalo de nuevo.\n")

MINUTOS_PROMEDIO = 7

def calcular_horas_youtube(archivo_html):
    print("\n  Leyendo el archivo, esto puede tardar unos segundos...")
    try:
        with open(archivo_html, "r", encoding="utf-8") as f:
            contenido = f.read()
    except UnicodeDecodeError:
        with open(archivo_html, "r", encoding="latin-1") as f:
            contenido = f.read()

    enlaces_videos = re.findall(r'href="https://www\.youtube\.com/watch\?v=', contenido)
    total_videos = len(enlaces_videos)

    if total_videos == 0:
        print("\n  No se encontraron vídeos. ¿Estás seguro de que es el archivo correcto?")
        print("   El archivo debe llamarse 'historial-de-reproducciones.html'")
        return

    total_minutos = total_videos * MINUTOS_PROMEDIO
    total_horas = total_minutos / 60
    total_dias = total_horas / 24

    dias = int(total_minutos) // (24 * 60)
    resto = int(total_minutos) % (24 * 60)
    horas = resto // 60
    minutos = resto % 60

    print("\n" + "═" * 44)
    print("   RESULTADOS DE TU HISTORIAL DE YOUTUBE")
    print("═" * 44)
    print(f"   Vídeos en el historial : {total_videos:>10,}")
    print("─" * 44)
    print(f"   Total de horas         : {total_horas:>9,.0f} h")
    print(f"   Equivalente en días    : {total_dias:>9,.1f} días")
    print(f"   Tiempo exacto          : {dias} días, {horas} h y {minutos} min")
    print("═" * 44)
    print()

def main():
    print(BANNER)
    try:
        archivo = pedir_ruta_archivo()
        calcular_horas_youtube(archivo)
    except KeyboardInterrupt:
        print("\n\n  Cancelado por el usuario.")
        sys.exit(0)

if __name__ == "__main__":
    main()
