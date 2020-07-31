# Development Guideline for todo-app

## Getting started

### Prerequisite Software

| **No** | **Name**           | **Version** | **Notes**                                                                        |
| ------ | ------------------ | ----------- | -------------------------------------------------------------------------------- |
| 1      | Python               | 3.7          |
| 2      | Postgres             | \*          |
| 3      | Visual Studio Code | **Latest**  | Required extensions: **EditorConfig for VS Code**, **auto-pep8 - Code formatter** |
| 4      | Docker             | **Latest**  |

### Start application locally

```docker
docker compose up --build
```

### Run test cases

```python
python -m unittest app.to_do_app.tests.test_task_items
```

## What's In This Document

### 1. [Coding convention](/docs/convention.md)

### 2. [Postman collection](https://www.getpostman.com/collections/7d8e95b86a6580474767)
