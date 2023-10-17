# Installing Finch on macOS

!!! Note
    This page is specific to Finch running on macOS. At this time macOS is the
    only supported operating system.

## Prerequisites

To get started with Finch on macOS, the development machine must meet the
following prerequisites.

* macOS versions:
    * 13 Ventura
    * 12 Monterey
    * 11 Big Sur (known to work, but not tested)
* Both Intel and Apple Silicon based systems running the last 2 major versions of macOS are supported.
* Recommended minimum hardware requirements is at least 2 vCPU and 4 GB memory.
* Administrative privileges are required to install Finch on to the machine.

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

3. You can now [verify the installation](#verify-the-finch-installation).

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
   prompt. You can now [verify the
   installation](#verify-the-finch-installation).

    ![Finch Installation Complete](/assets/finch_macos_installation_4.png "Finch Installation 4")

## Verify the Finch Installation

Now that Finch has been successfully installed, you can verify the installation
with the following steps.

1. Once the installation is complete, running the `finch vm init` command once is required
   to set up the underlying system and create the virtual machine. This initial setup
   usually takes about a minute, and may once again require your macOS password.

    ```bash
    finch vm init
    ```

2. Verify that the installation and the vm initialization have completed by
   running the `hello-finch` container image.

    ```bash
    finch run public.ecr.aws/finch/hello-finch:latest
    ```

    If it has all ran successfully you should now see the output:

    ```bash

                                @@@@@@@@@@@@@@@@@@@
                            @@@@@@@@@@@@    @@@@@@@@@@@
                          @@@@@@@                  @@@@@@@
                        @@@@@@                        @@@@@@
                      @@@@@@                            @@@@@
                     @@@@@                      @@@#     @@@@@@@@@
                    @@@@@                     @@   @@@       @@@@@@@@@@
                    @@@@%                     @     @@            @@@@@@@@@@@
                    @@@@                                               @@@@@@@@
                    @@@@                                         @@@@@@@@@@@&
                    @@@@@                                  &@@@@@@@@@@@
                     @@@@@                               @@@@@@@@
                      @@@@@                            @@@@@(
                       @@@@@@                        @@@@@@
                         @@@@@@@                  @@@@@@@
                            @@@@@@@@@@@@@@@@@@@@@@@@@@
                                @@@@@@@@@@@@@@@@@@


    Hello from Finch!

    Visit us @ github.com/runfinch
    ```

## Next Steps

In this short guide you learned how to install Finch on to your macOS workstation and
start the virtual machine.

* To learn how to run your first containerized application see [Running
  Containers](../running_containers/).
* To learn more about the Finch virtual machine see the [Managing the Finch
  VM](../../managing-finch/managing_vm/) documentation.
