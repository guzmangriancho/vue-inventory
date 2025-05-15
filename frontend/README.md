# Proyecto: Inventario de Productos

Este proyecto es una tienda online que maneja un inventario de productos, desarrollado con **Vue 3** y **Vite**. Se utiliza `reactive()` y `watch()` para gestionar la reactividad sin emplear propiedades computadas.

---

## Estructura de Archivos

```
vue-inventory/
├── index.html
├── package.json
├── public/
├── src/
│   ├── assets/
│   ├── components/             # Componentes reutilizables
│   │   ├── ProductList.vue     # Lista de productos (tabla)
│   │   └── ProductItem.vue     # Fila de cada producto
│   ├── store/
│   │   └── inventory.js        # Inventario reactivo y lógica de watch
│   ├── App.vue                 # Componente raíz (incluye header, main y footer)
│   └── main.js                 # Punto de entrada de la aplicación
└── vite.config.js
```

---

## Respuestas a las preguntas teóricas

### 1. ¿Cómo podrías observar un cambio en una propiedad anidada?

En Vue, cuando usamos `reactive()` para crear objetos con propiedades anidadas, la reactividad no siempre se propaga a niveles profundos de forma automática. Para observar cambios en una propiedad anidada, es necesario usar un `watch()` configurado en modo profundo (`deep: true`). Esto le indica a Vue que debe monitorear no solo el objeto en sí, sino también sus propiedades internas. Por ejemplo, si tenemos un objeto producto con la propiedad `stock` y queremos actualizar `disponible` cada vez que `stock` cambia, podemos usar un watch profundo para detectar esos cambios.

### 2. ¿Cómo funciona `watch()` para escuchar cambios en propiedades específicas dentro de `reactive()`?

La función `watch()` en Vue se utiliza para reaccionar ante cambios en valores reactivos. Al pasarle una función que retorne la propiedad o el objeto a observar, `watch()` ejecuta una función callback cada vez que se detecta un cambio. En el callback se pueden realizar operaciones o actualizaciones en función del nuevo valor. En el caso de este proyecto, se usa para revisar el valor de `stock` en cada producto y actualizar la propiedad `disponible` sin necesidad de usar propiedades computadas.

### 3. ¿Cómo harías que un `watch()` detecte cambios en `stock` dentro de un array de productos?

Cuando tenemos un array de objetos reactivos, como es el caso de nuestro inventario de productos, y queremos que `watch()` detecte cambios en propiedades internas (por ejemplo, `stock`), es fundamental configurar el watch en modo profundo (`deep: true`). Al hacerlo, Vue recorrerá cada objeto del array y monitorizará cualquier cambio en sus propiedades internas. De esta forma, cualquier modificación en el valor de `stock` disparará el callback del watch y permitirá actualizar la propiedad `disponible` de forma reactiva.

---

## Teoría Aplicada al Proyecto

En este proyecto se utiliza el sistema reactivo de Vue para gestionar un inventario.

- **Estado Reactivo:**  
  Se define el inventario con `reactive()` en `src/store/inventory.js`, donde cada producto es un objeto con `nombre`, `precio`, `stock` y `disponible`.

- **Monitoreo de Cambios:**  
  Se utiliza `watch()` en modo profundo para actualizar automáticamente `disponible` en función del `stock`.

- **Componentes y Estructura:**  
  Los componentes están divididos en `ProductList.vue` (tabla de productos) y `ProductItem.vue` (fila individual). La aplicación está montada en `App.vue`, que incluye además un header y un footer.  
  Se usa **Vite** para aprovechar tiempos de recarga rápidos y una configuración optimizada para proyectos modernos con **Vue 3**.

---

Guzmán González de Riancho Gutiérrez
