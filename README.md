# Python project that contains libraries and classes for Git repository use.
# Classification (U)

# Description:
  This project is used to interact with local and remote Git repositories and have capbility to merge repositories.  It contains classes and libraries for both local and remote Git repositories.

###  This README file is broken down into the following sections:
  * Prerequisites
    - Pip Installation
  * Installation
  * Testing
    - Unit


# Prerequisites:

  * List of Linux packages that need to be installed on the server:
    - git
    - python-pip

  * Local class/library dependencies within the program structure:
    - python-lib


# Installation:
  * From here on out, any reference to **{Python_Project}** or **PYTHON_PROJECT** replace with the baseline path of the python program.
  * Replace any reference to **{Other_Python_Project}** with the baseline path of another python program.
  * There are two types of installs: pip and git.

### Pip Installation:

##### Create requirements file in another program's project to install git-lib as a library module.

Create requirements-git-lib.txt file and requirements-python-lib.txt files:

```
cd {Python_Project}
cp requirements-git-lib.txt {Other_Python_Project}/requirements-git-lib.txt
cp requirements-python-lib.txt {Other_Python_Project}/requirements-python-lib.txt
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.

Modify the {Other_Python_Project}/README.md file:

```
pip install -r requirements-git-lib.txt --target git_lib --system
pip install -r requirements-python-lib.txt --target git_lib/lib --system
```

##### Add the general Git-lib requirements to the other program's requirements.txt file.  Remove any duplicates.

Add/modify the following lines to the {Other_Python_Project}/requirements.txt file:

```
gitdb2==2.0.4
GitPython==2.1.8
smmap2==2.0.4
```

### Git Installation:

Install general Git-lib libraries and classes using git.

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
pip install -r requirements.txt --upgrade --system
exit
```

Install supporting classes and libraries:

```
pip install -r requirements-python-lib.txt --target lib --system
```


# Testing:

# Unit Testing:

### Installation:

Install the project using the procedures in the Git Installation section.

### Testing:

```
cd {Python_Project}/git-lib
test/unit/git_class/unit_test_run.sh
```

### Code Coverage:

```
cd {Python_Project}/git-lib
test/unit/git_class/code_coverage.sh
```

