import reflex as rx
import os
from dotenv import dotenv_values

envConfig = dotenv_values()


config = rx.Config(
    app_name="arris",
    db_url=os.environ["DATABASE_URL"],
    shopify_api_key=os.environ["SHOPIFY_API_KEY"],
    shopify_api_secret_key=os.environ["SHOPIFY_API_SECRET_KEY"],
    be_domain=os.environ["BE_DOMAIN"],
    fe_domain=os.environ["FE_DOMAIN"],
    jwt_secret=os.environ["JWT_SECRET"],
    openai_key=os.environ["OPENAI_KEY"],
)
