# WSL Configuration

Windows Subsystem for Linux can be optimized and tuned using a configuration file located at C:\Users\<username>\.wslconfig. In the sections below we discuss some configuration that can be tuned to optimize Finch. For a full list of .wslconfig configuration options see the [Microsoft documentation here](https://learn.microsoft.com/en-us/windows/wsl/wsl-config).

!!! warning
    The configuration changes which modify your `.wslconfig` file will apply to **ALL** WSL 2 distributions.

### Limiting CPU and memory usage

For users who want to replicate Finch's `finch.yaml` `memory` and `cpu` can instead use similar options in their `.wslconfig` file, like so:

```
[wsl2]

# Limits VM memory to use no more than 4 GB.
# This can be set as whole numbers using GB or MB
memory=4GB 

# Sets the VM to use two virtual processors
processors=2
```

### Reclaiming memory automatically

In addition to setting max memory limits, user's can also specify to clean up WSL cached memory automatically. With this setting unset, cached memory remains allocated by the WSL 2 VM until shutdown.

```
[experimental]
# Automatically releases cached memory after detecting idle CPU usage.
# Set to gradual for slow release, and dropcache for instant
# release of cached memory.
autoMemoryReclaim=dropcache
```
