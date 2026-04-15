# YouTube History Calculator

Descubre cuántas horas de tu vida has pasado viendo YouTube — en menos de un minuto.

El script analiza el historial exportado desde Google Takeout y te devuelve una estimación del tiempo total que has invertido en la plataforma, desglosado en días, horas y minutos.

---

## Instalación y uso

No requiere librerías externas. Solo necesitas **Python 3.6+**.

```bash
git clone https://github.com/kur0h3i/youtube-history-calculator.git
cd youtube-history-calculator
python yt_history_calculator.py
```

El script te pedirá dos cosas por consola:
1. La ruta a tu archivo de historial de YouTube
2. La duración promedio de los vídeos que ves (opcional, por defecto 12 min)

---

## Cómo obtener tu historial de YouTube

1. Ve a [Google Takeout](https://takeout.google.com)
2. Haz clic en **"Deseleccionar todo"** y luego activa solo **"YouTube y YouTube Music"**
3. Dentro de las opciones, selecciona únicamente **"Historial"**
4. Descarga el archivo ZIP y extráelo
5. La ruta que necesitas será algo así:

```
Takeout/YouTube y YouTube Music/historial/historial-de-reproducciones.html
```

---

## Ejemplo de salida

```
════════════════════════════════════════════
   RESULTADOS DE TU HISTORIAL DE YOUTUBE
════════════════════════════════════════════
   Vídeos en el historial :      8,472
   Promedio por vídeo     :         12 min
────────────────────────────────────────────
   Total de horas         :      1,694 h
   Equivalente en días    :       70.6 días
   Tiempo exacto          : 70 días, 14 h y 24 min
════════════════════════════════════════════
```

---

## Nota sobre la precisión

El cálculo es una **estimación**. El archivo de historial de Google no incluye la duración real de cada vídeo, por lo que se multiplica el número de entradas por una duración promedio configurable. El resultado puede variar si:

- Tienes muchos Shorts (duración ~1 min)
- Ves principalmente vídeos largos (>30 min)
- Pausaste y reanudaste el mismo vídeo varias veces

Ajusta el promedio en la consola para obtener un resultado más cercano a tu consumo real.

---

## Requisitos

- Python 3.6 o superior
- Sin dependencias externas (solo usa `re`, `os` y `sys` de la librería estándar)

---

## Licencia

MIT — úsalo, modifícalo y compártelo libremente.
