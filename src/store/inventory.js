import { reactive, watch } from "vue";

// Definición del estado reactivo del inventario
export const inventory = reactive({
	products: [
		{ id: 1, nombre: "Manzana", precio: 0.8, stock: 50, disponible: true },
		{ id: 2, nombre: "Pan Integral", precio: 1.5, stock: 30, disponible: true },
		{ id: 3, nombre: "Leche Entera", precio: 1.2, stock: 20, disponible: true },
		{
			id: 4,
			nombre: "Huevos (docena)",
			precio: 2.5,
			stock: 0,
			disponible: false,
		},
		{ id: 5, nombre: "Queso", precio: 3.0, stock: 15, disponible: true },
		{
			id: 6,
			nombre: "Filetes de Ternera",
			precio: 10.0,
			stock: 10,
			disponible: true,
		},
		{ id: 7, nombre: "Arroz (kg)", precio: 0.9, stock: 40, disponible: true },
		{
			id: 8,
			nombre: "Alubias (kg)",
			precio: 1.0,
			stock: 25,
			disponible: true,
		},
	],
});

// Watch para observar cambios en el array de productos (modo profundo)
watch(
	() => inventory.products,
	(newProducts) => {
		newProducts.forEach((product) => {
			product.disponible = product.stock > 0;
		});
	},
	{ deep: true }
);

// Función para actualizar el stock de un producto específico
export function updateStock(id, newStock) {
	const product = inventory.products.find((p) => p.id === id);
	if (product) {
		product.stock = newStock;
	}
}
