# Inventory Vue (Frontend + Backend)

Este repositorio contiene dos proyectos independientes que conforman una tienda online con inventario reactivo:

- **frontend/**: aplicación web desarrollada con Vue 3 y Vite. Muestra el inventario de productos de forma dinámica.
- **backend/**: API construida con Flask y GraphQL. Gestiona los datos en memoria del inventario.

En cada carpeta encontrarás un archivo con las respuestas teóricas de la correspondiente práctica:

- **frontend/front.md**: respuestas sobre reactividad en Vue (Práctica de frontend).
- **backend/back.md**: respuestas sobre GraphQL y Flask (Práctica de backend).

---

## Requisitos previos

- **Node.js** (v16+).
- **Python** (v3.8+).
- **Git**.
- **PowerShell**.

---

## Instalación

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/guzmangriancho/vue-inventory.git
   cd vue-inventory
   ```

2. **Instalar dependencias del backend**

   ```bash
   cd backend
   python -m venv venv
   .\venv\Scripts\Activate
   pip install -r requirements.txt
   ```

3. **Instalar dependencias del frontend**

   ```bash
   cd frontend
   npm install
   ```

---

## Uso

### Backend

1. Activar el entorno virtual:

   ```bash
   cd backend
   .\venv\Scripts\Activate
   ```

2. Iniciar el servidor:

   ```bash
   python app.py
   ```

- La API GraphQL estará disponible en:
  `http://localhost:5000/graphql`

- Esta query sirve para leer todos los productos de la bbdd:
- 
  ```bash
     query GetProductos {
     products {
       id
       nombre
       precio
       stock
       disponible
     }
   }
   ```

### Frontend

En otra terminal, desde la carpeta `frontend`:

```bash
npm run dev
```

- La aplicación Vue se ejecutará en:
  `http://localhost:5173`

### Levantar todo junto (Windows)

En la raíz del proyecto (`inventory-vue`), ejecuta el script:

```powershell
./start-all.ps1
```

Este script abrirá dos consolas (una para el backend y otra para el frontend) y lanzará automáticamente el navegador con ambas URLs.

---

## Pruebas

En `backend/tests/` hay un archivo `test_api.py` con pruebas básicas usando `pytest`. Para ejecutarlas:

```bash
cd backend
pip install pytest
pytest
```
