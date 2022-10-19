# Pushing Container Images

A container image stored on the local Finch virtual machine can be pushed to a
container registry using the `finch push` command.

## Authenticating to a Container Registry

Before a container image can be pushed to a container registry, it is common for
a registry to ask you to authenticate yourself. Depending on the container
registry you use, after you have logged in, you will be given a give an infinite
or a time based token. You can push and pull container images from that
container registry until your token expires.

=== "Amazon ECR"
    To login to [Amazon Elastic Container
    Registry](https://aws.amazon.com/ecr/), you first use the AWS CLI to
    retrieve an ECR Token. You then pass this to token to Finch with the finch
    login command.

    ```bash
    export AWS_REGION=eu-west-1
    export AWS_ACCOUNT_ID=111222333444

    aws ecr get-login-password --region $AWS_REGION | finch login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
    ```

    If the login has been successful, you should see:

    ```bash
    Login Succeeded
    ```

=== "Docker Hub"
    To login to [Docker Hub](https://hub.docker.com/), or any registry with
    username and password authentication. You can use the finch login command
    and enter the username and password when prompted.

    ```bash
    finch login
    Enter Username: username
    Enter Password:
    ```

    If the login has been successful, you should see:

    ```bash
    Login Succeeded
    ```

## Pushing a Container Image to an Image Repository

In [Building Container Images](../building_images/) we built the
[hello-finch](https://github.com/runfinch/finch/tree/main/contrib/hello-finch)
container image. In this section we will push a single from your local machine
to a container registry. These commands assume a repository has already been
created in the container registry.

1. Ensure the container image exists locally.

    ```bash
    finch image list
    ```

    Before pushing a container image, ensure the container image exists in the
    local image store.

    ```
    REPOSITORY     TAG       IMAGE ID        CREATED        PLATFORM       SIZE       BLOB SIZE
    hello-finch    latest    69b2528740fe    2 weeks ago    linux/arm64    1.8 MiB    1008.4 KiB
    ```

2. Re Tag the Container Image using the URI of the repository where you want to
   push the container image. The following example pushes a container image to
   an Amazon ECR repository.

    ```bash
    export AWS_REGION=eu-west-1
    export AWS_ACCOUNT_ID=111222333444

    finch tag \
      hello-finch:latest \
      $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/hello-finch:latest
    ```

3. Push the container image up to the container registry.

    ```bash
    finch push \
      $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/hello-finch:latest
    ```

4. Using the Console or the CLI of the container registry (in this example
   Amazon ECR), you can verify that the container image has been successfully
   pushed.

    ```bash
    aws ecr list-images --repository hello-finch
    {
        "imageIds": [
            {
                "imageDigest": "sha256:69b2528740fe3923f279594db844feca13b2a078e1101de17773ab54f01af9f5",
                "imageTag": "latest"
            }
        ]
    }
    ```

## Pushing a Multi-Architecture Container Image to a Repository

In [Building Container Images](../building_images/) we built a multi
architecture container image for the
[hello-finch](https://github.com/runfinch/finch/tree/main/contrib/hello-finch)
example application. In this section we will show how to push both architectures
of the container image, and a container image OCI [Image
Index](https://github.com/opencontainers/image-spec/blob/main/image-index.md), to
the container registry.

1. Ensure both architectures of the container image have been built and exist locally.

    ```bash
    finch image list
    REPOSITORY     TAG       IMAGE ID        CREATED          PLATFORM       SIZE       BLOB SIZE
    hello-finch    latest    5874669344b3    3 seconds ago    linux/arm64    1.8 MiB    1009.0 KiB
    hello-finch    latest    5874669344b3    3 seconds ago    linux/amd64    0.0 B      1.0 MiB
    ```

2. Re tag the container image using the URI of the repository where you want to
   push the container image. The following example pushes a container image to
   an Amazon ECR repository.

    ```bash
    export AWS_REGION=eu-west-1
    export AWS_ACCOUNT_ID=111222333444

    finch tag \
      hello-finch:latest \
      $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/hello-finch:latest
    ```

    You can verify both images have been re tagged using the `finch image list` command.

    ```bash
    finch image list
    ```

    Now you can see 4 images, 1 for each architecture for each tag.

    ```
    REPOSITORY                                                  TAG       IMAGE ID        CREATED               PLATFORM       SIZE       BLOB SIZE
    111222333444.dkr.ecr.eu-west-1.amazonaws.com/hello-finch    latest    5874669344b3    1 second ago          linux/arm64    1.8 MiB    1009.0 KiB
    111222333444.dkr.ecr.eu-west-1.amazonaws.com/hello-finch    latest    5874669344b3    1 second ago          linux/amd64    0.0 B      1.0 MiB
    hello-finch                                                 latest    5874669344b3    About a minute ago    linux/arm64    1.8 MiB    1009.0 KiB
    hello-finch                                                 latest    5874669344b3    About a minute ago    linux/amd64    0.0 B      1.0 MiB
    ```

3. Push the container images up to the container registry using the `--platform`
   flag to specify the architecture(s) you want to push.

    ```bash
    finch push \
      --platform linux/arm64,linux/amd64 \
      $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/hello-finch:latest
    ```

4. Using the Console or the CLI of the container registry (in this example
   Amazon ECR), you can verify that the container image has been successfully
   pushed. In the output below, you can see there are 3 digests. 1 corresponding
   to the [OCI Image
   Index](https://github.com/opencontainers/image-spec/blob/main/image-index.md)
   , and an [OCI Image
   Manifest](https://github.com/opencontainers/image-spec/blob/main/manifest.md)
   for each architecture.

    ```bash
    aws ecr list-images --repository hello-finch
    {
        "imageIds": [
            {
                "imageDigest": "sha256:5874669344b3de32c068f264063b1f146f55609ad2bf7384628487bd3b754a38",
                "imageTag": "latest"
            },
            {
                "imageDigest": "sha256:99a17e5c4245670452db0879127c58ddbf6c0110d1643f82a01ad2d0aba10dc6"
            },
            {
                "imageDigest": "sha256:7138727cd9f08d39d6a6f63fde0b5e1f735b9967fd1a918c50e1a5a8d09c9537"
            }
        ]
    }
    ```

## Next Steps

In this short section, you learned how to push container images on finch.

* To learn more about the `finch push` command see the [CLI
  Reference](/cli-reference/finch_push/).
