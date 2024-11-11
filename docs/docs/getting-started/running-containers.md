# Running Containers

The Finch CLI aims to support the same top level commands used in other
container runtimes, therefore if you have ever used `docker run` before you will
quickly become familiar with`finch run`.

Finch leverages [containerd](https://github.com/containerd/containerd) and
[nerdctl](https://github.com/containerd/nerdctl) to run containers on the
[lima](https://github.com/lima-vm/lima) virtual machine.

## Running your first container

`finch run` is a command that lets you run a container image that either exists
in a remote repository or that already exists in the local image store.

To start the
[hello-finch](https://github.com/runfinch/finch/tree/main/contrib/hello-finch),
sample application that has been built and stored in a remote registry, we can
use `finch run` following by the container image. If you need to authenticate to
a container registry see [pushing
images](../pushing-images/#authenticating-to-a-container-registry) documentation
for instructions.

=== "macOS / bash"
    ```bash
    finch run \
        public.ecr.aws/finch/hello-finch:latest
    ```
=== "Windows / PowerShell"
    ```powershell
    finch run `
        public.ecr.aws/finch/hello-finch:latest
    ```
=== "Linux"
    ```shell
    sudo finch run \
        public.ecr.aws/finch/hello-finch:latest
    ```


You should now see the ASCII art in your terminal.

```bash

                            @@@@@@@@@@@@@@@@@@@
                        @@@@@@@@@@@@    @@@@@@@@@@@
                      @@@@@@@                  @@@@@@@
                    @@@@@@                        @@@@@@
                  @@@@@@                            @@@@@
                 @@@@@                      @@@#     @@@@@@@@@
                @@@@@                     @@   @@@       @@@@@@@@@@
                @@@@%                     @     @@            @@@@@@@@@@@
                @@@@                                               @@@@@@@@
                @@@@                                         @@@@@@@@@@@&
                @@@@@                                  &@@@@@@@@@@@
                 @@@@@                               @@@@@@@@
                  @@@@@                            @@@@@(
                   @@@@@@                        @@@@@@
                     @@@@@@@                  @@@@@@@
                        @@@@@@@@@@@@@@@@@@@@@@@@@@
                            @@@@@@@@@@@@@@@@@@


Hello from Finch!

Visit us @ github.com/runfinch
```

## Running a container that exposes a port

When running containers on Finch, you can expose a container so that it is
reachable from your workstation. To do this, pass the port the application is
running on, and the desired external port to the `--publish` flag for `finch
run`. Note the external port has to be unique, multiple containers can not be
exposed on to the same port.

=== "macOS / bash"
    ```bash
    finch run \
        --publish 80:80 \
        public.ecr.aws/nginx/nginx
    ```
=== "Windows / PowerShell"
    ```powershell
    finch run `
        --publish 80:80 `
        public.ecr.aws/nginx/nginx
    ```
=== "Linux"
    ```shell
    sudo finch run \
        --publish 80:80 \
        public.ecr.aws/nginx/nginx
    ```

Now in a web browser, you should be able to
navigate to `localhost` and access the running web server container.

![Finch Nginx](/assets/finch_running_nginx.png "Finch Nginx")

## Common Run Flags

Popular `finch run` flags which will help you get started include:

* Automatically clean up a container after it has exited with `--rm`.

    === "macOS / bash"
        ```bash
        finch run \
            --rm \
            public.ecr.aws/finch/hello-finch:latest
        ```
    === "Windows / PowerShell"
        ```powershell
        finch run `
            --rm `
            public.ecr.aws/finch/hello-finch:latest
        ```
    === "Linux"
        ```bash
        sudo finch run \
            --rm \
            public.ecr.aws/finch/hello-finch:latest
        ```

      * Verify that all containers have been removed

        === "macOS/Windows"
            ```shell
            $ finch ps --all
            ```
        === "Windows / PowerShell"
            ```powershell
            finch ps --all
            ```
        === "Linux"
            ```shell
            $ sudo finch ps --all
            ```

* Start an interactive session into a container with the tty `--tty` and the
  interactive `--interactive` flags. Assuming your container image has a shell
  prompt, you will then be placed into the container where you can run commands.

    === "macOS / bash"
        ```bash
        finch run \
            --interactive \
            --tty \
            public.ecr.aws/docker/library/amazonlinux:latest \
            /bin/bash
        ```
    === "Windows / PowerShell"
        ```powershell
        finch run `
            --interactive `
            --tty `
            public.ecr.aws/docker/library/amazonlinux:latest `
            /bin/bash
        ```
    === "Linux"
        ```bash
        sudo finch run \
            --interactive \
            --tty \
            public.ecr.aws/docker/library/amazonlinux:latest \
            /bin/bash
        ```

* Start a container as a background process with the `--detach` flag.

    === "macOS / bash"
        ```bash
        finch run \
            --detach \
            --publish 80:80 \
            public.ecr.aws/nginx/nginx
        ```
    === "Windows / PowerShell"
        ```powershell
        finch run `
            --detach `
            --publish 80:80 `
            public.ecr.aws/nginx/nginx
        ```
    === "Linux"
        ```bash
        sudo finch run \
            --detach \
            --publish 80:80 \
            public.ecr.aws/nginx/nginx
        ```


## Next Steps

In this section, you learned how to run containers on Finch

* Next you can move on to [pushing container images](../pushing-images/) to
  container registries with Finch.
* To learn more about the `finch run` command see the [CLI
  Reference](../../cli-reference/finch_run/).
