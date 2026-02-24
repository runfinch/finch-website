## Authenticating to a Container Registry

Before a container image can be pushed to a container image repository, it is
common for the image registry to ask you to authenticate yourself. Depending on
the image registry you are using, you either authenticate yourself through the
`finch login` command, or you can leverage [credential
helpers](https://docs.docker.com/engine/reference/commandline/login/#credential-helpers),
to manage authentication tokens on your behalf.

### Credential Helper Options

Finch supports the following authentication and credential storage methods:

- **User Keychain (macOS)**: `osxkeychain` is configured by default in `~/.finch/config.json`, allowing credentials to be securely stored in the encrypted macOS Keychain.
- **Manual configuration**: Configure supported helpers like `ecr-login` in `~/.finch/config.json`.
- **Manual login**: Authenticate directly with `finch login`.
- **Docker credential helpers**: Falls back on Docker's credential helpers if available (requires Docker Desktop).

**Important:** Finch does not support system credential stores for Windows (`wincred`) or Linux (`secretservice`). Configuring these in `~/.finch/config.json` will fail to authenticate.

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

        If the login has been successful, you should see:

        ```bash
        Login Succeeded
        ```

        For multiple accounts, ensure all profiles are configured in `~/.aws/credentials`, then login as follows:

        ```bash
        export AWS_ACCOUNT_ID_1=111222333444
        export AWS_ACCOUNT_ID_2=555666777888
        export AWS_REGION_1=us-east-1
        export AWS_REGION_2=eu-west-1

        AWS_PROFILE=$AWS_ACCOUNT_ID_1 aws ecr get-login-password --region $AWS_REGION_1 | finch login --username AWS --password-stdin $AWS_ACCOUNT_ID_1.dkr.ecr.$AWS_REGION_1.amazonaws.com
        AWS_PROFILE=$AWS_ACCOUNT_ID_2 aws ecr get-login-password --region $AWS_REGION_2 | finch login --username AWS --password-stdin $AWS_ACCOUNT_ID_2.dkr.ecr.$AWS_REGION_2.amazonaws.com
        ```

        After logging in, subsequent finch operations will use the stored credentials and do not require `AWS_PROFILE`.

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

        For multiple accounts, ensure all profiles are configured in `~/.aws/credentials`, then login as follows:

        ```powershell
        $AWS_ACCOUNT_ID_1="111222333444"
        $AWS_ACCOUNT_ID_2="555666777888"
        $AWS_REGION_1="us-east-1"
        $AWS_REGION_2="eu-west-1"

        $env:AWS_PROFILE=$AWS_ACCOUNT_ID_1; aws ecr get-login-password --region $AWS_REGION_1 | finch login --username AWS --password-stdin "$AWS_ACCOUNT_ID_1.dkr.ecr.$AWS_REGION_1.amazonaws.com"
        $env:AWS_PROFILE=$AWS_ACCOUNT_ID_2; aws ecr get-login-password --region $AWS_REGION_2 | finch login --username AWS --password-stdin "$AWS_ACCOUNT_ID_2.dkr.ecr.$AWS_REGION_2.amazonaws.com"
        ```

        After logging in, subsequent finch operations will use the stored credentials and do not require `AWS_PROFILE`.

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

=== "Native Credential Stores"

    #### Using the macOS Keychain for secure credential storage

    The macOS Keychain is a built-in password manager that stores credentials
    encrypted-at-rest. This is preferable over the default behavior of storing 
    credentials as plaintext in `~/.finch/config.json`, and is configured by default. 
    Similar functionality for Windows Credential Manager is not currently supported.

    To ensure that the macOS Keychain is being used, confirm that 
    `osxkeychain` is set as the credstore in `~/.finch/config.json`:

    ```
    {
        "credsStore": "osxkeychain"
    }
    ```

    If it is not configured, you can either set it manually or delete the file and 
    login to a desired registry, which will automatically configure it.

    This depends on `docker-credential-osxkeychain`, a standard helper for interacting
    with the macOS keychain. Ensure that it exists in `/usr/local/bin` (or any directory 
    in `PATH`):

    ```
    where docker-credential-osxkeychain
    ```

    If it is not installed, you have two options:

    1. Copy the version of the binary shipped with Finch into `PATH`:

    ```
    cp /Applications/Finch/cred-helpers/docker-credential-osxkeychain /usr/local/bin/docker-credential-osxkeychain
    ```

    2. Install via `brew`:

    ```
    brew install docker-credential-helper
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

    For multiple accounts, ensure all profiles are configured in `~/.aws/credentials`, then login as follows:

    ```bash
    export AWS_ACCOUNT_ID_1=111222333444
    export AWS_ACCOUNT_ID_2=555666777888
    export AWS_REGION_1=us-east-1
    export AWS_REGION_2=eu-west-1

    AWS_PROFILE=$AWS_ACCOUNT_ID_1 aws ecr get-login-password --region $AWS_REGION_1 | sudo -E finch login --username AWS --password-stdin $AWS_ACCOUNT_ID_1.dkr.ecr.$AWS_REGION_1.amazonaws.com
    AWS_PROFILE=$AWS_ACCOUNT_ID_2 aws ecr get-login-password --region $AWS_REGION_2 | sudo -E finch login --username AWS --password-stdin $AWS_ACCOUNT_ID_2.dkr.ecr.$AWS_REGION_2.amazonaws.com
    ```

    After logging in, subsequent finch operations will use the stored credentials and do not require `AWS_PROFILE`.

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
