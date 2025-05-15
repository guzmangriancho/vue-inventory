// src/store/api.js
const GRAPHQL_URL = "http://127.0.0.1:5000/graphql";

export async function fetchProducts() {
	const query = `
    query {
      products {
        id
        nombre
        precio
        stock
        disponible
      }
    }
  `;
	const res = await fetch(GRAPHQL_URL, {
		method: "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify({ query }),
	});
	const { data, errors } = await res.json();
	if (errors) throw new Error(errors.map((e) => e.message).join(", "));
	return data.products;
}

export async function mutateStock(id, delta) {
	const mutation = `
    mutation($id: Int!, $delta: Int!) {
      updateStock(id: $id, delta: $delta) {
        product {
          id
          stock
          disponible
        }
      }
    }
  `;
	const res = await fetch(GRAPHQL_URL, {
		method: "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify({ query: mutation, variables: { id, delta } }),
	});
	const { data, errors } = await res.json();
	if (errors) throw new Error(errors.map((e) => e.message).join(", "));
	return data.updateStock.product;
}
