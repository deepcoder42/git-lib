#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_git_co.py

    Description:  Unit testing of gitmerge.git_co in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_git_co.py

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


def checkout2(branch):

    """Function:  checkout

    Description:  Method stub holder for git.Repo.git.checkout().

    Arguments:

    """

    if branch:
        raise git.exc.GitCommandError("git", 128, "stderr")


def checkout(branch):

    """Function:  checkout

    Description:  Method stub holder for git.Repo.git.checkout().

    Arguments:

    """

    if branch:
        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_git_co_branch
        test_git_co_exception
        test_git_co_true

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

    def test_git_co_branch(self):

        """Function:  test_git_co_branch

        Description:  Test with branch parameter passed.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'checkout')
        self.gitr.gitcmd = giti(checkout)

        status, msg = self.gitr.git_co(branch="New_Branch")
        self.assertEqual((status, msg), (True, {}))

    def test_git_co_exception(self):

        """Function:  test_git_co_exception

        Description:  Test with raised exception.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'checkout')
        self.gitr.gitcmd = giti(checkout2)

        status, msg = self.gitr.git_co()
        self.assertEqual((status, msg["status"]), (False, 128))

    def test_git_co_true(self):

        """Function:  test_git_co_true

        Description:  Test with successful branch call.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'checkout')
        self.gitr.gitcmd = giti(checkout)

        status, msg = self.gitr.git_co()
        self.assertEqual((status, msg), (True, {}))


if __name__ == "__main__":
    unittest.main()
