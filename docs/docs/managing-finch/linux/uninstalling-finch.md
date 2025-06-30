# Uninstalling Finch

The best way to uninstall Finch on Linux depends on your system.

## Uninstalling Finch on Amazon Linux

Amazon Linux packages can be uninstalled via using the system package manager:

=== "AL2023"
    
    ```shell
    $ sudo dnf remove runfinch-finch
    ```

=== "AL2"
    
    ```shell
    $ sudo yum remove runfinch-finch
    ```

## Uninstalling Finch on Ubuntu

Ubuntu packages can be uninstalled via using the system package manager:

    ```shell
    $ sudo apt remove runfinch-finch
    ```

## Manual uninstallation

If you followed the manual installation steps, Finch and its dependencies can be fully uninstalled by running the following commands:

```bash
sudo rm -rf /etc/finch/ && \
sudo rm -rf /usr/libexec/finch/ && \
sudo rm -rf /var/lib/finch/
```

### Dependencies

Depending on the `nerdctl-full` archive that was extracted, there will be different files that need to be removed. You can query the files in the nerdct-full archive that you used and remove any matching files by running the following command:

```bash
tar -tf <path/to/nerdctl-full-archive>
```

To do this all at once:

```bash
cd /usr/local
for f in $(tar -tf <path/to/nerdctl-full-archive>); do
sudo rm -rf $f
done
```
