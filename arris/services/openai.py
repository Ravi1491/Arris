import reflex as rx
from openai import OpenAI
from rxconfig import config

client = OpenAI(api_key=config.openai_key)


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )

    print(response.choices[0].message.content)

    return response.choices[0].message.content


def generate_html_for_products(title, url, desc, price):
    prompts = f"""
      Design a Shopify hero section for a product page featuring the {title}. The section should be elegantly styled using HTML with inline CSS
      product title: {title}
      product image url: {url}
      product description: {desc}
      product price: {price}

      Design instruction:
      1. Always give html code with inline css and those css must be inside html tags only and don't apply any css on body tag. The design must have modern look with some extra tag line.
      2. Do not explain, only give the code block.
      3. Only give the code of body block
    """

    html = get_completion(prompts)

    print("html", html)

    return html
