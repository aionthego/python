from py_dev import main


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello from py-dev!" in captured.out
