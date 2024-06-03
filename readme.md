# Docker Swarm Test App

This is a simple Flask application used to test Docker and Docker Swarm.

## Description

This application provides basic arithmetic operations through different endpoints (`add`, `sub`, `div`, `mul`). It accepts two parameters (`num1` and `num2`) and performs the specified operation on them.

## Installation

1. Clone the repository:

    ```bash
    git clone <repo_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd <project_directory>
    ```

3. Build the Docker image:

    ```bash
    docker build -t testapp .
    ```

4. Run the Docker container:

    ```bash
    docker run -p 5000:5000 testapp
    ```

## Usage

- Access the endpoints using the following format:

    ```
    http://localhost:5000/<operation>?num1=<number>&num2=<number>
    ```

    Replace `<operation>` with one of: `add`, `sub`, `div`, `mul`, `<number>` with numerical values.

    Example:

    ```
    http://localhost:5000/div?num1=10&num2=2
    ```

## Endpoints

- `/`: Provides information about available endpoints and an example request.
- `/add`: Adds two numbers.
- `/sub`: Subtracts two numbers.
- `/div`: Divides two numbers.
- `/mul`: Multiplies two numbers.
