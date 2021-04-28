from .create_world import main as create_world
from django.core import management
from time import sleep


def main():
    create_world()
    management.call_command("makemigrations")
    sleep(secs=5)
    management.call_command("migrate")
    sleep(secs=5)


if __name__ == '__main__':
    main()
