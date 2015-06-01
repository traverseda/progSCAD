ProgScad comes with the following version constants so that you can easily determine if a progScad version is too new or too old.

We follow semantic versioning, which looks like "1.0.0", or "1,0". This can be read as "*MAJOR.MINOR.PATCH*".

 * MAJOR version when we make incompatible API changes,
 * MINOR version when we add functionality in a backwards-compatible manner, and
 * PATCH version when we make backwards-compatible bug fixes.

Generally, you should only be worried about MAJOR releases. If you try to use the 1.0.0 version of the library when the 2.0.0 verion of the library is installed on your system,
you're software is probably going to break.


The *progScadListVerion* constant makes it very easy to check the major version. It's a list container [MAJOR,MINOR] and sometimes PATCH.

Checking the major version is as easy as

    if (progScadListVerion[0] < 1 ){
        echo("This Design needs progScad 1.0.0 or newer")
    } else if (progScadListVerion[0] > 1 ){
        echo("This Design was written with the 1.0.0 release of progScad. New vesions might work, but they may result in hard to track down bugs and other strange behavior.")
        echo("Use at your own risk")
    }

with *progScadListVersion*.

Development (git) versions of progScad always have the version set to "0". If you want to test a script with a similar line in it on the latest version of progScad, you can simply say

    progScadListVersion=[9999,9999]

anywhere in your scad file.

We also provide some other constants you might find useful. You probably won't ever need to use any of these, but they're there if you need them.


|constant|example|
|---|---|
|progScadRawVersion^*|"1.0.0+untagged.1.g3d5e25c.dirty"|
|progScadVersion|"1.0.0"|
|progScadListVerion|[1,0,0]|
|progScadGitVersion|"3d5e25c2a63eba4deda3309b5df03b99655a6a85"|

*progScadRawVersion should be identical to progScadVersion, except when you're doing development work under git.
