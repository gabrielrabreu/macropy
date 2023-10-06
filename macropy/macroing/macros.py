from typing import List, Union

from .exceptions import StopError
from .steps import Step


class Alternate:
    def __init__(self, success: 'Macro', failure: 'Macro'):
        self.success = success
        self.failure = failure


class Wrapper:
    def __init__(self, step: Step, alternate: Union[Alternate, None] = None):
        self.step = step
        self.alternate = alternate

    def has_alternates(self) -> bool:
        return self.alternate is not None

    def execute(self):
        self.step.execute()

    def alternate_success(self):
        self.alternate.success.execute()

    def alternate_failure(self):
        self.alternate.failure.execute()


class Macro:
    def __init__(self):
        self.wrappers: List[Wrapper] = []

    def add_step(self, step: Step, alternate: Union[Alternate, None] = None) -> 'Macro':
        self.wrappers.append(Wrapper(step, alternate))
        return self

    def execute(self) -> None:
        for index, wrapper in enumerate(self.wrappers, start=1):
            wrapper.step.execute()
            result = wrapper.step.result

            if wrapper.has_alternates():
                if result:
                    wrapper.alternate_success()
                else:
                    wrapper.alternate_failure()
            else:
                if result is False:
                    raise StopError(str(wrapper.step))
