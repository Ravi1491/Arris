import reflex as rx
from arris.services.shopify import get_store
from arris.protected import require_login
from arris.services.shopify_page import update_page, delete_page
from arris.utils import ClientStorageState
from arris.schemas.shopify_page import get_store_page_by_id


class BuilderPageState(ClientStorageState):
    data: dict = {}
    is_fetching: bool = False
    html: str = "<div></div>"
    save_disabled: bool = True

    @rx.var
    def store_name(self) -> str:
        return self.router.page.params.get("store_name")

    @rx.var
    def page_id(self) -> str:
        return self.router.page.params.get("page_id")

    def get_data(self):
        self.is_fetching = True
        print("self.store_name", self.store_name)
        print("self.page_id", self.page_id)

        store_data = get_store(self.store_name)
        print("store_data", store_data)

        data = get_store_page_by_id(self.page_id)

        self.html = data.body_html
        self.is_fetching = False
        self.data = data

        print("self.data", self.data)

    def handle_change(self, html: str):
        self.html = html

        if html != self.data.body_html:
            self.save_disabled = False
        else:
            self.save_disabled = True

    def save_page(self):
        update_page(self.store_name, self.page_id, self.html)

        self.save_disabled = True
        self.data.body_html = self.html

    def remove_page(self):
        delete_page(self.store_name, self.page_id)

        self.save_disabled = True
        self.data.body_html = self.html


@rx.page(on_load=BuilderPageState.get_data, route="/builder/[store_name]/[page_id]")
@require_login
def builder_page() -> rx.Component:

    return rx.cond(
        BuilderPageState.is_fetching,
        rx.chakra.center(
            rx.chakra.spinner(),
        ),
        rx.box(
            rx.box(
                rx.box(
                    rx.image(
                        src="/company_logo.png",
                        alt="Descriptive text about the image",
                        height="45px",
                        width="45px",
                    ),
                    rx.text(
                        "ARRIS",
                        font_family="Integral CF",
                        class_name="text-2xl font-bold text-black",
                    ),
                    class_name="w-full flex gap-2 items-center",
                ),
                rx.cond(
                    BuilderPageState.save_disabled,
                    rx.button(
                        "Save and Publish",
                        disabled=BuilderPageState.save_disabled,
                        height="40px",
                        color="white",
                    ),
                    rx.button(
                        "Save and Publish",
                        on_click=BuilderPageState.save_page,
                        height="40px",
                        background_color="black",
                        color="white",
                        cursor="pointer",
                    ),
                ),
                class_name="flex justify-between items-center w-full mt-2 px-4 max-w-7xl mx-auto",
            ),
            rx.box(
                rx.box(
                    rx.image(
                        src="/company_logo.png",
                        alt="Descriptive text about the image",
                        height="45px",
                        width="45px",
                    ),
                    rx.text(
                        BuilderPageState.data["title"],
                        class_name="text-xl font-bold text-black",
                    ),
                    class_name="w-full flex gap-2 items-center",
                ),
                class_name="flex items-center w-full px-4 max-w-7xl mx-auto",
            ),
            rx.box(
                rx.text_area(
                    placeholder="Type here...",
                    value=BuilderPageState.html,
                    on_change=BuilderPageState.handle_change,
                    border="1px dashed #ccc",
                    border_radius="4px",
                    width="100%",
                    height="80vh",
                ),
                rx.box(
                    rx.html(
                        BuilderPageState.html,
                        height="80vh",
                    ),
                    border="1px dashed #ccc",
                    border_radius="4px",
                    width="100%",
                    class_name="overflow-y-auto",
                ),
                class_name="flex gap-2 items-center w-full max-w-7xl mx-auto justify-between my-4",
            ),
            class_name="h-screen w-full gap-4 flex flex-col bg-[#F4FAFF] overflow-y-auto",
        ),
    )
