<template>
	<tr>
		<td>{{ product.nombre }}</td>
		<td class="price">{{ product.precio.toFixed(2) }} €</td>
		<td class="stock">{{ product.stock }}</td>
		<td class="quantity">
			<span
				:class="{
					available: product.disponible,
					'not-available': !product.disponible,
				}"
			>
				{{ product.disponible ? "Disponible" : "No Disponible" }}
			</span>
		</td>
		<td class="action">
			<button class="btn-decrement" @click="decrementStock">-</button>
			<button class="btn-increment" @click="incrementStock">+</button>
		</td>
	</tr>
</template>

<script>
import { updateStock } from "../store/inventory";

export default {
	name: "ProductItem",
	props: {
		product: {
			type: Object,
			required: true,
		},
	},
	methods: {
		decrementStock() {
			const newStock = this.product.stock > 0 ? this.product.stock - 1 : 0;
			updateStock(this.product.id, newStock);
		},
		incrementStock() {
			const newStock = this.product.stock + 1;
			updateStock(this.product.id, newStock);
		},
	},
};
</script>

<style scoped>
.price,
.stock {
	text-align: right;
}

.quantity,
.action {
	text-align: center;
}

.btn-decrement {
	margin-right: 0.5rem;
}
</style>
