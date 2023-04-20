# Docker for Machine Learning

This project includes two sub-projects that are represent two parts of a Machine Learning initiative. A model training pipeline exists in the [pipeline/](./pipeline/) directory. A REST API web application exists in the [app/](./app/) directory to perform inference with the trained model.

Each sub-project includes a `README` with more details about the application and how it can be run. We will work on writing the `Dockerfile` as well as the build and run commands in our lab activity.

## Why Docker

Both sub-projects include a significant amount of python dependencies; there is some overlap as well as some unique packages used in each. To simplify the development and deployment of these applications, we will use Docker to build deterministic, platform-agnostic **Images**. The same images we run on our laptops could be run in a production setting on some application server, kubernetes cluster, or other distributed workflow service.

See more about Docker in the included [Dockerfile Basics](./dockerfile-basics.md) file.

## Activity

You should examine the included applications and their respective `pyproject.toml` files. This will help you get a feel for their dependencies and how they relate to each other. You should then perform the following:

- [ ] write `pipeline/Dockerfile`
- [ ] write and document `docker build ...` and `docker run ...` commands that make proper use of the application (saved artifacts should be persisted to your local filesystem)
- [ ] write `app/Dockerfile`
- [ ] write and document `docker build ...` and `docker run ...` commands that make proper use of the application (web application should be exposed/accessible from localhost in your browser)
- [ ] BONUS: write a `./Dockerfile` that makes use of multi-stage builds to run the pipeline during the build-phase and copy its artifacts to the second stage which serves the inference application

## Running Locally

Lastly, each sub-project also uses `poetry` to define the python package, manage its dependencies, and build the environment. Poetry is a great tool for creating python packages; you can read more about it [below](#setting-up-and-using-poetry).

Poetry keeps dependencies listed in `pyproject.toml` files and explicitly enumerated in `poetry.lock`. These files can be used to create new virtual environments; poetry can also export these dependencies to a `requirements.txt` file to be used with other virtual environment management solutions.

We will talk more about Poetry in a later lab session. For now, you are welcome to read about it and try it out, or just create a standard virtual environment with the following (run from each of the sub-project directories):

```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

NOTE: make sure you run the above with a version of python >= 3.9

## Makefile

Both sub-projects also include the start of a Makefile to simplify the execution of common commands used for building and running the application. We will not cover Makefile's in depth this year, but you can read about them in this [Makefile Lab from last year](https://github.com/MSIA/423-makefile-lab-activity). The major caveat is that `make` is not compatible with Windows machines. In this project, we will use them as a simple way for documenting and executing lengthy shell commands. For example:

```shell
make requirements
```

instead of:

```shell
poetry export -f requirements.txt --output requirements.txt --without-hashes
```

## Setting up and using Poetry

Poetry is a dependency manager and build tool for Python. It simplifies package management by creating and managing virtual environments for your projects and providing a consistent interface to install and manage dependencies.

### Installing Poetry

To install Poetry, follow the instructions on the official documentation [here](https://python-poetry.org/docs/#installation). The recommended installation method is using the installer script via `curl` or `wget`.

### Installing dependencies

After installing Poetry, you can install the project dependencies by running the following command in the root directory of each application:

```sh
poetry install
```

This will create a virtual environment for the project and install all the dependencies listed in the `pyproject.toml` file.

### Running the applications

To run the pipeline application, activate the virtual environment created by Poetry and run the script:

```sh
poetry run python src/pipeline.py
```

To run the FastAPI application, activate the virtual environment created by Poetry and start the server:

```sh
poetry run uvicorn src.app:app --reload
```

The `--reload` flag enables hot-reloading, which automatically reloads the server when changes are made to the code. You can access the FastAPI application by visiting `http://localhost:8000` in your web browser.

### Updating dependencies

To update dependencies, you can run the following command:

```sh
poetry update
```

This will update all the dependencies to their latest compatible versions and regenerate the virtual environment.
