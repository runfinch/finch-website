# Installing Finch

To install Finch, please see the dedicated section for each operating system
family:

- [macos](../managing-finch/macos/installation.md)

## Verify the Finch Installation

Once Finch has been successfully installed, you can verify the installation
with the following steps.

1. Ensure the Finch virtual machine is initialization and running with the
   `finch vm init`. This initial setup usually takes about a minute, and may
   once again require the users password.

    ```bash
    finch vm init
    ```

2. Verify that everything is working correctly by attempting to run the Finch
   demonstration container image `hello-finch`.

    ```bash
    finch run public.ecr.aws/finch/hello-finch:latest
    ```

    If everything is ok, you should now see the output:

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

## Next Steps

In this short guide you learned how to install Finch on to your macOS workstation and
start the virtual machine.

* To learn how to run your first containerized application see [Running
  Containers](../running-containers/).