# Installing Finch on Windows

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

Finch is packaged in the standard Amazon Linux repostiroies. That means, installing Finch is as easy as installing any other Amazon Linux package:

```
$ sudo yum install runfinch-finch
```

After running this command, you will have a `finch` program in your PATH, and you can navigate to the [Verifying Finch install](../../../getting-started/installation/#verify-the-finch-installation) page to proceed.

## Generic

For distributions which do not have packages built for them, installing Finch requires downloading and installing dependencies, as well as creating filesystem paths needed by Finch.

Some distributions will distribute some of these packages themselves (for example, Fedora has a `containerd` pacakge), but this guide assumes that none of Finch's dependencies are available via package managers. If the dependencies are available and installed via package managers, some of these steps may be skipped.

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
      1. `sudo mkdir -p /var/lib/finch/soci`
      1. `ln -sf /usr/local/bin/nerdctl /usr/libexec/finch/nerdctl`
      1. `ln -sf /usr/local/bin/buildctl /usr/libexec/finch/buildctl`
      1. `ln -sf /usr/local/bin/finch-daemon /usr/libexec/finch/finch-daemon`
1. Run system services using a service manager, like systemd, or directly. Example systemd service files can be found in the following locations:
   1. [containerd](https://github.com/containerd/containerd/blob/main/containerd.service)
   1. [buildkit](https://github.com/runfinch/finch/blob/main//contrib/packaging/rpm/finch-buildkit.service)
   1. [finch-daemon](https://github.com/runfinch/finch-daemon/blob/main/finch.service)
