#!/usr/bin/python
# Classification (U)

"""Program:  gitconfig_get_user.py

    Description:  Unit testing of gitconfig.get_user in git_class.py.

    Usage:
        test/unit/git_class/gitconfig_get_user.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import shutil

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
        test_get_user
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.user = "user_name"
        self.repo_dir = "test/unit/git_class/test/test-repo"
        gita = git_class.GitConfig(self.repo_dir)
        gita.writer.set_value("user", "name", self.user).release()

        self.gitr = git_class.GitConfig(self.repo_dir)

    def test_get_user(self):

        """Function:  test_get_user

        Description:  Test get_user method.

        Arguments:

        """

        self.assertEqual(self.gitr.get_user(), self.user)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isdir(self.repo_dir):
            shutil.rmtree(self.repo_dir)


if __name__ == "__main__":
    unittest.main()
