from typer import Typer

import app.commands.schema as schema

app = Typer()

app.add_typer(schema.app, name="schema")


def main():
    app()


if __name__ == "__main__":
    main()
