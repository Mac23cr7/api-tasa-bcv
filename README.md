# API de tasa del BCV

Esta API obtiene la tasa del Banco Central de Venezuela desde la página oficial del BCV y expone los datos a través de un endpoint JSON.

## Requisitos

- Python 3.10+
- pip

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate  # En Linux/macOS
.venv\Scripts\activate     # En Windows
pip install -r requirements.txt
```

## Ejecución local

```bash
python app.py
```

La API estará disponible en:

```text
http://127.0.0.1:5000/api/obtener-tasa-bcv
```

## Endpoint

### GET /api/obtener-tasa-bcv

Devuelve un JSON con la fecha y la información de las tasas del BCV.

Ejemplo de respuesta exitosa:

```json
{
  "date": "16/07/2026",
  "data": [
    {
      "name": "Dólar",
      "price": "36,00",
      "image": "https://www.bcv.org.ve/images/dolar.png"
    }
  ]
}
```

Si el BCV no responde o está caído, el endpoint devuelve un mensaje amigable para el frontend:

```json
{
  "success": false,
  "error": "No se pudo obtener la tasa del BCV",
  "message": "La tasa del BCV no está disponible en este momento. Intenta nuevamente más tarde."
}
```

## Despliegue en Vercel

Este proyecto está preparado para desplegarse en Vercel usando la configuración de [vercel.json](vercel.json).

## Tecnologías usadas

- Flask
- BeautifulSoup
- Requests
- Flask-Cors
