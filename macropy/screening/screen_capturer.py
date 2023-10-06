import pyautogui
from typing import Tuple
from PIL.Image import Image
from pynput import mouse
from pynput.mouse import Button

from .models import Position


class ScreenCapturer:
    def __init__(self):
        self._screen_size = pyautogui.size()
        self._start_position: Position | None = None
        self._end_position: Position | None = None

    def capture(self) -> Image:
        self._listen()
        return self._screenshot()

    def _listen(self) -> None:
        capturing = True
        listener = mouse.Listener(on_click=self._on_click)
        listener.start()
        while capturing:
            if self._start_position is not None and self._end_position is not None:
                capturing = False

    def _on_click(self, x: int, y: int, button: Button, pressed: bool) -> None:
        if self._is_inside_screen(x, y):
            if pressed:
                self._start_position = Position(x, y)
            else:
                self._end_position = Position(x, y)

    def _is_inside_screen(self, x: int, y: int) -> bool:
        return 0 <= x <= self._screen_size[0] and 0 <= y <= self._screen_size[1]

    def _screenshot(self) -> Image:
        left, width = self._get_min_and_difference(self._start_position.x, self._end_position.x)
        top, height = self._get_min_and_difference(self._start_position.y, self._end_position.y)
        return pyautogui.screenshot(region=(left, top, width, height))

    @staticmethod
    def _get_min_and_difference(a: int, b: int) -> Tuple[int, int]:
        _min = min(a, b)
        _difference = abs(a - b)
        return _min, _difference
