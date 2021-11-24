#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_git_fetch.py

    Description:  Unit testing of gitmerge.git_fetch in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_git_fetch.py

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


def fetch3():

    """Function:  fetch3

    Description:  Method stub holder for git.Repo.git.fetch().

    Arguments:

    """

    raise git.exc.GitCommandError("git", 2, "stderr")


def fetch2():

    """Function:  fetch2

    Description:  Method stub holder for git.Repo.git.fetch().

    Arguments:

    """

    raise git.exc.GitCommandError("git", 128, "stderr")


def fetch():

    """Function:  fetch

    Description:  Method stub holder for git.Repo.git.fetch().

    Arguments:

    """

    pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_git_fetch_2
        test_git_fetch_128
        test_git_fetch_true

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

    def test_git_fetch_2(self):

        """Function:  test_git_fetch_2

        Description:  Test with raised exception - 2 status.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'fetch')
        self.gitr.gitcmd = giti(fetch3)

        status, msg = self.gitr.git_fetch()
        self.assertEqual((status, msg["status"]), (False, 2))

    def test_git_fetch_128(self):

        """Function:  test_git_fetch_128

        Description:  Test with raised exception - 128 status.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'fetch')
        self.gitr.gitcmd = giti(fetch2)

        status, msg = self.gitr.git_fetch()
        self.assertEqual((status, msg["status"]), (False, 128))

    def test_git_fetch_true(self):

        """Function:  test_git_fetch_true

        Description:  Test with successful git_fetch call.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'fetch')
        self.gitr.gitcmd = giti(fetch)

        status, msg = self.gitr.git_fetch()
        self.assertEqual((status, msg), (True, {}))


if __name__ == "__main__":
    unittest.main()
