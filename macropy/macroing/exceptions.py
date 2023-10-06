class ForceStopError(Exception):
    def __init__(self):
        super().__init__("Forced stop execution.")


class StopError(Exception):
    def __init__(self, details: str):
        super().__init__(f"Stopping execution due to failure and no alternate flow setted. "
                         f"{details}.")
