import random
import time
from abc import ABC, abstractmethod
from pathlib import Path

from macroing.exceptions import ForceStopError
from screening import ScreenVerifier, ScreenClicker


class Step(ABC):
    def __init__(self):
        self.result: bool = False

    @abstractmethod
    def execute(self) -> None:
        pass

    def __str__(self) -> str:
        return f"Step()"


class ForceStopStep(Step):
    def __init__(self):
        super().__init__()

    def execute(self) -> None:
        print(self)
        raise ForceStopError

    def __str__(self) -> str:
        return f"StopStep()"


class WaitStep(Step):
    def __init__(self, min_seconds: int, max_seconds: int):
        super().__init__()
        self.min_seconds = min_seconds
        self.max_seconds = max_seconds

    def execute(self) -> None:
        print(self)
        time.sleep(random.randint(self.min_seconds, self.max_seconds))
        self.result = True

    def __str__(self) -> str:
        return f"WaitStep(min_seconds='{self.min_seconds}', max_seconds='{self.max_seconds}')"


class ClickStep(Step):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y

    def execute(self) -> None:
        print(self)
        self.result = True

    def __str__(self) -> str:
        return f"ClickStep(x='{self.x}', y='{self.y}')"


class TextLocateStep(Step):
    def __init__(self, text: str):
        super().__init__()
        self.text = text

    def execute(self) -> None:
        print(self)

        if self.text == "Texto 1":
            self.result = True
        else:
            self.result = False

    def __str__(self) -> str:
        return f"TextLocateStep(text='{self.text}')"


class ImageLocateStep(Step):
    def __init__(self, image_path: Path):
        super().__init__()
        self.image_path = image_path

    def execute(self) -> None:
        print(self)
        if ScreenVerifier.image_in_screen(self.image_path) is not None:
            self.result = True

    def __str__(self) -> str:
        return f"ImageLocateStep(image_path='{self.image_path}')"


class ClickImageLocateStep(Step):
    def __init__(self, image_path: Path):
        super().__init__()
        self.image_path = image_path

    def execute(self) -> None:
        print(self)
        box = ScreenVerifier.image_in_screen(self.image_path)
        if box is not None:
            ScreenClicker.click_in_box(box)
            self.result = True

    def __str__(self) -> str:
        return f"ClickImageLocate(image_path='{self.image_path}')"
