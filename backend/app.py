from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from data import productos, get_all_products, update_stock
from schema import schema

app = Flask(__name__)
cors = CORS(app)

# ruta graphql
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True
    )
)

if __name__ == "__main__":
    app.run(debug=True, port=5000)