import reflex as rx


def header() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.avatar(
                    src="/Cachito.png",
                    size="9",
                    radius="large",
                ),
                rx.vstack(
                    rx.text(
                        "Cachito Martínez Tello",
                        size="5",
                        weight="bold"
                    ),
                    rx.text(
                        "@CachitoDev",
                        color_scheme="gray",
                        weight="bold",
                    ),
                    rx.center(
                        rx.link(
                            rx.icon_button(
                                rx.icon(tag="github"),
                                is_round=True,
                                variant="soft",
                                size="3",
                            ),
                            href="https://github.com/leon-mtz07",
                            is_external=True,
                        ),
                        rx.link(
                            rx.icon_button(
                                rx.icon(tag="twitter"),
                                is_round=True,
                                variant="soft",
                                size="3"
                            ),
                            href="https://x.com/07_leon20",
                            is_external=True
                        ),
                        rx.link(
                            rx.icon_button(
                                rx.icon(tag="instagram"),
                                is_round=True,
                                variant="soft",
                                size="3"
                            ),
                            href="https://www.instagram.com/leon_mt_07/",
                            is_external=True
                        ),
                        spacing="4",
                        direction="row",
                        width="100%"
                    )
                ),
                justify="center",
                align="center"
            ),
            rx.text(
                "¡Guau! Hola, mi nombre es Cachito"
            ),
            rx.text("""¡Guau! Soy Schnauzer con pasión por la programación. 
                        Mis lenguajes favoritos son Python, C++, y R. Disfruto creando proyectos, automatizando tareas 
                        y analizando datos. Si necesitas un compañero de codificación peludo, ¡estoy aquí! 🐾💻""")

        )
    )
