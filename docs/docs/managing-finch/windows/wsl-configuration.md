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
**WARNING:** By default, Finch uses the standard WSL configuration, which mounts the host's C drive into Finch VM with read-write access.
If you prefer to restrict access to the VM (and the containers running inside) by setting the C drive to read-only, follow the steps below.

**Step 1: Disable C Drive Auto-Mount in WSL Configuration**

Log in to the Finch VM and disable the C drive auto-mount in the WSL configuration:

```
PS C:\Users\Administrator> wsl -d lima-finch
[root@EC2AMAZ-R56AQRB Desktop] cat /etc/wsl.conf
[boot]
systemd=true

# Disable auto-mount
[automount]
enabled=false 
```
**Step 2: Modify fstab for mounting C Drive in read-only**

Edit the fstab file to add entries for mounting the C drive in read-only mode. 
Some Finch commands require read-write access to `C:/Users/Administrator`, so we'll need to mount that directory in RW mode. 

```
[root@EC2AMAZ-R56AQRB Administrator] vi /etc/fstab
C:/ /mnt/c drvfs ro 0 0
C:/Users/Administrator /mnt/c/Users/Administrator drvfs rw 0 0
C:/source-dir-path /mnt/mount-dir-path drvfs perms 0 0 # Can add more dirs which requires RW access if needed
```

**Step 3: Exit the VM and Restart Finch**

To apply your changes, exit the VM and restart Finch:

```
PS C:\> wsl --shutdown 
PS C:\> finch vm status
Stopped
PS C:\> finch vm start
```

Finch on Windows does not make any claims or guarantees regarding VM-level isolation, so consider the instance as the security boundary. 
The steps outlined above will help ensure that the containers operate in a more secure environment, enhancing overall security posture. 
If you do not have such security considerations, you can continue using the default settings.
