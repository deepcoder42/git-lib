#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_is_remote.py

    Description:  Unit testing of gitmerge.is_remote in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_is_remote.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import collections
import git

# Local
sys.path.append(os.getcwd())
import git_class
import version

__version__ = version.__version__


def ls_remote2(arg1):

    """Function:  ls_remote2

    Description:  Method stub holder for git.Repo.git.ls_remote().

    Arguments:

    """

    if arg1:
        raise git.exc.GitCommandError('git', 128)


def ls_remote(arg1):

    """Function:  ls_remote

    Description:  Method stub holder for git.Repo.git.ls_remote().

    Arguments:

    """

    if arg1:
        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_is_remote_false
        test_is_remote_true

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.repo_name = "Repo_name"
        self.git_dir = "/directory/git"
        self.url = "URL"
        self.branch = "Remote_branch"
        self.mod_branch = "Mod_branch"

        self.gitr = git_class.GitMerge(self.repo_name, self.git_dir, self.url,
                                       self.branch, self.mod_branch)

    def test_is_remote_false(self):

        """Function:  test_is_remote_false

        Description:  Test with exception raised from ls_remote call.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'ls_remote')
        self.gitr.gitcmd = giti(ls_remote2)

        self.assertFalse(self.gitr.is_remote())

    def test_is_remote_true(self):

        """Function:  test_is_remote_true

        Description:  Test with successful ls_remote call.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'ls_remote')
        self.gitr.gitcmd = giti(ls_remote)

        self.assertTrue(self.gitr.is_remote())


if __name__ == "__main__":
    unittest.main()
