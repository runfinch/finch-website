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

To determine the build version of your Windows 10 installation, you can either run the following comamnd:
```powershell
> [System.Environment]::OSVersion.Version

Major  Minor  Build  Revision
-----  -----  -----  --------
10     0      20348  0
```

...or press Windows + R and run `winver.exe`.

So long as the "Build" number is greater than 18362, WSL 2 and Finch are supported. The next section will cover how to install WSL 2 based on which version of Windows you have installed.

## Installing WSL 2

=== "Windows 11 (and 10, 2004 and higher)"

    1. Run `wsl --install` and follow prompts to set your Linux user name. That's it!
    1. WSL 2 is now installed! See the "Installing Finch" section to get Finch up and running

    For more information and troubleshooting steps [see Microsoft's documentation here](https://learn.microsoft.com/en-us/windows/wsl/install)

=== "Windows 10 (old)"

    1. Run `dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart` to install the Windows Subsystem for Linux
    1. Run `dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart` and then **Restart** your machine
    1. After restarting, download the [latest version of the WSL 2 kernel from Microsoft](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi) and run the installer
    1. Make sure WSL 2 is set as your default version by running `wsl --set-default-version 2`
    1. Install a "default" distribution of WSL 2 by running `wsl --install -d Ubuntu`
    1. WSL 2 is now installed! See the "Installing Finch" section to get Finch up and running
    
    For more information and troubleshooting steps [see Microsoft's documentation here](https://learn.microsoft.com/en-us/windows/wsl/install-manual)

## Installing Finch

After installing WSL 2, or updating WSL 2 using (`wsl --update`), Finch can be installed like so:

1. Download the latest Finch Windows installer (`Finch.msi`) from [Finch's GitHub repository](https://github.com/runfinch/finch/releases/latest)
1. Run `Finch.msi`
1. Finch is now installed! Navigate to [Verifying Finch install](../../../getting-started/installation/#verify-the-finch-installation) to proceed
