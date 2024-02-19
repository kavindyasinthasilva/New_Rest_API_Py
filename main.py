
from internal.__init__ import init


def main():
    # Print binary details and terminate the program when --version flag provided.
    print("Main Run")
    init_thread = init()
    init_thread.join()


if __name__ == '__main__':
    main()
