import reflex as rx
from models import ShopifyPage
from sqlmodel import select


def get_store_pages(storeId: int):
    with rx.session() as session:
        shopifyPages = session.exec(
            select(ShopifyPage).where(ShopifyPage.store_id == storeId)
        ).all()
        return shopifyPages


def get_store_page_by_id(id: int):
    with rx.session() as session:
        shopifyPage = session.exec(
            select(ShopifyPage).where(ShopifyPage.id == id)
        ).first()

        return shopifyPage


def get_store_page_by_page_id(page_id: str):
    with rx.session() as session:
        shopifyPage = session.exec(
            select(ShopifyPage).where(ShopifyPage.page_id == page_id)
        ).first()

        return shopifyPage


def update_store_page(id: int, body_html: str):
    with rx.session() as session:
        shopifyPage = session.exec(
            select(ShopifyPage).where(ShopifyPage.id == id)
        ).first()

        shopifyPage.body_html = body_html

        session.add(shopifyPage)
        session.commit()


def delete_store_page(id: int):
    with rx.session() as session:
        shopifyPage = session.exec(
            select(ShopifyPage).where(ShopifyPage.id == id)
        ).first()

        session.delete(shopifyPage)
        session.commit()


def create_store_page(
    page_id: str,
    shopify_store_id: str,
    title: str,
    handle: str,
    body_html: str,
    author: str,
    template_suffix: str,
    admin_graphql_api_id: str,
    created_at: str,
    updated_at: str,
    published_at: str,
    store_id: int,
):

    with rx.session() as session:
        session.add(
            ShopifyPage(
                page_id=page_id,
                shopify_store_id=shopify_store_id,
                title=title,
                handle=handle,
                body_html=body_html,
                author=author,
                template_suffix=template_suffix,
                admin_graphql_api_id=admin_graphql_api_id,
                created_at=created_at,
                updated_at=updated_at,
                published_at=published_at,
                store_id=store_id,
            )
        )
        session.commit()
