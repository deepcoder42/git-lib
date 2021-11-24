#!/usr/bin/python
# Classification (U)

"""Program:  gitconfig_set_email.py

    Description:  Unit testing of gitconfig.set_email in git_class.py.

    Usage:
        test/unit/git_class/gitconfig_set_email.py

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
        test_set_email
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.email = "email_name@domain.name"
        self.repo_dir = "test/unit/git_class/test/test-repo"
        self.gitr = git_class.GitConfig(self.repo_dir)

    def test_set_email(self):

        """Function:  test_set_email

        Description:  Test set_email method.

        Arguments:

        """

        self.gitr.set_email(self.email)
        gita = git_class.GitConfig(self.repo_dir)

        self.assertEqual(gita.get_email(), self.email)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isdir(self.repo_dir):
            shutil.rmtree(self.repo_dir)


if __name__ == "__main__":
    unittest.main()
