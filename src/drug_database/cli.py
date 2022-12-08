"""Console script for drug_database."""
import json as _json

import typer
from rich.console import Console
from rich.table import Table

from ._drug_database import get_drug_factors

app = typer.Typer()


def version_callback(show_version: bool):
    """Prints version information."""
    if show_version:
        from . import __version__, __program_name__

        typer.echo(f"{__program_name__} {__version__}")
        raise typer.Exit()


def license_callback(show_license: bool):
    """Prints license information."""
    if show_license:
        from . import __license__

        typer.echo(f"{__license__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Show version",
    ),
    license: bool = typer.Option(
        None,
        "--license",
        callback=license_callback,
        is_eager=True,
        help="Show license",
    ),
):
    # Do other global stuff, handle other global options here
    return


@app.command(help="List all drugs")
def list_drugs():
    drugs = get_drug_factors()
    table = Table(title="Drugs")

    table.add_column("Name", justify="right", style="cyan", no_wrap=True)

    for drug in drugs.keys():
        # print(name)
        table.add_row(drug)

    console = Console()
    console.print(table)


@app.command(help="Show all factors for a given drug and FPC")
def show_drug(
    drug_name: str,
    fpc: int = typer.Option(1, help="Number of times FPC"),
    json: bool = typer.Option(
        False,
        help="Display out point in json format. The default is to show a rich table",
    ),
):
    drugs = get_drug_factors()

    # All keys are capitalized
    drug_name = drug_name.capitalize()
    if drug_name not in drugs:
        typer.echo(f"Invalid drug name {drug_name}", err=True)
        raise typer.Exit(101)

    drug = drugs[drug_name]
    if str(fpc) not in drug:
        typer.echo(
            f"Invalid fpc {fpc} for drug {drug_name}, expected one of {list(drug.keys())}",
            err=True,
        )
        raise typer.Exit(101)

    data = drug[str(fpc)]
    console = Console()
    if json:
        console.print(_json.dumps(data))
    else:
        table = Table(title=f"Scaling factors for drug {drug_name} and FPC {fpc}")

        table.add_column("Name", justify="right", style="cyan", no_wrap=True)
        table.add_column("Value", style="magenta")

        for k, v in data.items():
            table.add_row(k, str(v))

        console.print(table)
