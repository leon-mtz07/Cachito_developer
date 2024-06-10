import datetime

import reflex as rx


def footer() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.text(f"@Cachito Martínez Tello '2018-{datetime.date.today().year}'",
                    margin_top="10px")
        )
    )
