## Authenticating to a Container Registry

Before a container image can be pushed to a container image repository, it is
common for the image registry to ask you to authenticate yourself. Depending on
the image registry you are using, you either authenticate yourself through the
`finch login` command, or you can leverage [credential
helpers](https://docs.docker.com/engine/reference/commandline/login/#credential-helpers),
to manage authentication tokens on your behalf.

### Credential Helper Options

Finch supports the following authentication methods:

- **Manual configuration**: Configure supported helpers like `ecr-login` in `~/.finch/config.json`.
- **Manual login**: Authenticate directly with `finch login`.
- **Docker credential helpers**: Falls back on Docker's credential helpers if available (requires Docker Desktop).

**Important:** Finch does not support system credential stores (`osxkeychain`, `wincred`, `secretservice`) directly. Configuring these in `~/.finch/config.json` will fail to authenticate.

### macOS and Windows

=== "Amazon ECR"

    #### Using the Amazon ECR Credential Helper to login to Amazon ECR

    The Amazon ECR Credential Helper is a credential helper that handles
    [Amazon ECR](https://aws.amazon.com/ecr/) authentication tokens for you. It
    does this by leveraging the AWS credentials used by the the AWS CLI, typically
    these are located on the workstation at `~/.aws/credentials`.

    To configure the Amazon ECR credential helper:

    1. Ensure the [AWS
       credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
       have been configured and are working correctly on the host local machine
       before attempting to using the Amazon ECR credential helper.

        ```bash
        aws sts get-caller-identity
        ```

    2. Add the `ecr-login` to the `creds_helpers` section of the [Finch
       configuration file](../../configuration-reference). The file is found at:
        `~/.finch/finch.yaml`.

        ```bash
        cpus: 3
        memory: 4GiB
        creds_helpers:
            - ecr-login
        ```

    3. If it does not already exist, add `ecr-login` to the registry credentials
       file located at `~/.finch/config.json`

        ```bash
        {
        	"credsStore": "ecr-login"
        }
        ```

    4. Stop and start the Finch virtual machine to pick up the new configuration.

        ```
        finch vm stop
        finch vm start
        ```

    #### Using the AWS CLI to login to Amazon ECR

    Alternatively you can use the AWS CLI to retrieve an
    [Amazon ECR](https://aws.amazon.com/ecr/) authentication token and pass this
    into Finch with the `finch login` command. By default this token expires after
    12 hours.

    === "macOS / bash"
        ```bash
        export AWS_ACCOUNT_ID=111222333444
        export AWS_REGION=eu-west-1

        aws ecr get-login-password --region $AWS_REGION | finch login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
        ```
    === "Windows / PowerShell"
        ```powershell
        $AWS_ACCOUNT_ID="111222333444"
        $AWS_REGION="eu-west-1"

        aws ecr get-login-password --region $AWS_REGION | finch login --username AWS --password-stdin "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com"
        ```

    If the login has been successful, you should see:

    ```bash
    Login Succeeded
    ```

=== "Amazon ECR Public"

    #### Using the Amazon ECR Credential Helper to login to Amazon ECR Public

    The Amazon ECR Credential Helper is a credential helper that handles [Amazon ECR Public](https://gallery.ecr.aws/) authentication tokens for you. It does
    this by leveraging the AWS credentials used by the the AWS CLI, typically these are located on the workstation at `~/.aws/credentials`.

    To configure the Amazon ECR credential helper:

    1. Ensure the [AWS
       credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
       have been configured and are working correctly on the host local machine
       before attempting to using the Amazon ECR credential helper.

        ```bash
        aws sts get-caller-identity
        ```

    2. Add the `ecr-login` to the `creds_helpers` section of the [Finch
       configuration file](../../configuration-reference). The file is found at:
        `~/.finch/finch.yaml`.

        ```bash
        cpus: 3
        memory: 4GiB
        creds_helpers:
            - ecr-login
        ```

    3. If it does not already exist, add `ecr-login` to the registry credentials
       file located at `~/.finch/config.json`

        ```bash
        {
        	"credsStore": "ecr-login"
        }
        ```

    4. Stop and start the Finch virtual machine to pick up the new configuration.

        ```
        finch vm stop
        finch vm start
        ```

    #### Using the AWS CLI to login to Amazon ECR Public

    Alternatively you can use the AWS CLI to retrieve an [Amazon ECR Public]
    (https://gallery.ecr.aws/) authentication token and pass this into
    Finch with the `finch login` command. By default this token expires after 12
    hours.

    ```bash
    # Note that the region will always be us-east-1 when authenticating to ECR Public.
    aws ecr-public get-login-password --region us-east-1 | finch login --username AWS --password-stdin public.ecr.aws
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

### Linux

=== "Amazon ECR"

    #### Using the Amazon ECR Credential Helper to login to Amazon ECR

    The Amazon ECR Credential Helper is a credential helper that handles
    [Amazon ECR](https://aws.amazon.com/ecr/) authentication tokens for you. It
    does this by leveraging the AWS credentials used by the the AWS CLI, typically
    these are located on the workstation at `~/.aws/credentials`. Since Finch requires
    being run as root, this may be `/root/.aws/credentials`.

    To configure the Amazon ECR credential helper:

    1. Ensure the [AWS
       credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
       have been configured and are working correctly on the host local machine
       before attempting to using the Amazon ECR credential helper.

        ```bash
        aws sts get-caller-identity
        ```

    2. Install the ecr credential helper by following [these steps](./../../managing-finch/linux/optional-components/#ecr-credential-helper).
    

    3. If it does not already exist, add `ecr-login` to the registry credentials
       file located at `/root/.docker/config.json`

        ```bash
        {
        	"credsStore": "ecr-login"
        }
        ```

    #### Using the AWS CLI to login to Amazon ECR

    Alternatively you can use the AWS CLI to retrieve an
    [Amazon ECR](https://aws.amazon.com/ecr/) authentication token and pass this
    into Finch with the `finch login` command. By default this token expires after
    12 hours.

    ```bash
    export AWS_ACCOUNT_ID=111222333444
    export AWS_REGION=eu-west-1

    aws ecr get-login-password --region $AWS_REGION | sudo -E finch login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
    ```

    If the login has been successful, you should see:

    ```bash
    Login Succeeded
    ```

=== "Amazon ECR Public"

    #### Using the Amazon ECR Credential Helper to login to Amazon ECR Public

    The Amazon ECR Credential Helper is a credential helper that handles [Amazon ECR Public](https://gallery.ecr.aws/) authentication tokens for you. It does
    this by leveraging the AWS credentials used by the the AWS CLI, typically these are located on the workstation at `~/.aws/credentials`.

    To configure the Amazon ECR credential helper:

    1. Ensure the [AWS
       credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
       have been configured and are working correctly on the host local machine
       before attempting to using the Amazon ECR credential helper.

        ```bash
        aws sts get-caller-identity
        ```

    2. Install the ecr credential helper by following [these steps](./../../managing-finch/linux/optional-components#ecr-credential-helper).

    3. If it does not already exist, add `ecr-login` to the registry credentials
       file located at `/root/.docker/config.json`

        ```bash
        {
        	"credsStore": "ecr-login"
        }
        ```

    #### Using the AWS CLI to login to Amazon ECR Public

    Alternatively you can use the AWS CLI to retrieve an [Amazon ECR Public]
    (https://gallery.ecr.aws/) authentication token and pass this into
    Finch with the `finch login` command. By default this token expires after 12
    hours.

    ```bash
    # Note that the region will always be us-east-1 when authenticating to ECR Public.
    aws ecr-public get-login-password --region us-east-1 | sudo finch login --username AWS --password-stdin public.ecr.aws
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
    sudo finch login
    Enter Username: username
    Enter Password:
    ```

    If the login has been successful, you should see:

    ```bash
    Login Succeeded
    ```
