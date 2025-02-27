import click
import dbmanager
import csv_generator

@click.command(short_help="Show help for a specific command or list all commands")
@click.argument('command',required=False)
@click.pass_context
def htl(ctx,command):
    """
    Displays help for a specific command or lists all available commands.

    If a command name is passed, it provides detailed help for that command.
    Otherwise, it lists all available commands with their short descriptions.

    Parameters:
        ctx (click.Context): The context object to find the root CLI group.
        command (str, optional): The name of the command to show help for.

    Example Usage:
        - To list all commands:
          `python cli.py htl`
        - To get detailed help for a specific command:
          `python cli.py htl <command_name>`
    """
    cli=ctx.find_root().command
    if not command:
        click.echo("ET --> Available commands:")
        for cmd_name, cmd in cli.commands.items():
            click.echo(f" - {cmd_name}: {cmd.short_help}")
    elif command in cli.commands:
        cmd = cli.commands[command]
        click.echo(f"Help for '{command}':")
        click.echo(cmd.get_help(ctx))
    else:
        click.echo(f"ET --> Error: Command '{command}' does not exist.")


@click.command(short_help="Creates a new expense")
@click.argument('description',required=True)
@click.argument('amount',required=True)
def adde(description:str,amount:int):pass

@click.command(short_help="Update the info of an expense")
@click.argument()
def upde():pass

@click.command(short_help="Delete an expense")
@click.argument()
def dele():pass

@click.command(short_help="Shows all expenses")
@click.argument()
def alle():pass

@click.command(short_help="Sum all expenses")
@click.argument()
def sume():pass

@click.command(short_help="Sum all expenses of a month")
@click.argument()
def msme():pass