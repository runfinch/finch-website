# Installing Finch on Windows

## Prerequisites

To get started with Finch on macOS, the development machine must meet the
following prerequisites.

* Windows versions:
    * Windows 11 (x86-64)
    * Windows 10 Version 1903 or later, with Build 18362.1049 (x86-64)
* Recommended minimum hardware requirements is at least 2 vCPU and 4 GB memory.
* Administrative privileges are required to install Finch on to the machine.
* WSL 2 already installed
* **(Optional)** For the best experience running terminal commands on Windows, it's recommended to install [Microsoft's Windows Terminal](https://learn.microsoft.com/en-us/windows/terminal/)

To determine the build version of your Windows 10 installation, you can either run the following command:
```powershell
[System.Environment]::OSVersion.Version

Major  Minor  Build  Revision
-----  -----  -----  --------
10     0      20348  0
```

...or press Windows + R and run `winver.exe`.

So long as the "Build" number is greater than 18362, WSL 2 and Finch are supported. The next section will cover how to install WSL 2 based on which version of Windows you have installed.

## Installing WSL 2

There are two different methods of installing WSL 2 depending on which version of Windows you have installed. For newer versions (Windows 11 and Windows 10 with build greater than 19041), follow [this guide from Microsoft](https://learn.microsoft.com/en-us/windows/wsl/install). For Windows 10 builds greater than 18362.1049, [follow this guide](https://learn.microsoft.com/en-us/windows/wsl/install-manual) (make sure to follow the WSL 2 steps as well).

## Verifying WSL 2 install

After you're done installing WSL 2, or if you've already had it installed and you've run `wsl --update`, you can verify your installation.

To verify your WSL 2 installation, run the `wsl.exe -l -v` command. The output should look similar to this:

```text
wsl.exe -l -v
  NAME          STATE           VERSION
* Ubuntu        Stopped         2
```

The `wsl.exe --status` command should also have output similar to this:
```text
wsl --status
Default Distribution: Ubuntu
Default Version: 2
```

If the default version is not `2`, run `wsl --set-default-version 2`.

If your any other output is different or these commands do not work, please refer back to the Microsoft guides for troubleshooting steps.

## Installing Finch

After verifying your WSL 2 installation, Finch can be installed like so:

1. Download the latest Finch Windows installer (`Finch.msi`) from [Finch's GitHub repository](https://github.com/runfinch/finch/releases/latest)
1. Run `Finch.msi`

    ![Finch Installation Wizard](/assets/finch_windows_installation_1.png "Finch Installation 1")

1. Read and accept the Finch license and click Next.

    ![Finch Installation License](/assets/finch_windows_installation_2.png "Finch Installation 2")

1. Select your install location if different from the default location, and click Next.

    ![Finch Installation Location](/assets/finch_windows_installation_3.png "Finch Installation 3")

1. Click Install.

    ![Finch Installation Install](/assets/finch_windows_installation_4.png "Finch Installation 4")

1. When the Finch installation is complete, you can close the installation window by pressing Finish.

    ![Finch Installation Complete](/assets/finch_windows_installation_5.png "Finch Installation 5")

1. Finch is now installed! Relaunch any terminal windows in order for the `finch` command to be available in your PATH. Navigate to [Verifying Finch install](../../../getting-started/installation/#verify-the-finch-installation) to proceed.
