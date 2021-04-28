from django.core import management
from time import sleep


def main():
    management.call_command("shell" "< create_world.py")
    management.call_command("makemigrations")
    sleep(secs=5)
    management.call_command("migrate")
    sleep(secs=5)


if __name__ == '__main__':
    main()
