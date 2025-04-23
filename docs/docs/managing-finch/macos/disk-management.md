# Managing Finch Storage

## Disk Mounts

To allow containers and container image builds to access files from the local
workstation within the virtual machine, a users home directory (on macOS this is
`/Users/<username>`) is automatically
mounted into the machine by Lima.

To demonstrate this, in an empty directory on the workstation you can create a
`hello` file, and then mount it into the container with the `--volume` command.

```bash
touch hello

finch run \
   --volume $PWD:/data \
   public.ecr.aws/amazonlinux/amazonlinux:2 \
   ls /data
```

You should see the file you just created.

```bash
hello
```

### Adding additional disk mounts

For users wanting to mount additional directories in the virtual machine, they
can specify additional mounts in the Finch Configuration.

1. Open the Finch configuration in a text editor `~/.finch/finch.yaml` and add
   the relevant paths for the local directory on your workstation.

    ```
    cpus: 3
    memory: 4GiB
    additional_directories:
      - "/Volumes/test"
    ```
    !!! note 
    
        If your username doesn't match your home directory name, you may need to add `/Users/<username>` to the additional_directories list. This can help avoid permission issues when building Docker images or accessing files within containers.
        ```
        additional_directories:
            - "/Users/<username>"
        ```
2. Restart the virtual machine to pick up the changes in the mounts.

    ```
    finch vm stop
    finch vm start
    ```

3. Once the virtual machine has been restarted you can test this mount. First
   create a temporary directory and file in this new disk location.

    ```bash
    mkdir /Volume/test/testdir
    touch /Volume/test/testdir/hello
    ```

    Then mount the volume into a new container.

    ```bash
    finch run \
       --volume /Volume/test/testdir:/data \
       public.ecr.aws/amazonlinux/amazonlinux:2 \
       ls /data
    ```

    You should see the file you just created.

    ```bash
    hello
    ```


### Disk Mount Technology

By default the disk is mounted into the virtual machine using
[sshfs](https://github.com/libfuse/sshfs). For users running macOS 13 or later,
if you switch to Apple's [Virtualization
Framework](https://developer.apple.com/documentation/virtualization) in the
[Finch Configuration](/docs/configuration-reference/), the disk mounts will
instead leverage the more performant
[virtiofs](https://developer.apple.com/documentation/virtualization/shared_directories).

1. Open the Finch configuration in a text editor `~/.finch/finch.yaml` and add
   the key `vmType` with the value `vz`.

    ```
    cpus: 3
    memory: 4GiB
    vmType: vz
    ```

2. Restart the virtual machine to pick up the changes in the virtualization technology.

    ```
    finch vm stop
    finch vm start
    ```

## Disk Size

By default the Finch virtual machine will have a disk capacity of 50GB, even
though you may have more disk space available on the local workstation. As you
start to build container images and run containers, this disk space may reach
capacity.

To free up disk space you can delete stale container image layers with:

```bash
finch image prune
```

You can also free up disk by delete all container images without a container
attached with:

```bash
finch image prune --all
```

### Increasing the size of the Data Disk

To expand the virtual machine disk size above 50GB, you can use the Finch VM disk resize command.

1. First make sure the virtual machine has been stopped

    ```bash
    finch vm stop
    ```

2. Resize the virtual machine disk using the finch vm disk resize command.
   Note that disk size can only be increased, not decreased.

    ```bash
    finch vm disk resize --size <size>
    ```

    For example, to increase to 100GiB:

    ```bash
    finch vm disk resize --size 100GiB
    ```

3. Next start back up the virtual machine

    ```bash
    finch vm start
    ```

4. To validate the change has been successful, shell into the
   virtual machine, checks the disk size with `df -h`.

    ```bash
    export LIMA_HOME=/Applications/Finch/lima/data

    /Applications/Finch/lima/bin/limactl shell finch df -H
    ```
