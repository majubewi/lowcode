# For addition markdown and emoji in print()
from rich import print
print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())

# For pretty printing any data structures in console
from rich import pretty
pretty.install()

# Inspect type and methods of a object
from rich import inspect
inspect(str,methods=True)



