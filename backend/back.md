# Proyecto: Inventario de Productos (Backend)

Esta práctica consiste en crear una API con Flask y GraphQL para gestionar el inventario en memoria. A continuación respondo las preguntas teóricas de forma sencilla.

## Preguntas teóricas

### 1. ¿Qué ventajas ofrece GraphQL sobre REST en este contexto?

GraphQL permite al cliente solicitar solo los campos que necesita en una única petición al endpoint `/graphql`, evitando así recibir datos de más o de menos. Además, unifica todas las operaciones (consultas y mutaciones) en un solo punto, lo que simplifica la organización de rutas y la combinación de varias peticiones en una sola.

### 2. ¿Cómo se definen los tipos y resolvers en una API con GraphQL?

En el archivo de esquema (schema) se declaran los tipos de datos que maneja la API, por ejemplo `Producto` con sus campos `id`, `nombre`, `precio`, `stock` y `disponible`. Luego, en las funciones resolvers de Python asociadas a cada consulta o mutación, se accede al inventario en memoria, se procesan los argumentos recibidos y se devuelve o actualiza la información según corresponda.

### 3. ¿Por qué es importante que el backend también actualice `disponible` y no depender solo del frontend?

Porque el servidor se convierte en la fuente de verdad única: evita que un cliente malintencionado envíe valores de `disponible` incorrectos y garantiza que todos los clientes (web, móvil, etc.) vean datos coherentes, incluso si algún frontend falla o no ejecuta su propia lógica.

### 4. ¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?

Todas las modificaciones de `stock` pasan por la misma mutación en el backend, donde se recalcula `disponible` antes de devolver el producto. Además, se añaden validaciones para que el `stock` no sea negativo y se incluyen pruebas automáticas con pytest que verifican que al cambiar el `stock`, la `disponible` siempre se ajusta correctamente.
