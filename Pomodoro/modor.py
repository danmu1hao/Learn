import flet as ft
import time
import threading

def main(page: ft.Page):
    # 设置窗口初始属性
    page.title = "番茄钟 Pomodoro Timer"
    page.window_resizable = True                  # ✅ 允许缩放
    page.window_always_on_top = True              # ✅ 窗口总在最前面
    page.window_width = 300
    page.window_height = 250

    is_transparent = False
    timer_value = ft.Text(value="00:00", size=40, text_align="center")
    input_minutes = ft.TextField(label="设置时间（分钟）", keyboard_type="number", value="25")
    
    start_button = ft.ElevatedButton(text="开始")
    transparent_button = ft.ElevatedButton(text="窗口透明化")
    resize_button = ft.ElevatedButton(text="调整窗口大小")

    def countdown(minutes):
        total_seconds = int(minutes) * 60
        while total_seconds > 0:
            mins, secs = divmod(total_seconds, 60)
            timer_value.value = f"{mins:02d}:{secs:02d}"
            page.update()
            time.sleep(1)
            total_seconds -= 1
        timer_value.value = "00:00"
        page.update()
        page.dialog = ft.AlertDialog(title=ft.Text("时间到！休息一下吧！"))
        page.dialog.open = True
        page.update()
        start_button.disabled = False

    def start_timer(e):
        if input_minutes.value.isdigit():
            start_button.disabled = True
            page.update()
            t = threading.Thread(target=countdown, args=(input_minutes.value,))
            t.start()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("请输入有效的分钟数"))
            page.snack_bar.open = True
            page.update()

    def toggle_opacity(e):
        nonlocal is_transparent
        if not is_transparent:
            page.window_opacity = 0.6
            transparent_button.text = "恢复不透明"
        else:
            page.window_opacity = 1.0
            transparent_button.text = "窗口透明化"
        is_transparent = not is_transparent
        page.update()

    def resize_window(e):
        page.window_width = 250
        page.window_height = 180
        page.update()

    # 注册事件
    start_button.on_click = start_timer
    transparent_button.on_click = toggle_opacity
    resize_button.on_click = resize_window

    # 使用 expand=True 让组件随窗口缩放
    page.add(
        ft.Column([
            ft.Text("番茄钟 - Pomodoro", size=24, text_align="center"),
            input_minutes,
            timer_value,
            ft.Row([start_button, transparent_button, resize_button], alignment="center")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10)
    )

    # 再次设置窗口大小，防止被内容撑大
    page.window_width = 300
    page.window_height = 250
    page.update()

ft.app(target=main)
