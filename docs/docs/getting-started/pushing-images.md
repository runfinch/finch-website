# Pushing Container Images

In [building container images](../building-images/) we built the
[hello-finch](https://github.com/runfinch/finch/tree/main/contrib/hello-finch)
container image. In this section we will push the container image from the local
workstation up to a container repository using the `finch push` command.

In the section we are pushing the container image to an existing [Amazon
ECR](https://aws.amazon.com/ecr/) repository, if you are using an alternative
container registry the authentication method and the container image tag will be
different.

1. Before pushing a container image, ensure the container image exists in the
   local image store.

    ```bash
    $ finch image list
    ```

    In the output you should see a list of all of the container images stored in
    the local container store.

    ```
    REPOSITORY     TAG       IMAGE ID        CREATED        PLATFORM       SIZE       BLOB SIZE
    hello-finch    latest    69b2528740fe    2 weeks ago    linux/arm64    1.8 MiB    1008.4 KiB
    ```

2. Within a container image name, we specify the container image repository
   where we want that image to be stored. To change the change name of the
   container image to the include the container image repository we use the
   `finch tag` command. The following example renames the container image to an
   Amazon ECR container image repo repository.

    === "macOS / bash"
        ```bash
        export AWS_ACCOUNT_ID=111222333444
        export AWS_REGION=eu-west-1

        finch tag \
        hello-finch:latest \
        $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/hello-finch:latest
        ```
    === "Windows / PowerShell"
        ```powershell
        $AWS_ACCOUNT_ID="111222333444"
        $AWS_REGION="eu-west-1"

        finch tag `
        hello-finch:latest `
        $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/hello-finch:latest
        ```

3. The Amazon ECR registry requires an authentication token to push and pull
   images. Therefore we need to login first with `finch login`. This may be
   different for your container image registry, see [registry
   authentication](../../container-images/authentication/) for more information.

    ```bash
    aws ecr get-login-password --region $AWS_REGION | finch login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
    ```

    If the login has been successful you should see:

    ```bash
    Login Succeeded
    ```

4. Using the `finch push` command we push the container image from the local
   machine up to the container image repository.

    ```bash
    finch push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/hello-finch:latest
    ```

4. With the AWS Console or the AWS CLI we can verify that the container image
   has been successfully pushed.

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

In [Building Container Images](../building-images/) we also built a multi
architecture container image for the
[hello-finch](https://github.com/runfinch/finch/tree/main/contrib/hello-finch)
example application. In this section we will show how to push both architectures
of the container image, and a container image OCI [Image
Index](https://github.com/opencontainers/image-spec/blob/main/image-index.md),
to the container registry.

1. Ensure both architectures of the container image have been built and exist
   locally.

    ```bash
    finch image list
    REPOSITORY     TAG       IMAGE ID        CREATED          PLATFORM       SIZE       BLOB SIZE
    hello-finch    latest    5874669344b3    3 seconds ago    linux/arm64    1.8 MiB    1009.0 KiB
    hello-finch    latest    5874669344b3    3 seconds ago    linux/amd64    0.0 B      1.0 MiB
    ```

2. Change the name of the container image using `finch tag` so the destination
   repository is included in the tag. The following example pushes a container
   image to an Amazon ECR repository.

    === "macOS / bash"
        ```bash
        export AWS_ACCOUNT_ID=111222333444
        export AWS_REGION=eu-west-1

        finch tag \
            hello-finch:latest \
            $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/hello-finch:latest
        ```
    === "Windows / PowerShell"
        ```powershell
        $AWS_ACCOUNT_ID="111222333444"
        $AWS_REGION="eu-west-1"

        finch tag `
            hello-finch:latest `
            "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/hello-finch:latest"
        ```

    You can verify both images have been re tagged using the `finch image list`
    command.

    ```bash
    finch image list
    ```

    Now you should see four images, one for each architecture for each tag.

    ```
    REPOSITORY                                                  TAG       IMAGE ID        CREATED               PLATFORM       SIZE       BLOB SIZE
    111222333444.dkr.ecr.eu-west-1.amazonaws.com/hello-finch    latest    5874669344b3    1 second ago          linux/arm64    1.8 MiB    1009.0 KiB
    111222333444.dkr.ecr.eu-west-1.amazonaws.com/hello-finch    latest    5874669344b3    1 second ago          linux/amd64    0.0 B      1.0 MiB
    hello-finch                                                 latest    5874669344b3    About a minute ago    linux/arm64    1.8 MiB    1009.0 KiB
    hello-finch                                                 latest    5874669344b3    About a minute ago    linux/amd64    0.0 B      1.0 MiB
    ```

3. The Amazon ECR registry requires an authentication token to push and pull
   images. Therefore we need to login first with `finch login`. This may be
   different for your container image registry, see [Registry
   Authentication](../../container-images/authentication/) for more information.

    ```bash
    aws ecr get-login-password --region $AWS_REGION | finch login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
    ```

    If the login has been successful you should see:

    ```bash
    Login Succeeded
    ```

4. Push the container images up to the container registry using the `--platform`
   flag to specify the architecture(s) you want to push.

    === "macOS / bash"
        ```bash
        finch push \
            --platform linux/arm64,linux/amd64 \
            $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/hello-finch:latest
        ```
    === "Windows / PowerShell"
        ```powershell
        finch push `
            --platform linux/arm64,linux/amd64 `
            $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/hello-finch:latest
        ```

5. With the AWS Console or the AWS CLI we can verify that the container image
   has been successfully pushed. In the output below, you can see there are 3
   digests. 1 corresponding to the [OCI Image
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
  Reference](../../cli-reference/finch_push/).
