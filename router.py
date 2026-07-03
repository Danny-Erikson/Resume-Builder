from commands.build import build
from commands.update import update


ROUTES = {
    "build": build,
    "update": update,
}


def route(action, extra_args=None):
    if extra_args is None:
        extra_args = []

    command = ROUTES.get(action)

    if command is None:
        print(f"Unknown command: {action}")
        return

    command(extra_args)
