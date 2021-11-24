#!/usr/bin/python
# Classification (U)

"""Program:  gitclass_create_init.py

    Description:  Unit testing of GitClass.create_init in git_class.py.

    Usage:
        test/unit/git_class/gitclass_create_init.py

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

# Local
sys.path.append(os.getcwd())
import git_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_default_arg
        test_repodir_arg

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.gitc = git_class.GitClass()
        self.repo_dir = "/directory/git"
        self.git_class = "Git Init Class Instance"
        self.results = "Git Init Class Instance"

    @mock.patch("git_class.git")
    def test_repodir_arg(self, mock_git):

        """Function:  test_repodir_arg

        Description:  Test with passing repo_dir argument.

        Arguments:

        """

        mock_git.Repo.init.return_value = self.git_class
        self.gitc.create_init(self.repo_dir)

        self.assertEqual((self.gitc.gitrepo, self.gitc.gitcmd,
                          self.gitc.repo_dir, self.gitc.gitinit),
                         (None, None, self.repo_dir, self.results))

    @mock.patch("git_class.git")
    def test_default_arg(self, mock_git):

        """Function:  test_default_arg

        Description:  Test with using default arguments.

        Arguments:

        """

        mock_git.Repo.init.return_value = self.git_class
        self.gitc.create_init()

        self.assertEqual((self.gitc.gitrepo, self.gitc.gitcmd,
                          self.gitc.repo_dir, self.gitc.gitinit),
                         (None, None, ".", self.results))


if __name__ == "__main__":
    unittest.main()
