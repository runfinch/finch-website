# DevContainers on Finch

## What is DevContainers?

A [development container](https://containers.dev/) (DevContainer) enables repeatable, consistent development environments for individual developers or teams.
Dev Containers are used by developers to build, test, and run applications during the software development process.
Unlike production deployment containers, which are optimized for efficiently running the final application, development containers include additional tooling, libraries, and configurations that are helpful for the developer workflow, but not necessary or desirable in a production setting.
The purpose of development containers is to provide a consistent, repeatable environment for developers, whereas deployment containers are focused on minimizing the runtime footprint and dependencies required to execute the application in production.

Visual Studio Code (VSCode) can run a workspace within a DevContainer using the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.
Although VSCode settings refer to Docker, Finch can support a majority of use cases as an Open Source Container Runtime Solution.

## Why use DevContainers?

1. Consistency: The biggest benefit of using dev containers is that you will be able to consistently reproduce your development environment. You can be confident that your code will run the same way on any computer, regardless of the underlying operating system or installed software.
2. Collaboration: Dev containers make it easy for teams to collaborate on projects. Instead of each team member needing to set up their own development environment, everyone can use the same dev container. This ensures that everyone is working in the same environment, which can help to prevent conflicts and ensure that everyone is on the same page.
3. Portability: Because dev containers are self-contained, developers can easily move a container from one computer to another. This makes it easy to work on your project on multiple computers or to share your development environment with others.
4. Isolation: Dev containers provide isolation, which means they won’t interfere with any other software or processes running on your computer. This can help to prevent conflicts, compatibility issues, or even damage, and it ensures that your development environment is clean and stable.


## Getting Started

For macOS, refer to [DevContainers on Finch within Mac](https://runfinch.com/docs/integrations/mac/devcontainers/)

For windows, refer to [DevContainers on Finch within Windows](https://runfinch.com/docs/integrations/windows/devcontainers/)


## Known Bugs or Limitations

- **Identifier length limit of 76 characters**: By default, VSCode uses long hash values to name images and container instances. For finch using nerdctl versions earlier than 2.0.0, the default vscode container names are too long and fail validation.
  - **Resolution**: Include the following configuration option to declare a unique container name of less than 76 characters.

    ```bash
    ## example using the directory as container name
    "runArgs": ["--name", "${localWorkspaceFolderBasename}"],
    ```

- **Container is Created, but not Started**: If the VSCode process is interrupted, it may leave zombie containers that are status `CREATED` instead of `RUNNING`. These containers may cause the VSCode DevContainer Logs to encounter errors related to unable to read information from the container.
  - **Resolution**: Utilize the `finch` cli command to list and remove/prune zombie containers.

    ```bash
    ## list the containers with Id's and Status
    finch container ls -a

    ## remove the specific container
    finch container rm <id>

    ## remove all containers
    finch container prune
    ```

- **Issues with Downloading Dependencies**: If your build environment experiences issues with downloading dependencies from the Go proxy servers, then you may want to bypass the proxy servers.
  - **Resolution**: Include the following configuration option to download dependencies "direct" from go servers.

    ```bash
    "containerEnv": {
        "GOPROXY": "direct"
    },
    ```


  to set the environment variable `export GOPROXY=direct`

- **Advanced Network Creation with Compose**: `finch compose` does not currently support all of the functionality of `docker compose`

- **Docker in Docker via Sockets**: finch does not currently support Docker sockets.
