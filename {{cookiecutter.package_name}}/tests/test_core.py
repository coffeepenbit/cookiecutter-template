from {{cookiecutter.package_name}} import core


def test_main(capsys):
    core.main()
    stdout, _ = capsys.readouterr()

    assert stdout == "Hello, world!\n"