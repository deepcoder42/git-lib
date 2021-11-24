#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_process_untracked.py

    Description:  Unit testing of gitmerge.process_untracked in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_process_untracked.py

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
import mock

# Local
sys.path.append(os.getcwd())
import git_class
import version

__version__ = version.__version__


class Index(object):

    """Class:  Index

    Description:  Class stub holder for git.gitrepo.index.

    Methods:
        __init

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialization of class instance.

        Arguments:

        """

        pass


class Diff(Index):

    """Class:  Diff

    Description:  Class stub holder for git.gitrepo.index.diff.

    Methods:
        __init
        add
        commit

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialization of class instance.

        Arguments:

        """

        super(Diff, self).__init__()
        self.new_files = None
        self.msg = None

    def add(self, new_files):

        """Method:  add

        Description:  Method stub holder for git.gitrepo.index.add().

        Arguments:

        """

        self.new_files = new_files

        return True

    def commit(self, msg):

        """Method:  commit

        Description:  Method stub holder for git.gitrepo.index.commit().

        Arguments:

        """

        self.msg = msg

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_process_remove_dir
        test_process_add_option
        test_process_remove_option
        test_process_newfiles_list
        test_process_empty_list2
        test_process_empty_list

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
        self.git_set_data = "index untracked_files"

        self.gitr = git_class.GitMerge(self.repo_name, self.git_dir, self.url,
                                       self.branch, self.mod_branch)

        self.new_list1 = []
        self.new_list2 = ["file1"]

    @mock.patch("git_class.os")
    @mock.patch("git_class.shutil")
    def test_process_remove_dir(self, mock_shutil, mock_os):

        """Function:  test_process_remove_dir

        Description:  Test with removal of directory.

        Arguments:

        """

        mock_shutil.rmtree.return_value = True
        mock_os.path.isdir.return_value = True

        giti = collections.namedtuple('GIT', self.git_set_data)
        diff = Diff()
        self.gitr.gitrepo = giti(diff, self.new_list1)
        self.gitr.new_files = self.new_list2

        self.gitr.process_untracked("remove")

        self.assertEqual(self.gitr.new_files, self.new_list2)

    @mock.patch("git_class.os")
    @mock.patch("git_class.gen_libs")
    def test_process_add_option(self, mock_lib, mock_os):

        """Function:  test_process_add_option

        Description:  Test with add option passed.

        Arguments:

        """

        mock_lib.rm_file.return_value = True
        mock_os.path.isdir.return_value = False

        giti = collections.namedtuple('GIT', self.git_set_data)
        diff = Diff()
        self.gitr.gitrepo = giti(diff, self.new_list1)
        self.gitr.new_files = self.new_list2

        self.gitr.process_untracked("add")

        self.assertEqual(self.gitr.new_files, self.new_list2)

    @mock.patch("git_class.os")
    @mock.patch("git_class.gen_libs")
    def test_process_remove_option(self, mock_lib, mock_os):

        """Function:  test_process_remove_option

        Description:  Test with remove option passed.

        Arguments:

        """

        mock_lib.rm_file.return_value = True
        mock_os.path.isdir.return_value = False

        giti = collections.namedtuple('GIT', self.git_set_data)
        diff = Diff()
        self.gitr.gitrepo = giti(diff, self.new_list1)
        self.gitr.new_files = self.new_list2

        self.gitr.process_untracked("remove")

        self.assertEqual(self.gitr.new_files, self.new_list2)

    @mock.patch("git_class.os")
    @mock.patch("git_class.gen_libs")
    def test_process_newfiles_list(self, mock_lib, mock_os):

        """Function:  test_process_newfiles_list

        Description:  Test with new_files list set.

        Arguments:

        """

        mock_lib.rm_file.return_value = True
        mock_os.path.isdir.return_value = False

        giti = collections.namedtuple('GIT', self.git_set_data)
        diff = Diff()
        self.gitr.gitrepo = giti(diff, self.new_list1)
        self.gitr.new_files = self.new_list2

        self.gitr.process_untracked()

        self.assertEqual(self.gitr.new_files, self.new_list2)

    @mock.patch("git_class.os")
    @mock.patch("git_class.gen_libs")
    def test_process_empty_list2(self, mock_lib, mock_os):

        """Function:  test_process_empty_list2

        Description:  Test with empty list passed.

        Arguments:

        """

        mock_lib.rm_file.return_value = True
        mock_os.path.isdir.return_value = False

        giti = collections.namedtuple('GIT', self.git_set_data)
        diff = Diff()
        self.gitr.gitrepo = giti(diff, self.new_list2)

        self.gitr.process_untracked()

        self.assertEqual(self.gitr.new_files, self.new_list2)

    def test_process_empty_list(self):

        """Function:  test_process_empty_list

        Description:  Test with empty list passed.

        Arguments:

        """

        giti = collections.namedtuple('GIT', self.git_set_data)
        diff = Diff()
        self.gitr.gitrepo = giti(diff, self.new_list1)

        self.gitr.process_untracked()

        self.assertEqual(self.gitr.new_files, self.new_list1)


if __name__ == "__main__":
    unittest.main()
