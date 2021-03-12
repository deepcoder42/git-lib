#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_priority_merge.py

    Description:  Unit testing of gitmerge.priority_merge in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_priority_merge.py

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
import mock
import git
import collections

# Local
sys.path.append(os.getcwd())
import git_class
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


def merge2(arg_list):

    """Function:  merge

    Description:  Method stub holder for git.Repo.git.merge().

    Arguments:
        (input) arg_list -> List of arguments for merge command.

    """

    if arg_list:
         raise git.exc.GitCommandError("git", 128, "stderr")


def merge(arg_list):

    """Function:  merge

    Description:  Method stub holder for git.Repo.git.merge().

    Arguments:
        (input) arg_list -> List of arguments for merge command.

    """

    status = True

    if arg_list:
        status = True

    return status


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_allow_branch_options - Test with allow and branch parameters.
        test_allow_option -> Test with allow parameter passed.
        test_priority_merge_branch -> Test with branch parameter passed.
        test_priority_merge_exception -> Test with raised exception.
        test_priority_merge_true -> Test with successful checkout call.

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

    def test_allow_branch_options(self):

        """Function:  test_allow_branch_options

        Description:  Test with allow and branch parameters.

        Arguments:

        """

        GIT = collections.namedtuple('GIT', 'merge')
        self.gitr.gitcmd = GIT(merge)

        status, msg = self.gitr.priority_merge(ranch="New_Branch", allow=True)
        self.assertEqual((status, msg), (True, {}))

    def test_allow_option(self):

        """Function:  test_allow_option

        Description:  Test with allow parameter passed.

        Arguments:

        """

        GIT = collections.namedtuple('GIT', 'merge')
        self.gitr.gitcmd = GIT(merge)

        status, msg = self.gitr.priority_merge(allow=True)
        self.assertEqual((status, msg), (True, {}))

    def test_priority_merge_branch(self):

        """Function:  test_priority_merge_branch

        Description:  Test with branch parameter passed.

        Arguments:

        """

        GIT = collections.namedtuple('GIT', 'merge')
        self.gitr.gitcmd = GIT(merge)

        status, msg = self.gitr.priority_merge(branch="New_Branch")
        self.assertEqual((status, msg), (True, {}))

    def test_priority_merge_exception(self):

        """Function:  test_priority_merge_exception

        Description:  Test with raised exception.

        Arguments:

        """

        GIT = collections.namedtuple('GIT', 'merge')
        self.gitr.gitcmd = GIT(merge2)

        status, msg = self.gitr.priority_merge()
        self.assertEqual((status, msg["status"]), (False, 128))

    def test_priority_merge_true(self):

        """Function:  test_priority_merge_true

        Description:  Test with successful branch call.

        Arguments:

        """

        GIT = collections.namedtuple('GIT', 'merge')
        self.gitr.gitcmd = GIT(merge)

        status, msg = self.gitr.priority_merge()
        self.assertEqual((status, msg), (True, {}))


if __name__ == "__main__":
    unittest.main()
