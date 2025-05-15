<template>
	<div>
		<table class="inventory-table">
			<thead>
				<tr>
					<th class="col-nombre">Producto</th>
					<th class="col-precio" style="text-align: right">Precio</th>
					<th class="col-stock" style="text-align: right">Stock</th>
					<th class="col-estado" style="text-align: center">Estado</th>
					<th class="col-acciones" style="text-align: center">Acciones</th>
				</tr>
			</thead>
			<tbody>
				<ProductItem
					v-for="product in products"
					:key="product.id"
					:product="product"
				/>
			</tbody>
		</table>
	</div>
</template>

<script>
import { toRefs } from "vue";
import { inventory } from "../store/inventory";
import ProductItem from "./ProductItem.vue";

export default {
	name: "ProductList",
	components: {
		ProductItem,
	},
	setup() {
		const { products } = toRefs(inventory);
		return { products };
	},
};
</script>

<style scoped>
.inventory-table {
	width: 100%;
	border-collapse: collapse;
	table-layout: fixed;
}

.inventory-table th,
.inventory-table td {
	padding: 0.75rem 1rem;
	text-align: left;
	border-bottom: 1px solid #444;
	color: #fff;
}

.inventory-table thead {
	background-color: #333;
}

.col-nombre {
	width: 20%;
}

.col-precio {
	width: 15%;
}

.col-stock {
	width: 15%;
}

.col-estado {
	width: 20%;
}

.col-acciones {
	width: 20%;
}
</style>
