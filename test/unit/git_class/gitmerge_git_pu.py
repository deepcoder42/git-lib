#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_git_pu.py

    Description:  Unit testing of gitmerge.git_pu in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_git_pu.py

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


def push3(option):

    """Function:  push3

    Description:  Method stub holder for git.Repo.git.push().

    Arguments:

    """

    status = 2

    if option:
        raise git.exc.GitCommandError("git", status, "stderr")

    else:
        raise git.exc.GitCommandError("git", 2, "stderr")


def push2(option):

    """Function:  push2

    Description:  Method stub holder for git.Repo.git.push().

    Arguments:

    """

    status = 128

    if option:
        raise git.exc.GitCommandError("git", status, "stderr")

    else:
        raise git.exc.GitCommandError("git", 128, "stderr")


def push(option):

    """Function:  push

    Description:  Method stub holder for git.Repo.git.push().

    Arguments:

    """

    if option:
        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_git_pu_tags
        test_git_pu_2
        test_git_pu_128
        test_git_pu_true

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

    def test_git_pu_tags(self):

        """Function:  test_git_pu_tags

        Description:  Test with passing tags option.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'push')
        self.gitr.gitcmd = giti(push)

        status, msg = self.gitr.git_pu(tags=True)
        self.assertEqual((status, msg), (True, {}))

    def test_git_pu_2(self):

        """Function:  test_git_pu_2

        Description:  Test with raised exception - 2 status.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'push')
        self.gitr.gitcmd = giti(push3)

        status, msg = self.gitr.git_pu()
        self.assertEqual((status, msg["status"]), (False, 2))

    def test_git_pu_128(self):

        """Function:  test_git_pu_128

        Description:  Test with raised exception - 128 status.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'push')
        self.gitr.gitcmd = giti(push2)

        status, msg = self.gitr.git_pu()
        self.assertEqual((status, msg["status"]), (False, 128))

    def test_git_pu_true(self):

        """Function:  test_git_pu_true

        Description:  Test with successful git_pu call.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'push')
        self.gitr.gitcmd = giti(push)

        status, msg = self.gitr.git_pu()
        self.assertEqual((status, msg), (True, {}))


if __name__ == "__main__":
    unittest.main()
