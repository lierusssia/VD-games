try:
    from VD_games.scripts.VD_games import greet
except ModuleNotFoundError:
    from VD_games import greet


def main():
    greet()


if __name__ == "__main__":
    main()
