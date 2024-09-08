"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from . import pages


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.vstack(
            rx.link(
                rx.heading(
                    "Cool Tools!",
                    as_="h1",
                    size="9",
                    _hover={"cursor": "pointer", "color": "rgb(194, 46, 72)"},
                ),
                href="/post",
                underline="none",
            ),
            spacing="5",
            align="center",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
app.add_page(pages.post_page, route="/post")
