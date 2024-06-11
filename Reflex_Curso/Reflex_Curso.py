"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from Reflex_Curso.views.header.header import header
from Reflex_Curso.components.link_button import link_button
from Reflex_Curso.components.footer import footer


class State(rx.State):
    ...


@rx.page(
    title="Cachito",
    description="This is a page to describe something about myself, even if it's something brief.",
    image="/assets/Cachito.png",
    meta=[
        {"name": "theme_color", "content": "FFFFFF"},
        {"char_set": "UTF-8"},
        {"property": "og:url", "content": "url"}
    ]
)
def index() -> rx.Component:
    return rx.center(
        # Aquí es para el botón que hace cambiar de color toda la página
        rx.color_mode.button(
            position="top-right",
            size="4",
            border="1px solid gray"
        ),
        rx.card(
            # Esto es para la presentación del Cachito
            header(),
            # Esto sería para poner una división para luego poner los links de interés
            rx.hstack(
                rx.divider(margin="0"),
                rx.text(
                    "🐾Useful links to help you become as good as I am.🐾",
                    weight="bold",
                    white_space="nowrap",
                    size="3",
                ),
                rx.divider(margin="0"),
                align="center",
                width="100%",
                margin_top="15px",
                margin_bottom="15px",
                min_width="430px"
            ),
            # Estos son los links de interés
            link_button("UDEMY", "https://www.udemy.com"),
            link_button("MOUREDEV", "https://www.youtube.com/@mouredev"),
            link_button("QUANT TRADING", "https://www.youtube.com/@DimitriBianco"),
            link_button("JETBRAINS", "https://www.jetbrains.com"),
            link_button("PYCHARM", "https://www.jetbrains.com/pycharm/"),
            link_button("VISUAL STUDIO CODE", "https://code.visualstudio.com"),
            footer(),
            size="4",
            max_width="35em",
            width="100%",
            margin_top="50px",
            box_shadow="5px 5px 5px 0px gray",
            direction="column",
        ),
    )


app = rx.App()
app.add_page(index)
