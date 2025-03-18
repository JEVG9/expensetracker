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
@click.argument('amount', type=float,required=True)
@click.argument('category',required=True)
@click.option('--date', type=str,default=None,help="YYYY-MM-DD")
def adde(description:str,amount:float,category:str,date:str):
    """
    Creates a new expense and adds it to the database.

    Args:
        description (str): The name of the expense.
        amount (float): The amount of the expense.
        category (str): The category of the expense.
        date (str, optional): The date of the expense in YYYY-MM-DD format. Defaults to None.

    Returns:
        None, must print a message to console for K/N.
    """
    if not description.strip() or not category.strip():
        click.echo("ET --> Fields can not be empty")
        return
    dbmanager.add_expense(description, amount, category, date)
    click.echo(f"ET --> Expense '{description}' of ${amount} added under '{category}' category. Date: {date if date else 'Current Timestamp'}")
    
@click.command(short_help="Update the info of an expense")
@click.argument('id',type=int,required=True)
@click.argument('newamount',type=float,required=True)
def upde(id,newamount):
    """
    Modifies an expense only by the amount, can not change anything else.

    Args:
        id(int): Id of the expense.
        newamount(float): New amount of the expense.
    
    Returns:
        None, prints a message to console for K/N.
    """
    if not newamount.strip() or not id.stripe():
        click.echo("ET --> Fields can not be empty")
        return
    dbmanager.mod_expense(id,newamount)
    click.echo(f"ET --> Expense {id} modified")

@click.command(short_help="Delete an expense")
@click.argument('id',type=int,required=True)
def dele(id:int):
    """
    Deltes the expense info from the db.

    Args:
        id(int): Id of the expense
    Returns:
        None, prints a message to console for K/N.
    """
    if not id.stripe():
        click.echo("ET --> Fields can not be empty")
        return
    dbmanager.del_expense(id)
    click.echo(f"ET --> Fields can not be empty")

@click.command(short_help="Shows all expenses")
@click.option('--cat',type=str,default=None,help="category name, no spaces")
def alle(cat:str):
    """
    Shows a list of all expenses with all their info.
    If a category is instroduced it shows all filtered expenses.

    Args:
        cat(str,optional): A str with the category name.
    Returns:
        None, must print the list or an error message.
    """
    print(dbmanager.get_expenses(cat))

@click.command(short_help="Sum all expenses")
@click.option('--m',type=int,default=None,help="01,02,..,12")
@click.option('--y',type=int,default=None,help="1999,2001,..,2014")
@click.option('--c',type=str,default=None,help="comida, transporte")
def sume(m,y,c):
    """
    Sums all expenses and if needed can sum by category and
    or by date.

    Args:
        c(str,optional): A str with the category name.
        m(int,optional): An integer for trhe month.
        y(int,optional): An integer for the year.
    Returns:
        None, must print the list or an error message.
    """
