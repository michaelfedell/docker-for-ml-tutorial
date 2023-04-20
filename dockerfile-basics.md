# Writing Dockerfiles

## Goals

- Understand the anatomy of a Dockerfile
- Select a base image
- Understand the difference between CMD and ENTRYPOINT
- Understand layers and how to optimally order your Dockerfile
- Brief introduction to multi-stage builds

## Anatomy of a Dockerfile

A Dockerfile is a text file that contains a set of instructions for building a Docker image. The instructions are executed in the order they appear in the file, and each instruction creates a new layer in the image. The basic structure of a Dockerfile is as follows:

```dockerfile
# This is a comment
INSTRUCTION arguments
```

Each instruction is a keyword followed by one or more arguments. Here are some commonly used instructions:

### Common Dockerfile Instruction

- `FROM`: Specifies the base image to use for the build.
- `RUN`: Executes a command in the container.
- `COPY` or ADD: Copies files from the local file system to the container.
- `CMD`: Specifies the default command to run when the container is started.
- `ENTRYPOINT`: Specifies the executable that should be run when the container is started.

### Example

```dockerfile
# Base image
FROM some-base-image:tag

# Maintainer information
LABEL maintainer="Your Name <your.email@example.com>"

# Install dependencies
RUN apt-get update && \
    apt-get install -y some-package

# Set environment variables
ENV PATH=/app/bin:$PATH

# Copy application files
COPY app.py /app/
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install -r /app/requirements.txt

# Set the command to run when the container starts
CMD ["python", "/app/app.py"]
```

## Selecting a Base Image

The first line in a Dockerfile must be a `FROM` instruction, which specifies the base image to use for the build. The base image is the starting point for the container and should contain the operating system and any necessary dependencies for your application.

There are many official and community-provided base images available on Docker Hub. When selecting a base image, it is important to choose one that is well-maintained and includes all the dependencies you need for your application.

Here is an example of a `FROM` instruction using the official Python base image:

```dockerfile
FROM python:3.9-slim
```

## `CMD` vs `ENTRYPOINT`

Both `CMD` and `ENTRYPOINT` are used to specify the command that should be run when the container is started. The main difference between them is how they handle arguments.

The `CMD` instruction specifies the default command and any arguments that should be passed to it. The command can be overridden at runtime by passing arguments to docker run.

```dockerfile
CMD ["python"]
```

```shell
docker run my-image 
# >> Runs default CMD which starts a python shell

docker run my-image bash
# >> Args passed to docker run will override the `CMD` instruction, thus starting a bash session
```

The `ENTRYPOINT` instruction specifies the executable that should be run when the container is started. Any arguments passed to docker run will be appended to the end of the ENTRYPOINT command.

```dockerfile
ENTRYPOINT ["python"]
```

```shell
docker run my-image 
# >> Runs default ENTRYPOINT with no args which starts a python shell

docker run my-image bash
# >> Args passed to docker run will be passed to ENTRYPOINT resulting in `python bash` being executed which will fail
```

## Layers and Optimizing Dockerfiles

Each instruction in a Dockerfile creates a new layer in the image. Layers are a fundamental concept in Docker and are used to optimize the build process and minimize the size of the resulting image. Subsequent builds will use the layer cache from previous builds, only executing the command again if the Instruction has changed.

When writing a Dockerfile, it is important to think about the order in which the instructions are executed. Instructions that change frequently should be placed towards the end of the file to avoid invalidating cached layers. Instructions that change less frequently should be placed towards the beginning of the file.

For example, here is an optimized Dockerfile for a Python web application:

```dockerfile
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy source code
COPY . .

# Expose port
EXPOSE 8000

# Start FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Multi-Stage Builds

Multi-stage builds allow you to create smaller images by using multiple stages in your Dockerfile. Each stage can use a different base image and perform a different task. For example, you might use a large base image to compile your application and then copy only the compiled code to a smaller image. To use multi-stage builds:

- Use the `FROM` instruction to specify the base image for each stage.
- Use the `COPY --from` instruction to copy files from a previous stage to the current stage.
- Use the `--target` option with the `docker build` command to build a specific stage.

An example of a multi-stage build will be provided with this repo to demonstrate how it can be useful.

## Some Common Best Practices

- **Keep the image small:** Use the smallest base image possible, and only install the packages and dependencies that are required for your application. This will reduce the image size and improve performance.
- **Use multi-stage builds:** If your application requires multiple dependencies, consider using multi-stage builds to keep the final image small. This allows you to build and compile dependencies in one image, and then copy only the compiled dependencies to the final image.
- **Order your instructions to optimize caching:** Docker images are built in layers, and each layer is cached independently. To take advantage of caching, order your instructions so that the layers that are least likely to change are at the top of the Dockerfile, and the layers that are most likely to change are at the bottom.
- **Minimize the number of layers:** Each instruction in a Dockerfile creates a new layer in the image. To keep the image size small, minimize the number of layers by chaining multiple instructions together using `&&`.
- **Use environment variables for configuration:** Use environment variables to configure your application. This allows you to easily configure your application without modifying the Dockerfile or the image.
- **Clean up after yourself:** Be sure to clean up any temporary files or packages that you installed during the build process. This will help keep the final image small and reduce clutter.

By following these best practices, you can create Docker images that are optimized for performance, security, and maintainability.

## Conclusion

Dockerfiles provide a powerful and flexible way to package your applications into Docker images. By following best practices and optimizing your Dockerfiles, you can create smaller, faster, and more efficient images.
