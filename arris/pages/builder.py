import reflex as rx
from arris.services.shopify import get_store
from arris.protected import require_login
from arris.services.shopify_page import ShopifyPageService


class BuilderState(rx.State):
    data: dict = {}

    @rx.var
    def store_name(self) -> str:
        return self.router.page.params.get("store_name")

    def get_data(self):

        self.data = get_store(self.store_name)

        print(self.data)

    def createPage(self, form_data: dict):

        page_title = form_data["page_title"]
        html = "<h1>ARRIS</h1>"

        if page_title == "":
            return rx.window_alert("Please enter a valid page title")

        print("page_title", page_title)
        print("html", html)

        return ShopifyPageService.create_page(
            self.store_name,
            page_title,
            html,
        )


@rx.page(on_load=BuilderState.get_data)
@require_login
def builder():
    return rx.box(
        rx.heading("Builder Page"),
        rx.heading(BuilderState.store_name),
        rx.form.root(
            rx.form.field(
                rx.flex(
                    rx.form.label("Page Title"),
                    rx.form.control(
                        rx.input.input(
                            placeholder="Page Title",
                            type="name",
                        ),
                        as_child=True,
                    ),
                    direction="column",
                    spacing="2",
                ),
                name="page_title",
            ),
            rx.form.submit(
                rx.button("Create Page"),
                as_child=True,
            ),
            on_submit=BuilderState.createPage,
        ),
    )
