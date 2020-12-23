#From https://github.com/tmbo/questionary#installation
#AND https://github.com/tiangolo/typer

# Requirements via pip3: typer and questionary
import typer
import questionary #Question types: https://questionary.readthedocs.io/en/stable/pages/types.html
from jcache import JCache

app = typer.Typer()


@app.command()
def hello(name: str):
    last_name = questionary.text(f"Hello {name}, what's your last name?").ask()

    typer.echo(f"Okay, {name} {last_name}. Welcome to the Lasagne Devlivery Express.")


@app.command()
def order(name: str, formal: bool = False):

    # Introduction to order a Lasagne
    if formal:
        typer.echo(f"""I will ask you some question Mr./Ms. {name} and you can tell me how you would like to
            have your lasagne. I then will write down these things and we will make the lasagne.""")
    else:
        typer.echo(f"{name}, you have some options for the lasagne.")

    # Ask for sauce (multichoice)
    sauce = questionary.checkbox(
        'Select Sauce',
        choices=[
            "Tomato",
            "Tomato (vegetarian)",
            "Bechamel",
    ]).ask()

    # Ask for cheese
    cheese = questionary.confirm('With cheese?').ask()

    # Select Herbs
    herbs = questionary.select(
        'Select Herb',
        choices=[
            "Parsley",
            "Basil"
    ]).ask()

    # Collect order data
    order = {
        "name" : name,
        "sauce" : sauce,
        "cheese" : cheese,
        "herbs" : herbs
    }


    # Save order to cache
    cache = JCache()
    import random
    id = random.randint(0,20000000)
    cache.stash(id, order)

    # Answer
    typer.echo(f"{name}, please come back in 15 minutes. Your id is {id}.")

@app.command()
def take(id: int):

    # Load order from cachefile
    cache = JCache()
    order = cache.fetch(id)

    # Answer
    typer.echo(f"Welcome back {order['name']}. Your Lasagne is ready.")

if __name__ == "__main__":
    app()