# Building Container Images

Finch leverages Moby's [BuildKit](https://github.com/moby/buildkit) to build
container images defined in a
[Dockerfile](https://docs.docker.com/engine/reference/builder/). To interact
with BuildKit you use the `finch build` command.

## Building a Container Image

A sample application called
[hello-finch](https://github.com/runfinch/finch/tree/main/contrib/hello-finch)
is included in the [Finch
Repository](https://github.com/runfinch/finch/tree/main/contrib/hello-finch). In
this guide we will clone this Finch repository, and build
[hello-finch](https://github.com/runfinch/finch/tree/main/contrib/hello-finch).

1. Clone the [Finch](https://github.com/runfinch/finch) repository.

    ```bash
    git clone https://github.com/runfinch/finch.git
    ```

2. Navigate to the
   [hello-finch](https://github.com/runfinch/finch/tree/main/contrib/hello-finch)
   application.

    ```bash
    cd finch/contrib/hello-finch
    ```

3. Build
   [hello-finch](https://github.com/runfinch/finch/tree/main/contrib/hello-finch)
   with the `finch build`. Here we specifying the tag that we want to use for
   the image, as well as where the build context can be found.

    ```bash
    finch build \
      --tag hello-finch \
      .
    ```

4. You can see the newly build container image in the image store using the
   `finch image list` command.

    ```bash
    finch image list
    ```

    The output shows your new container image, the platform it was built for and
    the uncompressed size.

    ```
    REPOSITORY     TAG       IMAGE ID        CREATED        PLATFORM       SIZE       BLOB SIZE
    hello-finch    latest    69b2528740fe    2 weeks ago    linux/arm64    1.8 MiB    1008.4 KiB
    ```

## Building a Multi Architecture Container Image

By default Finch will build a container image that corresponds to your local
machine, i.e. an x86 container image when running on an Intel machine, an arm64
when running on a Apple Silicon machine. If you wish to build a container image
for an alternative architecture, or multiple architectures at the same time,
then you can use the `--platform` flag with `finch build`.

1. Once again we will build the
   [hello-finch](https://github.com/runfinch/finch/tree/main/contrib/hello-finch)
   demo application. If you haven't already, clone the
   [Finch](https://github.com/runfinch/finch) repository.

    ```bash
    git clone https://github.com/runfinch/finch.git
    ```

2. Navigate to the
   [hello-finch](https://github.com/runfinch/finch/tree/main/contrib/hello-finch)
   application.

    ```bash
    cd finch/contrib/hello-finch
    ```

3. Build
   [hello-finch](https://github.com/runfinch/finch/tree/main/contrib/hello-finch)
   with the `finch build`. Here we specify an alternative architecture with the
   `--platform` flag. Here you could specify a single architecture `--platform
   linux/amd64` or multiple architectures `--platform linux/arm64,linux/amd64`.

    ```bash
    finch build \
      --platform linux/arm64,linux/amd64 \
      --tag hello-finch \
      .
    ```

4. You can see both container images in the local image store, with the `finch
   image list` command.

    ```bash
    finch image list
    ```

    Notice how there are 2 images, one for each architecture.

    ```
    REPOSITORY     TAG       IMAGE ID        CREATED        PLATFORM       SIZE       BLOB SIZE
    hello-finch    latest    5874669344b3    2 weeks ago    linux/arm64    1.8 MiB    1009.0 KiB
    hello-finch    latest    5874669344b3    2 weeks ago    linux/amd64    0.0 B      1.0 MiB
    ```

## Next Steps

In this short section, you learned how to build container images on finch.

* To learn how to run these Container Images navigate to [Running
  Containers](../running_containers/)
* To learn more about the `finch build` command see the [CLI
  Reference](/cli-reference/finch_build/)
