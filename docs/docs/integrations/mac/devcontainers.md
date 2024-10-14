# DevContainers for MacOS

## Prerequisites

- Install VSCode and Extension

To install VSCode, refer to instruction at [code.visualstudio.com](https://code.visualstudio.com/) or your organization administrators.

To install the extension, refer to instructions for the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.

- Install Finch

To install Finch, refer to [Managing Finch:macOS Installation](https://runfinch.com/docs/managing-finch/macos/installation/).

- Initiate a Finch Virtual Machine (vm)

    ```bash
    finch vm init
    ```

- Modify your `~/.finch/finch.yaml` to add the following configuration option. Refer to [Configuration Reference](https://runfinch.com/docs/configuration-reference/) for more information.

    ```bash
    dockercompat: true
    ```


## Configure VSCode DevContainer Extension Settings

Open the extension settings by navigating within the setting window or using the command palette and typing "Dev Containers: Settings"

- Configure the "Docker Compose Path" to: `<path>/<to>/finch compose`

- Disable "Docker Credential Helper"

- Configure the "Docker Path" to: `<path>/<to>/finch`


## Create a workspace for a DevContainer

Create a directory that will be the workspace root.

    ```bash
    mkdir ./myLocalDevContainer
    cd ./myLocalDevContainer
    ```
Within the directory, create or clone the pertinent source code for the workspace. For example:

    ```bash
    git clone https://github.com/go-training/helloworld.git
    ```
Create a DevContainer configuration JSON file. For detailed information, refer to [VSCode: Create a DevContainer.json](https://code.visualstudio.com/docs/devcontainers/create-dev-container#_create-a-devcontainerjson-file)

    ```bash
    mkdir -p .devcontainer
    touch .devcontainer/devcontainer.json
    ```

Populate the DevContainer configuration JSON file.

- Example `devcontainer.json` file:

    ```bash
    ## Generic devcontainer.json contents
    {
        "name": "GoAppDevContainer",
        "image": "mcr.microsoft.com/devcontainers/go:1-1.22-bookworm",
        "runArgs": ["--name", "${localWorkspaceFolderBasename}"],
    }
    ```


## Opening VSCode in a DevContainer

- Open the workspace root directory within a new VSCode Window

- Use the VSCode Command Palette and type "Dev Containers: Reopen in Container". Alternatively, VSCode may automatically detect the DevContainer configuration file and may prompt the user with an option to "Reopen in Container".

- Allow for the DevContainer to download necessary dependencies, initiate the specific container, and to SSH attach to the container.

- Use a Terminal session within the container to confirm operation. For example:

    ```bash
    ## Within the go-training/helloworld devcontainer
    go version

    go test .

    go run main.go

    ```





