<template>
	<div id="app">
		<header>
			<h1>Inventario de Productos</h1>
		</header>
		<main>
			<div class="table-container">
				<ProductList />
			</div>
		</main>
		<footer>
			<p>
				Guzmán G. Riancho Gutiérrez - Programación Web II - Universidad Europea
				del Atlántico
			</p>
		</footer>
	</div>
</template>

<script>
import ProductList from "./components/ProductList.vue";

export default {
	name: "App",
	components: {
		ProductList,
	},
};
</script>

<style>
header {
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	background-color: #1a1a1a;
	padding: 1rem 2rem;
	z-index: 1000;
}

main {
	padding-top: 80px;
	display: flex;
	justify-content: center;
}

.table-container {
	width: 80%;
	margin-top: 2rem;
	background-color: #1a1a1a;
	padding: 1rem 2rem;
	border-radius: 8px;
}

footer {
	color: rgb(83, 83, 83);
	position: fixed;
	bottom: 0;
	left: 0;
	width: 100%;
	font-size: 0.9em;
	text-align: center;
}
</style>
