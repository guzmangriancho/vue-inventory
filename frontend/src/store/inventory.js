// src/store/inventory.js
import { reactive } from "vue";
import { fetchProducts, mutateStock } from "./api";

export const inventory = reactive({
	products: [],
});

// Inicializamos el inventario al arrancar la app
export async function initInventory() {
	try {
		const prods = await fetchProducts();
		inventory.products = prods;
	} catch (err) {
		console.error("Error cargando productos:", err);
	}
}

// Función para incrementar o decrementar stock vía backend
export async function updateStock(id, delta) {
	try {
		const updated = await mutateStock(id, delta);
		// Sustituye el producto en el array reactivo
		const idx = inventory.products.findIndex((p) => p.id === id);
		if (idx !== -1) {
			inventory.products[idx] = {
				...inventory.products[idx],
				stock: updated.stock,
				disponible: updated.disponible,
			};
		}
	} catch (err) {
		console.error("Error actualizando stock:", err);
	}
}
