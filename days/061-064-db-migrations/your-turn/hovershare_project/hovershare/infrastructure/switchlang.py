import uuid
from typing import Callable, Any


class switch:
    """
        python-switch is a module-level implementation of the switch statement for Python.
        See https://github.com/mikeckennedy/python-switch for full details.
        Copyright Michael Kennedy (https://twitter.com/mkennedy)
    """
    __no_result = uuid.uuid4()
    __default = uuid.uuid4()

    def __init__(self, value):
        self.value = value
        self.cases = set()
        self._found = False
        self.__result = switch.__no_result
        self._falling_through = False
        self._func_stack = []

    def default(self, func: Callable[[], Any]):
        """
            Use as option final statement in switch block.

            with switch(val) as s:
               s.case(...)
               s.case(...)
               s.default(function)

        :param func: Any callable taking no parameters to be executed if this (default) case matches.
        :return: None
        """
        self.case(switch.__default, func)

    def case(self, key, func: Callable[[], Any], fallthrough=False):
        """
            Specify a case for the switch block:

            with switch(val) as s:
               s.case('a', function)
               s.case('b', function, fallthrough=True)
               s.default(function)

        :param key: Key for the case test (if this is a list or range, the items will each be added as a case)
        :param func: Any callable taking no parameters to be executed if this case matches.
        :param fallthrough: Optionally fall through to the subsequent case (defaults to False)
        :return:
        """
        if fallthrough is not None:
            if self._falling_through:
                self._func_stack.append(func)
                if not fallthrough:
                    self._falling_through = False

        if isinstance(key, list) or isinstance(key, range):
            found = False
            for i in key:
                if self.case(i, func, fallthrough=None):
                    found = True
                    if fallthrough is not None:
                        self._falling_through = fallthrough
            return found

        if key in self.cases:
            raise ValueError("Duplicate case: {}".format(key))
        if not func:
            raise ValueError("Action for case cannot be None.")
        if not callable(func):
            raise ValueError("Func must be callable.")

        self.cases.add(key)
        if key == self.value or not self._found and key == self.__default:
            self._func_stack.append(func)
            self._found = True
            if fallthrough is not None:
                self._falling_through = fallthrough
            return True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            raise exc_val

        if not self._func_stack:
            raise Exception("Value does not match any case and there "
                            "is no default case: value {}".format(self.value))

        for func in self._func_stack:
            # noinspection PyCallingNonCallable
            self.__result = func()

    @property
    def result(self):
        if self.__result == switch.__no_result:
            raise Exception("No result has been computed (did you access "
                            "switch.result inside the with block?)")

        return self.__result


def closed_range(start: int, stop: int, step=1) -> range:
    if start >= stop:
        raise ValueError("Start must be less than stop.")

    return range(start, stop + step, step)
