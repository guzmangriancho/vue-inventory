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
			<button
				class="btn-decrement"
				@click="decrementStock"
				:disabled="!product.disponible"
			>
				-
			</button>
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
			updateStock(this.product.id, -1);
		},
		incrementStock() {
			updateStock(this.product.id, +1);
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

button:disabled {
	opacity: 0.5;
	cursor: not-allowed;
}
</style>
