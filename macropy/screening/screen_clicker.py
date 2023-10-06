import pyautogui

from .models import Box


class ScreenClicker:
    @staticmethod
    def click_in_box(box: Box) -> None:
        x, y = box.x, box.y
        pyautogui.leftClick(x, y)

    @staticmethod
    def track_mouse() -> None:
        pyautogui.mouseInfo()
