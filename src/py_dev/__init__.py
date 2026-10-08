def hello(name: str = "World") -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def main() -> None:
    print(hello())


if __name__ == "__main__":
    main()
