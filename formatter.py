import sys
from logging import Formatter
import gc
import IPython

from inspect import isclass, ismethod


def resource_module_name(level):
    module_name = sys._getframe(level).f_globals.get('__name__', '__main__')
    if '.' in module_name:
        module_name = '.'.join(module_name.split('.')[:-1])
    return sys._getframe(level), module_name


def find_method_owner(frame):
    code = frame.f_code
    globs = frame.f_globals
    functype = type(lambda: 0)
    funcs = []

    for func in gc.get_referrers(code):
        if type(func) is functype:
            if getattr(func, "func_code", None) is code:
                if getattr(func, "func_globals", None) is globs:
                    funcs.append(func)
                    if len(funcs) > 1:
                        return None

    if funcs:
        func = funcs[0]
    else:
        return None

    for potential_class_name in frame.f_globals:
        potential_class = frame.f_globals[potential_class_name]
        if isclass(potential_class):
            for potential_func_name in dir(frame.f_globals[potential_class_name]):
                potential_func = getattr(potential_class, potential_func_name)
                if ismethod(potential_func):
                    if potential_func.__func__ == func:
                        return potential_class_name


class MyFormatter(Formatter):

    def format(self, record):
        found_logging = False
        level = 0

        while True:
            frame, module_name = resource_module_name(level)

            if module_name == "logging":
                found_logging = True

            elif found_logging:
                break

            level += 1

        name = ""

        potential_owner = find_method_owner(frame)
        if potential_owner:
            name = potential_owner
        else:
            name = frame.f_code.co_name

        return "[%s] %s" % (name, record.getMessage())
