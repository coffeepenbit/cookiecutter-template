#!/bin/bash

set -e

function main() {
    setup_python_venv

    {% if cookiecutter.install_dev_packages == "yes" -%}
        install_dev_packages
    {%- else -%}
        install_without_dev_packages
    {% endif %}

    {% if cookiecutter.run_python_tests == "yes" -%}
        run_python_tests
    {% endif %}

    {% if cookiecutter.git_setup == "yes" -%}
        git_setup
    {% endif %}
}


function setup_python_venv() { 
    # TODO dont hardcore python version
    python3.8 -m venv .venv
    source .venv/bin/activate
    python -m pip install --upgrade pip
}


function install_dev_packages() {
    # This requires for source to have been activated for virtual venv
    python -m pip install -r requirements_dev.txt
}


function install_without_dev_packages() {
    python -m pip install -e .
}


function git_setup() {
    git init

    git config --local user.name {{cookiecutter.author}}
    git config --local user.email {{cookiecutter.email}}

    git add .
    git commit -m "Initial commit"
}


main
