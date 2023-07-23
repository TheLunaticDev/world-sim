from initialize import initialize
from main_loop import main_loop
from shutdown import shutdown


def main():
    initialize()
    main_loop()
    shutdown()


if __name__ == '__main__':
    main()
