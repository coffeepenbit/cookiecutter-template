from {{cookiecutter.project_slug}} import core


def test_main(capsys):
    core.main()
    stdout, _ = capsys.readouterr()

    assert stdout == "Hello, world!\n"
