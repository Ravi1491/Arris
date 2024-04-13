import os
import reflex as rx
from dotenv import dotenv_values  # type: ignore

config = dotenv_values()

database_url = os.environ.get(
    "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/arris"
)

shopify_api_key = os.environ.get("SHOPIFY_API_KEY")
shopify_api_secret_key = os.environ.get("SHOPIFY_API_SECRET_KEY")
be_domain = os.environ.get("BE_DOMAIN", "http://localhost:8000")

config = rx.Config(
    app_name="arris",
    db_url=config["DATABASE_URL"],
    shopify_api_key=config["SHOPIFY_API_KEY"],
    shopify_api_secert_key=config["SHOPIFY_API_SECRET_KEY"],
)

print(config.db_url)
