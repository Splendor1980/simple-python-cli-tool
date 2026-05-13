import click

@click.group()
def cli():
    """Простой CLI инструмент"""
    pass

@cli.command()
@click.option('--name', default='World', help='Имя для приветствия')
def hello(name):
    """Приветствие"""
    click.echo(f'Привет, {name}! 👋')

if __name__ == '__main__':
    cli()