import reflex as rx


def link_button(nombre: str, url: str) -> rx.Component:
    return rx.vstack(
        rx.link(
            rx.button(
                nombre,
                width="100%",
                padding="20px"
            ),
            href=url,
            is_external=True,
            width="100%",
            margin_top="15px",
            margin_bottom="15px"
        )
    )