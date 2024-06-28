# Finch Configuration

Finch has a configuration file stored at `~/.finch/finch.yaml` on macOS or `%LocalAppData%\.finch\finch.yaml` on Windows. This
configuration file abstracts away the virtual machine, Lima and Hypervisor
configuration.

Each time the `finch.yaml` configuration is updated, the virtual
machine will need to be restarted for the change to take effect.

```
finch vm stop
finch vm start
```

Example `finch.yaml` file:

```
cpus: 3
memory: 4GiB
snapshotters:
  - "overlayfs"
creds_helpers:
  - "ecr-login"
additional_directories:
  - "/Volumes/mydir"
vmType: vz
rosetta: true
```

## Parameters

Many of Finch's configuration options are currently macOS only, and this will be indicated below. On Windows, WSL has [its own set of configuration options options available here](./managing-finch/windows/wsl-configuration.md).

- `cpus` **(macOS only)**: The number of logical CPUs to attach to the virtual machine. The
  default is determined dynamically based on the resources available using
  `0.25 * total_cpu_cores`, with a minimum value of `2`.

- `memory` **(macOS only)**: The amount of memory to attach to the virtual machine. The default
  is determined dynamically based on the resources available using
   `0.25 * total_memory`, with a minimum value of `2GiB`.

- `snapshotters`: The list of [containerd
  snapshotters](https://github.com/containerd/containerd/tree/main/docs/snapshotters)
  that will be installed and configured on to the virtual machine. For more
  information on lazy loading snapshotters see [Lazy
  Loading](/docs/container-images/lazy-loading/). Supported values: `soci`,
  `overlayfs`. When this field is omitted Finch will use the `overlayfs`
  snapshotter. By default this field is omitted.

- `creds_helpers`: The list of credential helpers that will be installed and
  configured automatically on `finch vm init` or `finch vm start`. For more
  information see [Registry
  Authentication](/docs/container-images/authentication/). Supported values:
  `ecr-login`. By default this field is omitted.

- `additional_directories` **(macOS only)**: By default Finch will mount the users home directory
  into the virtual machine. To mount additional directories from macOS into the
  virtual machine, specify them here. See [disk
  management](/docs/managing-finch/macos/disk-management/) for more details.
  Default is `[]`

- `vmType`: The hypervisor to use for the virtual machine.
    - macOS
        - [QEMU](https://www.qemu.org/) (`qemu`) or Apple [Virtualization
          Framework](https://developer.apple.com/documentation/virtualization) (`vz`).
          Apple Virtualization Framework can only be used on macOS 13 or later. Default
          is `vz`
    - Windows
        - The only supported vmType for Windows is `wsl2`

- `rosetta` **(macOS only)**: The emulation layer to use when running container images or
  processes on an architecture not native to the machine. If value is set to
  `false`, the emulation is provided by QEMU. If value is set to `true`,
  [Apple's
  Rosetta](https://developer.apple.com/documentation/apple-silicon/about-the-rosetta-translation-environment)
  framework is used. Rosetta can only be used if `vmType: vz`. When `vmType: vz`
  is set, without specifying `rosetta`, `rosetta` will default to `true`.
  Otherwise, the default is `false`
