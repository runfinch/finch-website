# Installing Finch on Linux

## Prerequisites

To get started with Finch on Linux, the development machine must meet the
following prerequisites.

- Linux Kernel v4.x+

To determine the kernel version of your Linux machine, you can run the following command:

```bash
uname -r
```

So long as the first number is greater than 4, Finch is supported. The next sections will cover how to install Finch based on which Linux distribution you are using, along with generic installation options.

## Amazon Linux

Finch is packaged in the standard Amazon Linux repositories. That means, installing Finch is as easy as installing any other Amazon Linux package:

=== "AL2023"

    ```shell
    $ sudo dnf install runfinch-finch
    ```

=== "AL2"

    ```shell
    $ sudo amazon-linux-extras enable docker
    $ sudo yum install runfinch-finch
    ```

After running this command, you will have a `finch` program in your PATH, and you can navigate to the [Verifying Finch install](../../../getting-started/installation/#verify-the-finch-installation) page to proceed. Navigate to the [Optional Components](./optional-components.md) page to configure Finch optional components.

Note that the all of the following Finch guides will use `sudo finch ...`. There is an [optional mechanism to avoid the use of sudo](./../optional-components/#running-finch-without-sudo), follow the link for more information.

## Ubuntu

Finch is packaged in a self hosted APT repository. That means, installing Finch is as easy as this:

=== "AMD64"

    ```shell
    $ curl -fsSL https://artifact.runfinch.com/deb/GPG_KEY.pub | sudo gpg --dearmor -o /usr/share/keyrings/runfinch-finch-archive-keyring.gpg
    $ echo "deb [signed-by=/usr/share/keyrings/runfinch-finch-archive-keyring.gpg arch=amd64] https://artifact.runfinch.com/deb noble main" | sudo tee /etc/apt/sources.list.d/runfinch-finch.list
    $ sudo apt update
    $ sudo apt install runfinch-finch
    ```

=== "ARM64"

    ```shell
    $ curl -fsSL https://artifact.runfinch.com/deb/GPG_KEY.pub | sudo gpg --dearmor -o /usr/share/keyrings/runfinch-finch-archive-keyring.gpg
    $ echo "deb [signed-by=/usr/share/keyrings/runfinch-finch-archive-keyring.gpg arch=arm64] https://artifact.runfinch.com/deb noble main" | sudo tee /etc/apt/sources.list.d/runfinch-finch.list
    $ sudo apt update
    $ sudo apt install runfinch-finch
    ```

After running this command, you will have a `finch` program in your PATH, and you can navigate to the [Verifying Finch install](../../../getting-started/installation/#verify-the-finch-installation) page to proceed.

Note that the all of the following Finch guides will use `sudo finch ...`.

## Generic

For distributions which do not have packages built for them, installing Finch requires downloading and installing dependencies, as well as creating filesystem paths needed by Finch.

Some distributions will distribute some of these packages themselves (for example, Fedora has a `containerd` package), but this guide assumes that none of Finch's dependencies are available via package managers. If the dependencies are available and installed via package managers, some of these steps may be skipped.

The goal of these steps is to setup your system to mimic the configuration found in the [finch.spec file](https://github.com/runfinch/finch/blob/main/contrib/packaging/rpm/finch.spec) in the runfinch/finch repository.

1. Download the Finch Linux binary archive corresponding to your system's architecture from the Releases tab, and extract it using a command like `tar Cxzvvf /usr/local ./bin`
1. Download the Finch Daemon Linux binary archive corresponding to your system's architecture from [their Releases tab](https://github.com/runfinch/finch-daemon/releases), and extract it using a command like `tar Cxzvvf /usr/local/bin <archive_name> ./finch-daemon`
1. Download the latest nerdctl-full archive release corresponding to your system's architecture [from their Releases tab](https://github.com/containerd/nerdctl/releases), and extract it using a command like `tar Cxzvvf /usr/local <archive_name>`
1. Setup filesystem:
   1. Config:
      1. `sudo mkdir -p /etc/finch/nerdctl`
      1. `sudo cp ./contrib/packaging/rpm/nerdctl.toml /etc/finch/nerdctl/`
      1. `sudo mkdir -p /etc/finch/buildkit`
      1. `sudo cp ./contrib/packaging/rpm/buildkitd.toml /etc/finch/buildkit/`
   1. Runtime dependencies
      1. `sudo mkdir -p /usr/libexec/finch`
      1. `sudo mkdir -p /var/lib/finch/buildkit`
      1. `sudo mkdir -p /var/lib/finch/nerdctl`
      1. `ln -sf /usr/local/bin/nerdctl /usr/libexec/finch/nerdctl`
      1. `ln -sf /usr/local/bin/buildctl /usr/libexec/finch/buildctl`
      1. `ln -sf /usr/local/bin/finch-daemon /usr/libexec/finch/finch-daemon`
1. Run system services using a service manager, like systemd, or directly. Example systemd service files can be found in the following locations:
   1. [containerd](https://github.com/containerd/containerd/blob/main/containerd.service)
   1. [buildkit](https://github.com/runfinch/finch/blob/main//contrib/packaging/rpm/finch-buildkit.service)
   1. [finch-daemon](https://github.com/runfinch/finch-daemon/blob/main/finch.service)

After completing this setup, you will have a `finch` program in your PATH, and you can navigate to the [Verifying Finch install](../../../getting-started/installation/#verify-the-finch-installation) page to proceed. Navigate to the [Optional Components](./optional-components.md) page to configure Finch optional components.

Note that the all of the following Finch guides will use `sudo finch ...`. There is an [optional mechanism to avoid the use of sudo](./../optional-components/#running-finch-without-sudo), follow the link for more information.
