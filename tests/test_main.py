from py_dev import hello, main


def test_hello():
    assert hello() == "Hello, World!"
    assert hello("Antigravity") == "Hello, Antigravity!"


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out
