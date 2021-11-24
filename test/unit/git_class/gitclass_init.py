#!/usr/bin/python
# Classification (U)

"""Program:  gitclass_init.py

    Description:  Unit testing of GitClass.__init__ in git_class.py.

    Usage:
        test/unit/git_class/gitclass_init.py

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
        test_repo_dir_set
        test_init_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.repo_dir = "/repo/directory"

    def test_repo_dir_set(self):

        """Function:  test_repo_dir_set

        Description:  Test with repo_dir being set.

        Arguments:

        """

        gitc = git_class.GitClass(self.repo_dir)

        self.assertEqual((gitc.gitrepo, gitc.gitcmd, gitc.repo_dir,
                          gitc.gitinit),
                         (None, None, self.repo_dir, None))

    def test_init_default(self):

        """Function:  test_init_default

        Description:  Test with default values set.

        Arguments:

        """

        gitc = git_class.GitClass()

        self.assertEqual((gitc.gitrepo, gitc.gitcmd, gitc.repo_dir,
                          gitc.gitinit),
                         (None, None, ".", None))


if __name__ == "__main__":
    unittest.main()
