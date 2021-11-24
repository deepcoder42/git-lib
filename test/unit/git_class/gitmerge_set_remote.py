#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_set_remote.py

    Description:  Unit testing of gitmerge.set_remote in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_set_remote.py

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

# Local
sys.path.append(os.getcwd())
import git_class
import version

__version__ = version.__version__


def remote(arg1, arg2, arg3):

    """Function:  remote

    Description:  Method stub holder for git.Repo.git.remote().

    Arguments:

    """

    if arg1 and arg2 and arg3:
        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_set_remote

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

    def test_set_remote(self):

        """Function:  test_set_remote

        Description:  Test with default values settings.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'remote')
        self.gitr.gitcmd = giti(remote)

        self.assertFalse(self.gitr.set_remote())


if __name__ == "__main__":
    unittest.main()
