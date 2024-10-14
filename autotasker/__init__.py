import click
from autotasker.scripts.prueba import prueba


@click.group()
def cli():
    """Comando principal de la CLI."""
    pass


@cli.command()
@click.argument('filename')
def docker(filename):
    """Crea un contenedor de docker"""
    click.echo(f'El archivo que quieres convertir en imagen es: {filename}')


'''Hay que añadir contexto en la database'''


@cli.group()
def database():
    """Comandos para gestionar bases de datos."""
@database.command()
def importar_info():
    """Importar datos a una base de datos"""
    click.echo("datos importados")
@database.command()
def copias_seguridad():
    """Crea copias de seguridad"""
    click.echo("copia creada")


if __name__ == '__main__':
    cli()