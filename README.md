# Entrepreneurial Chatbot Assistant

[![Build Status](https://github.com/tommymmcguire/AIPI561/actions/workflows/cicd.yml/badge.svg)](https://github.com/tommymmcguire/AIPI561/actions)

---

## Overview

This project is a Llamafile application that utilizes `llama.cpp` and `Cosmopolitan` to wrap a Large Language Model (LLM) into a single executable file, exposing a local API endpoint. The application includes a frontend interface to interact with the model endpoint and is packaged in a container for portability.

### Walk Through [Youtube Video](https://youtu.be/lIi3pjJlNs0)

## Features

- **LLM Integration:** Incorporates a language model using `llama.cpp`.
- **Single Executable:** Utilizes `Cosmopolitan` to create a single executable file.
- **Local API Endpoint:** Exposes an API endpoint for model interaction.
- **Frontend Interface:** Provides a user-friendly interface to interact with the model.
- **Containerized Deployment:** Packaged in a container for easy deployment and portability.

## Architecture

![Architecture Diagram](https://github.com/user-attachments/assets/f86f591d-d040-4c5d-8986-f982165d9a05)


### Architecture Description

1. **User Interface:**
    - The user interacts with the chatbot through a web interface.
    - User inputs are sent to the backend via HTTP requests.

2. **Frontend:**
    - HTML/CSS and JavaScript files handle the presentation layer.
    - Provides a user-friendly chat interface.

3. **Backend:**
    - Implemented using Flask, which serves the web interface and API endpoints.
    - Receives user messages and sends them to the LLM for processing.
    - Returns the generated responses back to the frontend.

4. **Llamafile:**
    - The Llamafile executable, built with `llama.cpp` and `Cosmopolitan`, contains the LLM model.
    - Processes user inputs and generates responses.

5. **Docker:**
    - The entire application is containerized for portability and easy deployment.
    - Docker Compose is used to manage and run the containers.

## Getting Started

### Prerequisites

- Docker
- Python 3.x
- `llama.cpp`
- `Cosmopolitan`

### Installation

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/tommymmcguire/AIPI561.git
    cd AIPI561
    ```

2. **Build the Llamafile:**
    - Follow the instructions in the [llamafile repository](https://github.com/Mozilla-Ocho/llamafile) to build the Llamafile executable with your model weights in `.gguf` format.
    - You can also download pre-included Llamafiles from the repository.
  
3. **Run the Llamafile locally:**
    - Follow the instructions in the [llamafile repository](https://github.com/Mozilla-Ocho/llamafile) to run the Llamafile locally.
  
### GitHub Secrets Configuration

Before building and running the Docker container, make sure to add your Docker username and password to GitHub Secrets:

1. Navigate to your GitHub repository.
2. Go to `Settings` > `Secrets` > `New repository secret`.
3. Add the following secrets:
   - `DOCKER_USERNAME`: Your Docker Hub username.
   - `DOCKER_PASSWORD`: Your Docker Hub password.

### Modify Docker Commands

Replace `tommymmcguire22` with your Docker Hub username in the following commands:

3. **Build the Docker Container:**
    ```sh
    docker build -t your-docker-username/my-chatbot:latest .
    ```

4. **Run the Docker Container:**
    ```sh
    docker run -p 5001:5001 your-docker-username/my-chatbot:latest
    ```

### Build and Run the Docker Container

**Using Docker:**

```sh
docker build -t your-docker-username/my-chatbot:latest .
docker run -p 5001:5001 your-docker-username/my-chatbot:latest
```

**Using Docker Compose:**

```sh
docker-compose up --build
```

Once the container is built, you can subsequently run the application with:
```sh
docker-compose up
```

### Makefile Commands
1. Install Dependencies
   ```sh
    make install
    ```
2. Lint Code
   ```sh
    make lint
    ```
3. Run Tests
   ```sh
    make test
    ```
4. Run the Application:
   ```sh
    make run
    ```

### Usage

1. **Access the Frontend Interface:**
    Open your web browser and navigate to `http://localhost:5001`.

2. **Interact with the Model:**
    Use the frontend interface to send queries to the model and receive responses.

### Example Usage

<img width="1440" alt="Screenshot 2024-08-05 at 4 43 12 PM" src="https://github.com/user-attachments/assets/214e9b5b-1956-4a4f-ba01-078c852fc79e">



## Model Selection

### Model Used: TinyLlama

For this application, we selected the TinyLlama model for the following reasons:

- **Efficiency:** TinyLlama is optimized for resource efficiency, making it suitable for deployment in environments with limited computational resources.
- **Performance:** Despite its smaller size, TinyLlama offers competitive performance for natural language understanding and generation tasks.
- **Speed:** The model's reduced size allows for faster inference times, which is crucial for providing timely responses in an interactive chatbot application.

## Performance Test Results

### Server Information
- **Server Software:** Werkzeug/3.0.3
- **Server Hostname:** localhost
- **Server Port:** 5001

### Test Document
- **Document Path:** /chat
- **Document Length:** 1755 bytes

### Test Configuration
- **Concurrency Level:** 2
- **Time Taken for Tests:** 321.681 seconds
- **Complete Requests:** 5
- **Failed Requests:** 0
- **Total Transferred:** 9610 bytes
- **Total Body Sent:** 1090 bytes
- **HTML Transferred:** 8775 bytes

### Performance Metrics
- **Requests per Second:** 0.02 [#/sec] (mean)
- **Time per Request:** 128.672 [sec] (mean)
- **Time per Request (across all concurrent requests):** 64.336 [sec] (mean)
- **Transfer Rate:** 
  - 0.03 [Kbytes/sec] received
  - 0.00 [Kbytes/sec] sent
  - 0.03 [Kbytes/sec] total

### Connection Times (sec)
|           | min  | mean   | median | max    |
|-----------|------|--------|--------|--------|
| Connect   | 0.000| 0.001  | 0.000  | 0.002  |
| Processing| 51.626 | 105.149 | 130.478 | 152.437 |
| Waiting   | 51.611 | 105.132 | 130.468 | 152.421 |
| Total     | 51.626 | 105.149 | 130.478 | 152.438 |

**WARNING:** The median and mean for the initial connection time are not within a normal deviation. These results are probably not that reliable.

### Percentage of Requests Served Within a Certain Time (sec)
- 50%  117.622
- 66%  143.335
- 75%  143.335
- 80%  152.438
- 90%  152.438
- 95%  152.438
- 98%  152.438
- 99%  152.438
- 100%  152.438 (longest request)

## Project Structure

- `.github/workflows/ci.yml`: GitHub Actions configuration for Continuous Integration/Continuous Deployment.
- `src/frontend/static/style.css`: CSS file for styling the frontend.
- `src/frontend/templates/index.html`: HTML template for the frontend.
- `src/tests/test_app.py`: Unit tests for the application.
- `src/app/app.py`: Main application file.
- `Dockerfile`: Docker configuration for building the container.
- `docker-compose.yml`: Docker Compose configuration.
- `Makefile`: Makefile for automating tasks.
- `performance_test.sh`: Script for running performance tests.
- `requirements.txt`: Python dependencies.

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [llama.cpp](https://github.com/Mozilla-Ocho/llamafile)




