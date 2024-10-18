import click
from autotasker.managers.docker_manager import DockerManager
from InquirerPy import prompt, inquirer


@click.group()
@click.version_option(version="0.1.1", message=f"autotasker 0.1.1")
def cli():
    """Application for Automating Processes."""
    pass


@cli.command()
@click.argument('path')
@click.option('--only-image', is_flag=True, default=False,
              help='Creates only the image, without starting the container.')
@click.option('-env', help='Sets environment variables to be passed to the container during creation.')
@click.option('--env-file', help='Specifies a file containing environment variables to be loaded into the container.')
@click.option('-p', "--port", default=80, help='Specifies the port on which the container will expose its services. '
                                               'Defaults to port 80 if not specified.')
@click.option('-v', "--version", default='lts', help='Defines the version of the language or runtime environment to be '
                                                     'used. If not provided, the latest available version will be used'
                                                     ' by default.')
def docker(path: str, only_image: bool, env: str, env_file: str, port: int, version: str):
    """Creates a Docker container based on user input."""

    click.echo(click.style(" Select the programming language:", bold=True, fg='cyan'))
    languages = [
        {"name": "Django", "value": "django"},
        {"name": "Vite", "value": "vite"},
        {"name": "React (Vanilla)", "value": "react"},
    ]

    questions = [
        {
            "type": "list",
            "message": "Seleccione un lenguaje:",
            "choices": languages,
            "default": "python",
        }
    ]

    selected_language = prompt(questions)

    selected_lang = selected_language[0]
    image_name = inquirer.text(message="Enter the name of the Docker image:").execute()

    container_name = None
    if not only_image:
        container_name = inquirer.text(message="Enter the name of the Docker container:").execute()

    dockermanager = DockerManager(path, selected_lang, image_name, port, container_name, version)

    # Create the Dockerfile
    dockermanager.create_dockerfile()

    # Create the Image
    dockermanager.create_image()

    # Creaate Container
    if not only_image:
        dockermanager.create_container()


# Hay que añadir contexto en la database


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
