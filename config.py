import tomllib

import singleton


def init_config():
    try:
        with open("config.toml", "rb") as f:
            singleton.options = tomllib.load(f)
    except OSError:
        read_default_config()
    else:
        print("It seems there was a problem reading your config.")
        print("Please check it and fix any syntax or logical error.")
        print("Falling back to use default settings.")
        read_default_config()


def read_default_config():
    try:
        with open("default-config.toml", "rb") as f:
            singleton.options = tomllib.load(f)
    except OSError:
        print("Cannot find default config file. Exiting...")
        exit(1)
