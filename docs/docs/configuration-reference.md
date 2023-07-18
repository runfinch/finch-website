# Finch Configuration

Finch has a configuration file stored at `~/.finch/finch.yaml`. This
configuration file extracts away the virtual machine, Lima and Hypervisor
configuration.

Each time the `~/.finch/finch.yaml` configuration is updated, the virtual
machine will need to be restarted for the change to take effect.

```
finch vm stop
finch vm start
```

Example `finch.yaml` file:

```
cpus: 3
memory: 4GiB
additional_directories:
  - "/Volumes/mydir"
vmType: vz
rosetta: true
```

## Parameters:

- `cpus`: The number of logical CPUs to attach to the virtual machine. The default is
  determined dynamically based on the resources available using `0.25 * total_cpu_cores`,
  with a minimum value of `2`


- `memory`: The amount of memory to attach to the virtual machine. The default is
  determined dynamically based on the resources available using `0.25 * total_memory`,
  with a minimum value of `2GiB`

- `additional_directories`: By default Finch will mount the users home directory
  into the virtual machine. To mount additional directories from macOS into the
  virtual machine, specify them here. See [Disk Management for more
  details](/docs/managing-finch/disk-management/). Default is `[]`

- `vmType`: The hypervisor to use for the virtual machine.
  [QEMU](https://www.qemu.org/) (`qemu`) or Apple [Virtualization
  Framework](https://developer.apple.com/documentation/virtualization) (`vz`). Apple
  Virtualization Framework can only be used on macOS 13 or later. Default is
  `qemu`

- `rosetta`: The emulation layer to use when running container images or
  processes on an architecture not native to the machine. If value is set to
  `false`, the emulation is provided by QEMU. If value is set to `true`,
  [Apple's
  Rosetta](https://developer.apple.com/documentation/apple-silicon/about-the-rosetta-translation-environment)
  framework is used. Rosetta can only be used if `vmType: vz`. When `vmType: vz` is set,
  without specifying `rosetta`, `rosetta` will default to `true`. Otherwise, the default is `false`
