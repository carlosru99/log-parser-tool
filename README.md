# Log Parser Tools
Log Parser Tool for Clarity AI technical interview
## Setup

### Requirements

* Python ^3.8+
* Poetry

### Get ready

#### Install python 3.8.10

- **Recommended:** pyenv:

    ```bash
    $ pyenv install 3.8.10
    ```

    ```bash
    $ pyenv local 3.8.10
    ```

#### Install poetry and get into virtual environment

```bash
$ pip install poetry
```

- Install needed packages defined in pyproject.toml

```bash
$ poetry install
```
- Enter Poetry's environment

```bash
$ poetry shell
```

## Usage
 - Run main parser: **Example**

```bash
$ make run-main-parser FILE='"log.txt"' INIT_DATE='"2019-02-21 14:34:24"' END_DATE='"2019-08-13 06:05:24"' HOST='"Zaiden"'
```

 - Run tests for main parser: Example

```bash
make test-main-parser
```

 - Run unlimited parser

```bash
make run-unlimited-parser FILE='"log.txt"' HOST_FROM='"Aralis"' HOST_TO='"Zaiden"'
```