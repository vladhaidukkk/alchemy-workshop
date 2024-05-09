from typer import Typer

app = Typer()


@app.command()
def index(name):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    app()
