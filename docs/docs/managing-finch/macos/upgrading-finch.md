# Upgrading Finch

Finch releases updates on a regular cadence, to find the latest release and the
subsequent release notes, see the [Release Notes](../../changelog.md).

Finch packages upgrades of all components of the stack, including the latest
operating system image. As part of a Finch upgrade, all container data
(container images and container volumes) are persisted between upgrades.

## Upgrading Finch with [homebrew](https://brew.sh/)

If you have installed Finch with the [homebrew](https://brew.sh/) package manager,
you can upgrade Finch using `brew`.

1. Retrieve the latest package versions with `brew update`.

    ```bash
    brew update
    ```

2. You can validate that a new Finch version is available with `brew
   outdated`.

    ```bash
    brew outdated finch
    ```

    If a response is returned, there is an updated available for Finch.

    ```bash
    finch (0.6.1) != 0.6.2
    ```

3. Upgrade the package with `brew upgrade`.

    ```bash
    brew upgrade finch
    ```

4. Once the command has finished, you can check the status of the Finch virtual
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

## Upgrading Finch using the Application Package

For each Finch release, we provider a `.pkg` Application Package. The latest
package can be found on the [Github
Releases](https://github.com/runfinch/finch/releases), with a separate package
available for each architecture (Apple Silicon and Intel).

1. Download the relevant Application Package from the Finch [Github
Releases](https://github.com/runfinch/finch/releases) page. Ensuring you have
   selected the appropriate version and architecture

2. Once the Application Package has been download, in
   [Finder](https://support.apple.com/en-us/HT201732), you can double click the
   `.pkg` and start the upgrade. A popup on the installer, should display a
   warning that an existing version of Finch has been found and that it will be
   removed prior to upgrade. Click Ok on the pop up, and continue on the wizard.

    ![Finch Upgrade Wizard](/assets/finch_macos_upgrade_1.png "Finch Upgrade 1")

3. Click through the various pages in the wizard. This
   wizard is the same as wizard previously seen during the
   [Installation](/docs/getting-started/installing/#zys).

4. Once the command has finished, you can check the status of the Finch virtual
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