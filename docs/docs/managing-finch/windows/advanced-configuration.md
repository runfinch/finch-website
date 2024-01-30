# Windows Advanced Configuration

## Intro

After looking at the [Configuration Reference page](../../configuration-reference.md), you may notice that Finch on Windows lacks many of the settings that are availalbe on other versions (like, memory and cpu limits).

However, this isn't the full picture. Many of the same functionalities are instead controlled by WSL's own configuration options.

More information on all of these settings can be found [here](https://learn.microsoft.com/en-us/windows/wsl/wsl-config).

!!! warning
    The configuration changes which modify your `.wslconfig` file will apply to **ALL** WSL 2 distributions.

### Limiting CPU and memory usage

Users which want to replicate Finch's `finch.yaml` `memory` and `cpu` can instead use similar options in their `.wslconfig` file, like so:

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
