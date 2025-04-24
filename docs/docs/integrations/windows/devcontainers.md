# DevContainers for Windows

## Prerequisites

- Install VSCode and Extension

To install VSCode, refer to instruction at [code.visualstudio.com](https://code.visualstudio.com/) or your organization administrators.

To install the extension, refer to instructions for the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.

- Install Finch

To install Finch, refer to [Managing Finch:windows Installation](https://runfinch.com/docs/managing-finch/windows/installation/).

- Initiate a Finch Virtual Machine (vm)

    ```bash
    finch vm init
    ```

- Modify your `%LocalAppData%\.finch\finch.yaml` to add the following configuration option. Refer to [Configuration Reference](https://runfinch.com/docs/configuration-reference/) for more information.

    ```bash
    dockercompat: true
    ```


## Configure VSCode DevContainer Extension Settings

Open the extension settings by navigating within the setting window or using the command palette and typing "Dev Containers: Settings"

- Configure the "Docker Compose Path" to: `C:<path>/<to>/finch.exe compose`

- Disable "Docker Credential Helper"

- Configure the "Docker Path" to: `C:<path>/<to>/finch.exe`

- Configure the "Execute in WSLDistro" to: `C:<path>/<to>/finch.exe`

- Disable the "Mount Wayland Socker" option


## Working with Docker Compose Projects in Dev Containers:
When using `docker compose`, set the `DOCKER_COMPOSE_VERSION` to a value `> 2.9.0`.

- Using the Command Prompt: use `set DOCKER_COMPOSE_VERSION=x.x.x` for the current session

- Using the PowerShell: use `$env:DOCKER_COMPOSE_VERSION = "x.x.x"` for the current session

- Set the environment variable within the System Properties::Advanced System Settings::Environment Variables

> ⚠️ **Note:** Finch only supports dash (`-`) as the project name separator. 
> However, Dev Container tooling relies on the separator determined by `docker compose version`. 
> If the version is below `2.9.0`, it defaults to using underscores (`_`), causing name mismatches 
> and container startup failures. To ensure compatibility, set the `DOCKER_COMPOSE_VERSION` to `>= 2.9.0`.