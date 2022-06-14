# Voter

## Setup environment (Unix-*like*)

1. Install requirements
    ```bash
    pip install -r requirements.txt
    ```

2. Run the command below to start the *name server*
    ```bash
    pyro5-ns
    ```

## Setup environment (Windows)

If you are on windows and follow the steps above, when you run `server.py`, you will get the following error:

```bash
AttributeError: module 'signal' has no attribute 'SIGALRM'
```

This is because the `SIGALRM` attribute exists only for unix like systems. In this case, upload a `docker` container and run the application, whose steps are below in **"Setup environment with docker"**.

## Setup environment with `docker`

1. Build the `Dockerfile` image
    ```bash
    docker build -t <image_name> .
    ```

2. Create the container
    ```bash
    docker run -it --name <container_name> -dp 80:80 <image_name>
    ```

3. Access the container terminal
    ```bash
    docker exec -it <container_name> bash
    ```

4. Follow the steps of **"usage"** below, for the same container where the name server was started

## Usage

1. Go to the correct directory
    ```bash
    cd src
    ```

2. Start the server passing its name as an argument (`<server_name>`)
    ```bash
    python server.py <server_name>
    ```

3. Run the client by passing the same server name given
    ```bash
    python client.py <server_name>
    ```