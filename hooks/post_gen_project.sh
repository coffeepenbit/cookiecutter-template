#!/bin/bash

set -e

function main() {
    {% if cookiecutter.setup_virtual_environment == "yes" -%}
    setup_python_venv
    install_dev_packages
    {% endif %}
        

    {% if cookiecutter.git_initial_commit == "yes" -%}
    git_initial_commit
    {% endif %}
}


function setup_python_venv() { 
    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install --upgrade pip
    python -m pip install -e .
}


function install_dev_packages() {
    # This requires for source to have been activated for virtual venv
    python -m pip install -r requirements_dev.txt
}


function git_initial_commit() {
    git init

    git config --local user.name {{cookiecutter.author}}
    git config --local user.email {{cookiecutter.email}}

    
    git add .
    git commit -m "Initial commit"

    git branch -M main
    
    git remote add origin git@github.com:{{cookiecutter.author}}/{{cookiecutter.project_slug}}.git
}


main
