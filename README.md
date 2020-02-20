# OpenFaaS Template using Python 3 and Twisted

Python/Twisted templates that make use of the incubator project of-watchdog.

Templates available in this repository:

- python3-twisted

## Downloading the templates

```shell
faas template pull https://github.com/openfaas-incubator/python-flask-template
```

## Using the python3-http templates

Create a new function

```shell
faas new --lang python3-twisted <fn-name>
```

Build, push, and deploy

```shell
faas up -f <fn-name>.yml
```

Set your OpenFaaS gateway URL. For example:

```shell
OPENFAAS_URL=http://127.0.0.1:8080
```

Test the new function

```shell
curl -i $OPENFAAS_URL/function/<fn-name>
```
