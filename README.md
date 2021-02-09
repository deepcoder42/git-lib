# Python project that contains libraries and classes for Git repository use.
# Classification (U)

# Description:
  This program is used to interact with local and remote Git repositories and have capbility to merge repositories.  It contains classes and libraries for both local and remote Git repositories.

###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Testing
    - Unit


# Features:
  * Class that initializes and sets up instances to the Python git repository and git command line instances.
  * Class that handles operations of merging a git repository with a remote git repository.


# Prerequisites:

  * List of Linux packages that need to be installed on the server:
    - git
    - python-pip

  * Local class/library dependencies within the program structure:
    - lib/gen_libs


# Installation:
  There are two types of installs: pip and git.

### Pip Installation:
  * Replace **{Other_Python_Project}** with the baseline path of another python program.

##### Create requirements file in another program's project to install git-lib as a library module.

Create requirements-git-lib.txt file:
```
vim {Other_Python_Project}/requirements-git-lib.txt
```

Add the following lines to the requirements-git-lib.txt file:
```
git+ssh://git@github.com/deepcoder42/git-lib.git#egg=git-lib
```

Create requirements-python-lib.txt file:
```
vim {Other_Python_Project}/requirements-python-lib.txt
```

Add the following lines to the requirements-python-lib.txt file:
```
git+ssh://git@github.com/deepcoder42/python-lib.git#egg=python-lib
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.

Modify the README.md file:
```
vim {Other_Python_Project}/README.md
```

Add the following lines under the "Install supporting classes and libraries" section.
```
   pip install -r requirements-git-lib.txt --target git_lib
   pip install -r requirements-python-lib.txt --target git_lib/lib
```

##### Add the general Git-lib requirements to the other program's requirements.txt file.  Remove any duplicates.

Modify the requirements.txt file:
```
vim {Other_Python_Project}/requirements.txt
```

Add the following lines to the requirements.txt file:
```
gitdb2==2.0.4
GitPython==2.1.8
smmap2==2.0.4
```


### Git Installation:

Install general Git libraries and classes using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}
git clone git@github.com:deepcoder42/git-lib.git
```

Install/upgrade system modules:
```
cd git-lib
sudo bash
umask 022
pip install -r requirements.txt --upgrade
exit
```

Install supporting classes and libraries:
```
pip install -r requirements-python-lib.txt --target lib
```


# Testing:

# Unit Testing:

### Description: Testing consists of unit testing for the functions in the git_class.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * If pulling down another branch other than master then use the "--branch {Branch_Name}" option.

```
umask 022
cd {Python_Project}
git clone git@github.com:deepcoder42/git-lib.git
```

Install/upgrade system modules:
```
cd git-lib
sudo bash
umask 022
pip install -r requirements.txt --upgrade
exit
```

Install supporting classes and libraries:
```
pip install -r requirements-python-lib.txt --target lib
```

### Unit test runs:
  * Replace **{Python_Project}** with the baseline path of the python program.

##### Unit testing:
```
cd {Python_Project}/git-lib
test/unit/git_class/unit_test_run.sh
```

##### Code coverage unit testing:
```
cd {Python_Project}/git-lib
test/unit/git_class/code_coverage.sh
```

