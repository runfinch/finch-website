# Upgrading Finch

Finch releases updates on a regular cadence. To find the latest release and
information on what was included see the [release
notes](../../changelog.md).

A Finch release includes new versions of all components of the stack, including
the latest operating system patches. As part of a Finch upgrade, all container
related data (container images and container volumes) are persisted between
upgrades.

On Windows, currently the best way to upgrade is to download and run the latest Finch.msi release from [Finch's GitHub repository](https://github.com/runfinch/finch/releases/latest). For detailed instructions, follow the steps on [the Windows installation page](./installation.md#installing-finch).

After installing the latest version, make sure that the new version is running by:

1. Run `finch vm init`

2. Once the command has finished, you can check the status of the Finch virtual
   machine with `finch version`.

    ```bash
    finch version
    ```

    The output shows the version of Finch installed. If the virtual machine is
    running, it will also show the versions of the various container components.

    ```bash
    finch version
    Client:
     Version:       v0.6.2
     OS/Arch:       linux/arm64
     GitCommit:     741d578d9ab456a5f58f050d2324417501868e02
     nerdctl:
      Version:      v1.4.0
      GitCommit:    7e8114a82da342cdbec9a518c5c6a1cce58105e9
     buildctl:
      Version:      v0.11.6
      GitCommit:    2951a28cd7085eb18979b1f710678623d94ed578

    Server:
     containerd:
      Version:      v1.7.1
      GitCommit:    1677a17964311325ed1c31e2c0a3589ce6d5c30d
     runc:
      Version:      1.1.7
      GitCommit:    v1.1.7-0-g860f061b
    ```
