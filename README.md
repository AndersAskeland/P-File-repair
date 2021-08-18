# P-File repair
## Overview
A simple tool to repair certain GE p-files that are corrupted. This is specifically a problem for certain v. 28 p-files. These files always contains 10058420 bytes and contains a lot of unused 0 values. The following software removes these values and rewrites the file.

Currently, the software only works with v. 28 files. If you encounter this problem with other files and wish to use this software, please submit a feature request.

Some code is adapted from the "spant" package (https://cran.r-project.org/web/packages/spant/index.html).

### Features
* Select folder or single file
* Fix p-file

### Possible future features
* Set custom surfix/prefix
* View header information

## Github information
Git commit messages are tagged using the following system.

```
[style]       Formatting, and typos
[doc]         Alterations to the documentation or code comments
[feature]     Added/changed feature
[fix]         Bug fixes
[clean]       Cleaned up the file structure
[test]        Testing new stuff
[major]       Major changes. Usually only used if doing a large rewrite.
