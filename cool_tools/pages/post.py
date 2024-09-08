import reflex as rx


def post_page() -> rx.Component:
    return rx.container(
        rx.link(
            rx.button(
                "Post2Soap",
                href="",
            )
        ),
        rx.link(rx.button("Back to Home"), href="/"),
    )
