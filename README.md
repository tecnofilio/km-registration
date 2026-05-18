# Proyecto Flask para registrar fotos

Aplicacion web simple en Flask para cargar una foto, elegir una categoria desde un menu desplegable, agregar comentarios y mostrar una vista previa con el resumen enviado.

## Requisitos

- Python 3.10 o superior

## Instalacion

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Ejecutar

```powershell
python app.py
```

Luego abre `http://127.0.0.1:5000`.

## Campos del formulario

- Foto: PNG, JPG, JPEG, GIF o WEBP.
- Tipo: Office, Private, Office + private o BT.
- Comentarios: texto libre opcional.

## Formatos permitidos

PNG, JPG, JPEG, GIF y WEBP, con un limite de 8 MB por imagen.
