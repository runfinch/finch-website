# Installing Finch optional components on Linux

Finch on Linux can make use of some optional components. On other Finch platforms, some of these optional components are installed at runtime. This works well for platforms where Finch has its own isolated VM environment, but runtime management of system dependencies on a shared system is more problematic, so these optional components must be installed and configured manually on Linux at this time.

## SOCI snapshotter

The [SOCI snapshotter](https://github.com/awslabs/soci-snapshotter?tab=readme-ov-file) ("SOCI" is short for "Seekable OCI", and is pronounced "so-CHEE") is a containerd snapshotter plugin which enables standard OCI images to be lazily loaded without requiring a build-time conversion step. 

Follow the steps corresponding with your distribution in order to use the SOCI snapshotter with Finch on Linux.

### Amazon Linux

SOCI is packaged in the standard Amazon Linux repositories. That means, installing SOCI is as easy as installing any other Amazon Linux package:

=== "AL2023"
    
    ```shell
    $ sudo dnf install soci-snapshotter
    ```

=== "AL2"
    
    ```shell
    $ sudo amazon-linux-extras enable docker
    $ sudo yum install soci-snapshotter
    ```

SOCI also requires a daemon, which can be started with systemd after package installation:

```shell
$ sudo systemctl start soci-snapshotter
```

### Generic

1. Download the SOCI binary archive corresponding to your system's architecture from [the project's Releases tab](https://github.com/awslabs/soci-snapshotter/releases), and extract it using a command like `tar Cxzvvf /usr/local/bin soci-snapshotter-${SOCI_VERSION}-linux-amd64-static.tar.gz ./soci ./soci-snapshotter-grpc`
1. Run the SOCI snapshotter GRPC daemon system service using a service manager, like systemd, or directly. An example systemd service file can be found [here](https://github.com/awslabs/soci-snapshotter/blob/main/soci-snapshotter.service).
1. Configure containerd to contain a `proxy_plugin` config section for SOCI, by following [these instructions](https://github.com/awslabs/soci-snapshotter/blob/main/docs/install.md#config-containerd).

## ECR Credential Helper

[The Amazon ECR Docker Credential Helper](https://github.com/awslabs/amazon-ecr-credential-helper) is a [credential helper](https://github.com/docker/docker-credential-helpers) for the Docker daemon that makes it easier to use [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/). It removes the need to directly manage registry credentials via traditional `login` commands, making it easier to push/pull from authenticated ECR registries.

### Amazon Linux

The ECR Credential Helper is packaged in the standard Amazon Linux repositories. That means, installing ECR Credential Helper is as easy as installing any other Amazon Linux package:

=== "AL2023"

    ```shell
    $ sudo dnf install amazon-ecr-credential-helper
    ```

=== "AL2"

    ```shell
    $ sudo amazon-linux-extras enable docker
    $ sudo yum install amazon-ecr-credential-helper
    ```

### Generic

1. Download the ECR Credential Helper binary corresponding to your system's architecture from [the project's Releases tab](https://github.com/awslabs/amazon-ecr-credential-helper/releases), and set it's executable bit using `chmod +x docker-credential-ecr-login`.
1. Move the executable to a location within the root user's `PATH` (e.g. `mv docker-credential-ecr-login /bin/docker-credential-ecr-login`)

### Configuration

The ECR Credential Helper must also be configured for the root user's docker config, which can be found at `/root/.docker/config.json`. Follow the steps in [this guide](https://github.com/awslabs/amazon-ecr-credential-helper?tab=readme-ov-file#configuration) to configure the credential helper.