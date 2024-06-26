import reflex as rx
from models import ShopifyStores
from sqlmodel import select


def get_stores(email):
    with rx.session() as session:
        stores = session.exec(
            select(ShopifyStores).where(ShopifyStores.email == email)
        ).all()

        print(stores)

        return stores


def get_store(
    name: str,
    email: str = None,
):
    with rx.session() as session:
        if email is None:
            store = session.exec(
                select(ShopifyStores).where(ShopifyStores.name == name)
            ).first()

            return store

        store = session.exec(
            select(ShopifyStores).where(
                ShopifyStores.name == name and ShopifyStores.email == email
            )
        ).first()

        return store


def get_store_by_name(name: str):
    with rx.session() as session:
        store = session.exec(
            select(ShopifyStores).where(ShopifyStores.name == name)
        ).first()

        return store


def update_store(name: str):

    with rx.session() as session:
        store = session.exec(
            select(ShopifyStores).where(ShopifyStores.name == name)
        ).first()

        session.add(store)
        session.commit()


def add_store(
    name: str,
    email: str,
    access_token: str,
):

    with rx.session() as session:
        session.add(
            ShopifyStores(
                name=name,
                email=email,
                access_token=access_token,
            )
        )
        session.commit()
