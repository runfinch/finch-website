# Upgrading Finch

Finch releases updates on a regular cadence. To find the latest release and
information on what was included see the [release
notes](../../changelog.md).

On Linux, the way you upgrade depends on your distribution.

## Amazon Linux

Amazon Linux pacakges can be upgraded via using the system package manager:

=== "AL2023"
    
    ```shell
    $ sudo dnf update soci-snapshotter
    ```

=== "AL2"
    
    ```shell
    $ sudo yum update soci-snapshotter
    ```

## Manual installation

Components in a manual installation of Finch can be upgraded individually. Follow the installation instructions for detailed instructions on how to install various components. For a manual installation, upgrading is essentially re-extracting newer versions of software as if it were a new installation.
