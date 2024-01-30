=== "macOS"
    # macOS Architecture

    In this section we will dive into the various open source components that Finch
    distributes and how they piece together to form a local development environment
    on macOS.

    ## Finch Architecture

    ![Finch Architecture](/assets/finch_macos_qemu_architecture.png "Finch Architecture")

    | Component  | Description                                                                                                                                                                                                                                                                              | License                                                                  |
    | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
    | Lima       | [Lima (Linux virtual machines)](https://github.com/lima-vm/lima) launches Linux virtual machines with automatic file sharing and port forwarding. In Finch, Lima configures the hypervisor, it passes in the virtual machine image and any pre and post startup scripts.                 | [Apache 2.0](https://github.com/lima-vm/lima/blob/master/LICENSE)        |
    | nerdctl    | [nerdctl (contaiNERD ctl)](https://github.com/containerd/nerdctl) is a command line client for containerd with a similar user experience to the Docker CLI. In Finch, Nerdctl runs inside the virtual machine, starting and stopping containers by communicating directly to containerd. | [Apache 2.0](https://github.com/containerd/nerdctl/blob/main/LICENSE)    |
    | BuildKit   | Moby's [BuildKit](https://github.com/moby/buildkit) is a toolkit for converting source code to build artifacts in an efficient, expressive and repeatable manner. In Finch, BuildKit is used to build Docker and OCI container images inside the virtual machine.                        | [Apache 2.0](https://github.com/moby/buildkit/blob/master/LICENSE)       |
    | containerd | [containerd](https://github.com/containerd/containerd) is an industry-standard container runtime with an emphasis on simplicity, robustness, and portability. In Finch, containerd is the underlying container runtime that manages the containers in the virtual machine                | [Apache 2.0](https://github.com/containerd/containerd/blob/main/LICENSE) |
    | QEMU       | [QEMU](https://www.qemu.org/) is a generic and open source machine emulator and virtualizer. In Finch, QEMU manages the underlying virtual machine on macOS using the Hypervisor.Framework.                                                                                              | [GPL v2](https://gitlab.com/qemu-project/qemu/-/blob/master/LICENSE)     |


=== "Windows"
    # Windows Architecture

    In this section we will dive into the various open source components that Finch
    distributes and how they piece together to form a local development environment
    on Windows.

    ## Finch Architecture

    ![Finch Architecture](/assets/finch_windows_wsl_architecture.png "Finch Architecture")

    | Component  | Description                                                                                                                                                                                                                                                                              | License                                                                  |
    | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
    | Lima       | [Lima (Linux virtual machines)](https://github.com/lima-vm/lima) launches Linux virtual machines with automatic file sharing and port forwarding. In Finch, Lima configures the hypervisor, it passes in the virtual machine image and any pre and post startup scripts.                 | [Apache 2.0](https://github.com/lima-vm/lima/blob/master/LICENSE)        |
    | nerdctl    | [nerdctl (contaiNERD ctl)](https://github.com/containerd/nerdctl) is a command line client for containerd with a similar user experience to the Docker CLI. In Finch, Nerdctl runs inside the virtual machine, starting and stopping containers by communicating directly to containerd. | [Apache 2.0](https://github.com/containerd/nerdctl/blob/main/LICENSE)    |
    | BuildKit   | Moby's [BuildKit](https://github.com/moby/buildkit) is a toolkit for converting source code to build artifacts in an efficient, expressive and repeatable manner. In Finch, BuildKit is used to build Docker and OCI container images inside the virtual machine.                        | [Apache 2.0](https://github.com/moby/buildkit/blob/master/LICENSE)       |
    | containerd | [containerd](https://github.com/containerd/containerd) is an industry-standard container runtime with an emphasis on simplicity, robustness, and portability. In Finch, containerd is the underlying container runtime that manages the containers in the virtual machine                | [Apache 2.0](https://github.com/containerd/containerd/blob/main/LICENSE) |
    | WSL 2       | [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/about#what-is-wsl-2) Windows Subsystem for Linux (WSL) is a feature of Windows that allows you to run a Linux environment on your Windows machine, without the need for a separate virtual machine or dual booting. WSL is designed to provide a seamless and productive experience for developers who want to use both Windows and Linux at the same time. In Finch, WSL is used to manage the underlying virtual machine.                                                                                              | Proprietary     |
