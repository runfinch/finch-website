# Uninstalling Finch

> This page is specific to Finch running on macOS. At this time macOS is the
> only supported operating system.

Depending on the installation method, the process to uninstall Finch varies. If
you are leveraging the [homebrew](https://brew.sh/) package manager, you can use
homebrew's [builtin uninstallation method](#uninstalling-finch-with-homebrew).
If you installed Finch using the Application Package, there is an [uninstall
script](#uninstalling-finch-with-the-uninstall-script) included in Finch.


## Uninstalling Finch with [homebrew](https://brew.sh/)

If you have installed Finch with the [homebrew](https://brew.sh/) package
manager, you can uninstall Finch using `brew uninstall`.

```bash
brew uninstall finch
```

The package manager should then go through cleaning up the relevant finch files.

```bash
==> Uninstalling Cask finch
==> Running uninstall script /Applications/Finch/uninstall.sh
Password:
Finch-v0.6.2 will be REMOVED.
Application uninstalling process started
[1/3] [DONE] Successfully deleted shortcut links
[2/3] [DONE] Successfully deleted application informations
[3/3] [DONE] Successfully deleted application
Application uninstall process finished
```

## Uninstalling Finch with the uninstall script

Within the Finch Application Package we include a
[script](https://github.com/runfinch/finch/blob/main/installer-builder/darwin/Resources/uninstall.sh)
to help with uninstallation. You must run the the uninstallation script as a
privileged user. When running this command you will be prompted for a password
for the privileged user.

```bash
sudo bash /Applications/Finch/uninstall.sh
```

At the confirmation prompt, enter `Y`.

```bash
Finch-v0.6.2 will be REMOVED.
Do you wish to continue [Y/n]?
```

After the script has finished, the uninstallation process is complete.