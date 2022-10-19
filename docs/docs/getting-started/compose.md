# Using Compose with Finch

Containerized applications composed of multiple services are often defined in
[Docker Compose
files](https://compose-spec.io/). Finch
offers a CLI that is compatible to the
[docker-compose](https://github.com/docker/compose) cli, therefore commands that
you have used previously like `docker-compose up` could be translated to `finch
compose up`.

## Building Containers Images with a Compose File

A service defined in a compose file can be built with the `finch compose`
command. To do so, add the
[build](https://docs.docker.com/compose/compose-file/#build) key, with the value
set as local context to use.

1. In the
   [hello-finch](https://github.com/runfinch/finch/tree/main/contrib/hello-finch)
   sample application directory, we can create a Compose file. In the file we
   define the `hello-finch` service and provide a context for the container
   image build.

    ```bash
    git clone https://github.com/runfinch/finch.git
    cd finch/contrib/hello-finch

    # Add a Docker Compose File to the Directory
    cat <<EOF > docker-compose.yml
    services:
      hello-finch:
        image: hello-finch
        build: .
    EOF
    ```

2. Build the container images using `finch compose build`.

    ```bash
    finch compose build
    ```

3. You can verify that the container image has been built successfully using the
   `finch image list` command.

    ```bash
    finch image list
    ```

    The output should show the container image tagged with the service name.

    ```
    REPOSITORY     TAG       IMAGE ID        CREATED           PLATFORM       SIZE       BLOB SIZE
    hello-finch    latest    69b2528740fe    49 seconds ago    linux/arm64    1.8 MiB    1008.4 KiB
    ```

## Running Containers with a Compose File

1 or more services can be defined in a compose file, and then all services can
be started with the `finch compose up` command.

1. Leveraging the
   [hello-finch](https://github.com/runfinch/finch/tree/main/contrib/hello-finch)
   sample application, we can create a Docker Compose file. In the file we
   define the `hello-finch` service and provide a context for the container
   image build.

    ```bash
    git clone https://github.com/runfinch/finch.git
    cd finch/contrib/hello-finch

    # Add a Docker Compose File to the Directory
    cat <<EOF > docker-compose.yml
    services:
      hello-finch:
        image: hello-finch
        build: .
    EOF
    ```

2. Next we will run the service with `finch compose up`, if the container image
   does not exist locally, finch will build the container image before starting
   the service.

    ```bash
    finch compose up
    INFO[0018] Creating container hello-finch_hello-finch_1
    INFO[0018] Attaching to logs
    hello-finch_1 |
    hello-finch_1 |                            @@@@@@@@@@@@@@@@@@@
    hello-finch_1 |                        @@@@@@@@@@@@    @@@@@@@@@@@
    hello-finch_1 |                      @@@@@@@                  @@@@@@@
    hello-finch_1 |                    @@@@@@                        @@@@@@
    hello-finch_1 |                  @@@@@@                            @@@@@
    hello-finch_1 |                 @@@@@                      @@@#     @@@@@@@@@
    hello-finch_1 |                @@@@@                     @@   @@@       @@@@@@@@@@
    hello-finch_1 |                @@@@%                     @     @@            @@@@@@@@@@@
    hello-finch_1 |                @@@@                                               @@@@@@@@
    hello-finch_1 |                @@@@                                         @@@@@@@@@@@&
    hello-finch_1 |                @@@@@                                  &@@@@@@@@@@@
    hello-finch_1 |                 @@@@@                               @@@@@@@@
    hello-finch_1 |                  @@@@@                            @@@@@(
    hello-finch_1 |                   @@@@@@                        @@@@@@
    hello-finch_1 |                     @@@@@@@                  @@@@@@@
    hello-finch_1 |                        @@@@@@@@@@@@@@@@@@@@@@@@@@
    hello-finch_1 |                            @@@@@@@@@@@@@@@@@@
    hello-finch_1 |
    hello-finch_1 |
    hello-finch_1 |Hello from Finch!
    hello-finch_1 |
    hello-finch_1 |Visit us @ github.com/runfinch
    hello-finch_1 |
    INFO[0018] Container "hello-finch_hello-finch_1" exited
    INFO[0018] All the containers have exited
    INFO[0018] Stopping containers (forcibly)
    INFO[0018] Stopping container hello-finch_hello-finch_1
    ```

## Next Steps

In this short section, you learned how to use Compose files with Finch.

* To learn about leveraging Compose files with Finch, see the [Finch
  Compose](/cli-reference/finch_compose/) reference.
