# Installing Finch on macOS

## Prerequisites

To get started with Finch on macOS, the development machine must meet the
following prerequisites.

* macOS versions:
    * 14 Sonoma
    * 13 Ventura
* Both Intel and Apple Silicon based systems running the last 2 major versions of macOS are supported.
* Recommended minimum hardware requirements is at least 2 vCPU and 4 GB memory.
* Administrative privileges are required to install Finch on to the machine.

> Finch **may** work on previous macOS releases, however at this time it is only
> tested on the versions listed above.

## Installing Finch with [homebrew](https://brew.sh/)

To install Finch with a package manager you can leverage the
[homebrew](https://brew.sh/) package manager.

1. Verify that homebrew is already installed on the system by running the brew
   help command `brew help` in your favorite terminal application. If it is not,
   navigate to the homebrew documentation for [installation
   instructions](https://docs.brew.sh/Installation).

    ```bash
    brew help
    ```

2. Install Finch using the `brew` CLI. If prompted, enter your macOS password.

    ```bash
    brew install finch
    ```

3. You can now verify the installation.

    ```bash
    # Check the installed Finch version
    finch --version

    # Check the status of the Finch virtual machine
    finch vm status
    ```

## Installing using the Application Package

For each Finch release, we provider a `.pkg` Application Package. The latest
package can be found on the [Github
Releases](https://github.com/runfinch/finch/releases), with a separate package
available for each architecture (Apple Silicon and Intel).

1. Download the relevant Application Package from the Finch [Github
Releases](https://github.com/runfinch/finch/releases) page. Ensuring you have
   selected the appropriate version and architecture.

2. Once the Application Package has been downloaded, in
   [Finder](https://support.apple.com/en-us/HT201732), you can double click the
   `.pkg` and start the installation. Click continue.

    ![Finch Installation Wizard](/assets/finch_macos_installation_1.png "Finch Installation 1")

3. Read and accept the Finch license and click continue.

    ![Finch Installation License](/assets/finch_macos_installation_2.png "Finch Installation 2")

4. Click Install. This will prompt you for your macOS password.

    ![Finch Installation Screen](/assets/finch_macos_installation_3.png "Finch Installation 3")

5. When the Finch installation is complete, you can close the installation
   prompt.

    ![Finch Installation Complete](/assets/finch_macos_installation_4.png "Finch Installation 4")


6. You can now verify the installation.

    ```bash
    # Check the installed Finch version
    finch --version

    # Check the status of the Finch virtual machine
    finch vm status
    ```