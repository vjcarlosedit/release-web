import flet as ft

def main(page: ft.Page):

    page.title = "Contador"
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = "auto"
    page.appbar = ft.AppBar(title=ft.Text("Contador"),
                          center_title=True,
                          bgcolor="blue201",
                          color="white")

    counter = ft.Text("0", size=40)

    def increment(e):
        counter.value = str(int(counter.value) + 1)
        page.update()

    def decrement(e):
        counter.value = str(int(counter.value) - 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=decrement),
                counter,
                ft.IconButton(ft.icons.ADD, on_click=increment),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(main, view=ft.AppView.WEB_BROWSER)