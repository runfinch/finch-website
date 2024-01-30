[Lazy loading](https://en.wikipedia.org/wiki/Lazy_loading) container images is a
technique where instead of downloading all of the container image data then
starting the container, instead you start the container first and only download
container image data when the application requests it. Reducing the time taken
to launch containers.

Within Finch you can change the [containerd
snapshotter](https://github.com/containerd/containerd/tree/main/docs/snapshotters),
the containerd component that manages the container images, to allow you to use
lazy loading container images. At this time only the [Seekable OCI
(SOCI)](https://github.com/awslabs/soci-snapshotter) lazy loading snapshotter is
supported.

## Enable the SOCI Snapshotter

To enable the SOCI snapshotter, you need to edit the [Finch configuration
file](../configuration-reference/) and add the SOCI snapshotter. The Finch
configuration file is typically located at `~/.finch/finch.yaml`

```bash
snapshotters:
    - soci
```

After adding SOCI to the Finch configuration file you need to start and stop the
Finch virtual machine.

```bash
finch vm stop
finch vm start
```

## Generate SOCI Indexes

In Finch you can generate [Seekable OCI (SOCI)
Indexes](https://github.com/awslabs/soci-snapshotter/blob/main/docs/glossary.md#terminology)
to enable container images to be lazy loaded in other environments.

Before a SOCI index can be generated, the container image needs to exist
locally. This could be because you have just built the container image from
`finch build` or maybe because you have downloaded an existing image from a
container repository with `finch pull`.

Finch generates the SOCI index when the container image is pushed to a container
repository. Therefore before pushing the container image we may need to retag
the container image with `finch tag`, adding the destination repository to the
container image name. To generate the SOCI index and to push the container image
use the `finch push --snapshotter soci` command.

=== "macOS / bash"
    ```bash
    AWS_ACCOUNT_ID=111222333444
    AWS_REGION=eu-west-1

    finch push --snapshotter soci \
        $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/myimage:latest
    ```
=== "Windows / PowerShell"
    ```powershell
    $AWS_ACCOUNT_ID="111222333444"
    $AWS_REGION="eu-west-1"

    finch push --snapshotter soci `
        "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/myimage:latest"
    ```

In the output, you will see that Finch first pushes the container image up to the
container registry.

```bash
manifest-sha256:fd96e40d576375699bd94093a2a5005d857d252e25ab35e03294069e90d856da: done           |++++++++++++++++++++++++++++++++++++++|
config-sha256:7cbe3f4c79232396f3d55fafefb47f23aba5dee91934c68be4fc6a7e497a0b22:   done           |++++++++++++++++++++++++++++++++++++++|
elapsed: 22.7s                                                                    total:  2.2 Ki (97.0 B/s)
```

Finch will then generate the SOCI index and push that to the container image
repository to sit alongside the container image.

```bash
INFO[0022] soci: ztoc skipped - layer sha256:5aca968bda346aa3f3ae7e781a45d10a1f17df3d45a4bc05f201b7261e127c36 (application/vnd.docker.image.rootfs.diff.tar.gzip) size 628 is less than min-layer-size 10485760
INFO[0024] soci: layer sha256:2b92a4a464539d6c28ffd6b40875226086ace1e24d6598d771d8a65a6938acb1 -> ztoc sha256:495590adbcade7a74ddf76463c8e912ea1de56f4cf20e36ee9146ac8939b4301
INFO[0027] soci: layer sha256:b3c399da943c0747be26ad2d7858e7c1eac894c51592dfe10c98b0737b07609d -> ztoc sha256:41797408337b0bff3b57626338c482a2c0bc09383c24af5a26d8545ec96920d7
INFO[0027] soci: checking if a soci index already exists in remote repository...
INFO[0027] soci: pushing soci index with digest: sha256:b8005edf213e3ef96bff588690c618a778adb88801db7acf9256b0bdd841b006
INFO[0027] soci: pushing artifact with digest: sha256:495590adbcade7a74ddf76463c8e912ea1de56f4cf20e36ee9146ac8939b4301
INFO[0027] soci: pushing artifact with digest: sha256:44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a
INFO[0027] soci: skipped artifact with digest: sha256:fd96e40d576375699bd94093a2a5005d857d252e25ab35e03294069e90d856da
INFO[0027] soci: pushing artifact with digest: sha256:41797408337b0bff3b57626338c482a2c0bc09383c24af5a26d8545ec96920d7
INFO[0028] soci: successfully pushed artifact with digest: sha256:44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a
INFO[0028] soci: successfully pushed artifact with digest: sha256:495590adbcade7a74ddf76463c8e912ea1de56f4cf20e36ee9146ac8939b4301
INFO[0029] soci: successfully pushed artifact with digest: sha256:41797408337b0bff3b57626338c482a2c0bc09383c24af5a26d8545ec96920d7
INFO[0029] soci: pushing artifact with digest: sha256:b8005edf213e3ef96bff588690c618a778adb88801db7acf9256b0bdd841b006
INFO[0030] soci: successfully pushed artifact with digest: sha256:b8005edf213e3ef96bff588690c618a778adb88801db7acf9256b0bdd841b006
```

## Lazy Load a container image with SOCI

To lazy load a container image with SOCI, ensure that the image does not exist
on the local virtual machine with `finch image ls` and that a SOCI index has
been generated and is stored in the container repository alongside the container
image.

To run the container, you need to pass `--snapshotter soci` into the `finch run` command.

=== "macOS / bash"
    ```bash
    AWS_ACCOUNT_ID=111222333444
    AWS_REGION=eu-west-1

    finch run --snapshotter soci \
        $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/myimage:latest
    ```
=== "Windows / PowerShell"
    ```powershell
    $AWS_ACCOUNT_ID="111222333444"
    $AWS_REGION="eu-west-1"

    finch run --snapshotter soci `
        "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/myimage:latest"
    ```

**Successful Lazy Loading**

If the container image has been successfully lazy loaded you should notice an
improvement in launch time, additionally when the image was downloaded, you
should not see each layer being individually downloaded.

```bash
$ finch run --snapshotter soci $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/myimage:latest
111222333444.dkr.ecr.eu-west-1.amazonaws.com/myimage:latest:                      resolved       |++++++++++++++++++++++++++++++++++++++|
manifest-sha256:fd96e40d576375699bd94093a2a5005d857d252e25ab35e03294069e90d856da: done           |++++++++++++++++++++++++++++++++++++++|
config-sha256:7cbe3f4c79232396f3d55fafefb47f23aba5dee91934c68be4fc6a7e497a0b22:   done           |++++++++++++++++++++++++++++++++++++++|
elapsed: 15.4s
```

**Unsuccessful Lazy Loading**

If a SOCI Index does not exist or if the `soci-snapshotter` is unable to access
the SOCI Index, the snapshotter will fail back to downloading the container
image in full before starting the container image. The most obvious way to know
this has happened is that each container image layer will be downloaded in full,
before the container starts.

```bash
$ finch run --snapshotter soci $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/myimage:latest
111222333444.dkr.ecr.eu-west-1.amazonaws.com/myimage:latest:                      resolved       |++++++++++++++++++++++++++++++++++++++|
manifest-sha256:fd96e40d576375699bd94093a2a5005d857d252e25ab35e03294069e90d856da: done           |++++++++++++++++++++++++++++++++++++++|
config-sha256:7cbe3f4c79232396f3d55fafefb47f23aba5dee91934c68be4fc6a7e497a0b22:   done           |++++++++++++++++++++++++++++++++++++++|
layer-sha256:5aca968bda346aa3f3ae7e781a45d10a1f17df3d45a4bc05f201b7261e127c36:    done           |++++++++++++++++++++++++++++++++++++++|
layer-sha256:2b92a4a464539d6c28ffd6b40875226086ace1e24d6598d771d8a65a6938acb1:    downloading    |++++++++++++++++++++++----------------| 35.0 MiB/59.6 MiB
layer-sha256:b3c399da943c0747be26ad2d7858e7c1eac894c51592dfe10c98b0737b07609d:    downloading    |++++++--------------------------------| 28.8 MiB/179.7 MiB
elapsed: 22.0s                                                                    total:  63.8 M (5.3 MiB/s)
```