# DevContainers on Finch

## What is DevContainers?

[Dev Containers](https://containers.dev/) are used by developers to build, test, and run applications during the software development process.
Development containers include additional tooling, libraries, and configurations that are helpful for the developer workflow, but not necessary or desirable in a production setting.
The purpose of development containers is to provide a consistent, repeatable environment for developers.

Visual Studio Code (VSCode) can run a workspace within a DevContainer using the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.
Although VSCode settings refer to Docker, Finch can support a majority of use cases as an Open Source Container Runtime Solution.

## Getting Started

For macOS, refer to [DevContainers on Finch within Mac](https://runfinch.com/docs/integrations/mac/devcontainers/)

For Windows, refer to [DevContainers on Finch within Windows](https://runfinch.com/docs/integrations/windows/devcontainers/)


## Known Bugs or Limitations

- **Identifier length limit of 76 characters**: By default, VSCode uses long hash values to name images and container instances. For finch using nerdctl versions earlier than 2.0.0, the default vscode container names are too long and fail validation.
  - **Resolution**: Include a configuration option, like the following example, to declare a unique container name of less than 76 characters. (The following example uses the workspace basename, which is assumed to be less than 76 characters.)

    ```bash
    ## example using the directory as container name
    "runArgs": ["--name", "${localWorkspaceFolderBasename}"],
    ```

- **Advanced Network Creation with Compose**: `finch compose` does not currently support the functionality of `docker compose`. When using `docker compose`, set the `DOCKER_COMPOSE_VERSION` to a value `> 2.9.0`.

- **Docker in Docker via Sockets**: finch does not currently support any application with docker sockets.

- **Cached Optimization**: finch does not currently support cached optimization. Any related settings will be passed through execution.
