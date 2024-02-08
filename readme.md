# Flask User CRUD Task

## Overview

This project involves the development of a User CRUD REST API deployed on AWS Lambda serverless architecture using an
RDS PostgreSQL database. The API provides basic operations for user management, and the deployment process includes
Continuous Integration (CI) and Continuous Deployment (CD) pipelines for automatic deployment upon committing to the
main branch.

## Project Structure

The project includes the following key components:

- **Flask App:** The Flask application provides the CRUD functionality for user management.
- **AWS RDS:** Amazon RDS is utilized as the PostgreSQL database for storing user data.
- **CI/CD Pipelines:** Automated CI/CD pipelines ensure seamless deployment upon any commit to the main branch.
- **Pre-commit Hooks:** Pre-commit hooks are integrated to enforce coding standards before each commit.

## Commands Used

- **Initialization:**
  ```bash
  flask db init

- **Generate Migration:**
  ```bash
  flask db migrate -m "Initial migration"
- **Apply Migration:**

  ```bash
  flask db upgrade
- **Run Server:**

  ```bash
  flask run --port 3005

- **Pre-commit Installation:**

  ```bash
  brew install pre-commit
  pip install pre-commit
  pre-commit install
  pre-commit run --all-files

- **Additional Server Run Options:**

  ```bash
  flask run

  # or

  flask run --port 7777

- **AWS Deployment Endpoint**

  Development : https://i6j544m2mg.execute-api.ap-south-1.amazonaws.com/dev


- **Postman Collection**
  A public Postman collection is available for testing the API. Postman Collection.
-
  https://www.postman.com/premanathpythondeveloper/workspace/icompass-user-crud/collection/10688946-6b7ce632-c4cc-4c90-af88-adcb67c54068?action=share&creator=10688946
