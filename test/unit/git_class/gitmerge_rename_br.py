#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_rename_br.py

    Description:  Unit testing of gitmerge.rename_br in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_rename_br.py

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


def branch2(brch):

    """Function:  fetch2

    Description:  Method stub holder for git.Repo.git.branch().

    Arguments:

    """

    if brch:
        raise git.exc.GitCommandError("git", 128, "stderr")


def branch(brch):

    """Function:  fetch

    Description:  Method stub holder for git.Repo.git.branch().

    Arguments:

    """

    if brch:
        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_rename_br_branch
        test_rename_br_exception
        test_rename_br_true

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

    def test_rename_br_branch(self):

        """Function:  test_rename_br_branch

        Description:  Test with branch parameter passed.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'branch')
        self.gitr.gitcmd = giti(branch)

        status, msg = self.gitr.rename_br(branch="New_Branch")
        self.assertEqual((status, msg), (True, {}))

    def test_rename_br_exception(self):

        """Function:  test_rename_br_exception

        Description:  Test with raised exception.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'branch')
        self.gitr.gitcmd = giti(branch2)

        status, msg = self.gitr.rename_br()
        self.assertEqual((status, msg["status"]), (False, 128))

    def test_rename_br_true(self):

        """Function:  test_rename_br_true

        Description:  Test with successful branch call.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'branch')
        self.gitr.gitcmd = giti(branch)

        status, msg = self.gitr.rename_br()
        self.assertEqual((status, msg), (True, {}))


if __name__ == "__main__":
    unittest.main()
