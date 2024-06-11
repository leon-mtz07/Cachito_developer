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
                "Woof! Hi, my name is Cachito"
            ),
            rx.text("""**Woof! I'm a Schnauzer with a passion for programming. 
            My favorite languages are Python, C++, and R. I enjoy creating projects, automating tasks, and analyzing 
            data. If you need a furry coding companion, I'm here!** 🐾💻""")

        )
    )
