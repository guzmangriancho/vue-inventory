# schema.py
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Product as ProductModel
from database import SessionLocal

class ProductType(SQLAlchemyObjectType):
    class Meta:
        model = ProductModel
        fields = ("id", "nombre", "precio", "stock", "disponible")

class Query(graphene.ObjectType):
    products = graphene.List(ProductType)

    def resolve_products(self, info):
        db = SessionLocal()
        all_products = db.query(ProductModel).all()
        db.close()
        return all_products

class UpdateStock(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        delta = graphene.Int(required=True)

    product = graphene.Field(ProductType)

    def mutate(self, info, id, delta):
        db = SessionLocal()
        prod = db.get(ProductModel, id)
        if not prod:
            db.close()
            raise Exception(f"Producto con id={id} no encontrado")
        prod.stock = max(prod.stock + delta, 0)
        prod.disponible = prod.stock > 0
        db.add(prod)
        db.commit()
        db.refresh(prod)
        db.close()
        return UpdateStock(product=prod)

class ClearProducts(graphene.Mutation):
    ok = graphene.Boolean()

    def mutate(self, info):
        db = SessionLocal()
        # Borra todas las filas de la tabla products
        db.query(ProductModel).delete()
        db.commit()
        db.close()
        return ClearProducts(ok=True)

class Mutation(graphene.ObjectType):
    update_stock = UpdateStock.Field()
    clear_products  = ClearProducts.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
