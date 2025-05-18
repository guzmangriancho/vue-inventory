import graphene
from data import productos, get_all_products, update_stock

class producttype(graphene.ObjectType):
    id = graphene.Int()
    nombre = graphene.String()
    precio = graphene.Float()
    stock = graphene.Int()
    disponible = graphene.Boolean()

class query(graphene.ObjectType):
    products = graphene.List(producttype)

    def resolve_products(self, info):
        return [producttype(**p) for p in get_all_products()]

class updatestock(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        delta = graphene.Int(required=True)

    product = graphene.Field(producttype)

    def mutate(self, info, id, delta):
        prod = update_stock(id, delta)
        return updatestock(product=producttype(**prod))

class clearproducts(graphene.Mutation):
    ok = graphene.Boolean()

    def mutate(self, info):
        productos.clear()
        return clearproducts(ok=True)

class mutation(graphene.ObjectType):
    update_stock = updatestock.Field()
    clear_products = clearproducts.Field()

schema = graphene.Schema(query=query, mutation=mutation)