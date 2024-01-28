import flet as ft
from common_utils import generate_password, copy_to_clip

def main(page: ft.Page):
    page.title = "Password Generator"
    page.window_width = 600
    page.window_height = 700


    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK


    # Appbar
    page.appbar = ft.AppBar(
        title=ft.Text(
            value="Password Generator",
            color=ft.colors.WHITE,
            style=ft.TextThemeStyle.HEADLINE_MEDIUM,
            weight=ft.FontWeight.W_400
        ),
        leading=ft.Icon(
            name=ft.icons.KEY_ROUNDED,
        ),
        bgcolor="#212121"
    )

    info_text = ft.Text(
        value="Which of the following would you like to include in your password?",
        text_align=ft.TextAlign.CENTER,
        style=ft.TextThemeStyle.LABEL_LARGE,
        expand=True
    )

    lower_chbox = ft.Checkbox(
        label="Lowercase Letters (a-z)",
        value=True
    )

    upper_chbox = ft.Checkbox(
        label="Uppercase Letters (A-Z)",
        value=True
    )
    
    digits_chbox = ft.Checkbox(
        label="Digits (1-9)",
        value=True
    )

    special_chbox = ft.Checkbox(
        label="Special characters (!,@, &, %, $, etc.)",
        value=True
    )

    pass_field = ft.TextField(
        value="Password will be shown here.",
        disabled=True,
        dense=True,
        border_color=ft.colors.WHITE,
    )

    def close_dlg(e):
        custom_dlg.open = False
        page.update()

    custom_dlg = ft.AlertDialog(
        modal=True,
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.dialog = custom_dlg

    def show_dlg(title, content):
        custom_dlg.title=ft.Text(title)
        custom_dlg.content=ft.Text(content)
        custom_dlg.open = True
        page.update()

    def generate_clicked(e):
        chars = []

        if lower_chbox.value:
            chars.append("lowercase")
        if upper_chbox.value:
            chars.append("uppercase")
        if digits_chbox.value:
            chars.append("digits")
        if special_chbox.value:
            chars.append("special")

        if not chars:
            show_dlg("Insufficient input", "You must choose at least one category.")
            return
        
        if not length_field.value:
            show_dlg("No password length given", "Please provide a length for the password.")
            return
            

        if not length_field.value.isdigit() or not int(length_field.value) > 0:
            show_dlg("Invalid length", "Password length must be an integer greater than 0.")
            return


        pwd = generate_password(int(length_field.value), chars)
        pass_field.disabled = False
        pass_field.value = pwd
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Password copied to clipboard."),
        )
        page.snack_bar.open = True
        copy_to_clip(pwd)
        page.update()


    generate_btn = ft.OutlinedButton(
        text="Generate",
        on_click=generate_clicked
    )

    length_field = ft.TextField(
        label = "Length",
        dense=True,
        width=200
    )


    
    page.add(
        ft.Row(
            controls = [
                info_text,
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls = [
                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    # horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        lower_chbox,
                        upper_chbox,
                        digits_chbox,
                        special_chbox,
                        ft.Row(
                            controls = [
                                ft.Text(
                                    value="Password length: ",
                                    style=ft.TextThemeStyle.LABEL_LARGE
                                ),
                                length_field,
                            ]
                        ),
                        generate_btn,
                        
                    ]
                ),
                
            ]
        ),
        ft.Divider(),
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls = [
                pass_field,
            ]
        )
    )

    page.update()


ft.app(target=main, view=ft.AppView.WEB_BROWSER)