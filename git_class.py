# Classification (U)

"""Program:  git_class.py

    Description:  Class that has class definitions and methods for connecting
        to and using local and remote git repositories.

    Classes:
        GitClass
            GitMerge
            GitConfig

"""

# Libraries and Global Variables

# Standard
import os
import time
import shutil

# Third-party
import git

# Local
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class GitClass(object):

    """Class:  GitClass

    Description:  Class that initializes and sets up instances to the Python
        git repository and git command line instances.

    Methods:
        __init__
        create_repo
        create_cmd
        create_init

    """

    def __init__(self, repo_dir="."):

        """Method:  __init__

        Description:  Initialization of an instance of the GitClass class.

        Arguments:
            repo_dir -> Git repository path name.

        """

        self.gitrepo = None
        self.gitcmd = None
        self.gitinit = None
        self.repo_dir = repo_dir

    def create_repo(self, repo_dir=None):

        """Method:  create_repo

        Description:  Create a git instance to an existing local git
            repository.

        Arguments:
            repo_dir -> Git repository path name.

        """

        if repo_dir:
            self.repo_dir = repo_dir

        self.gitrepo = git.Repo(self.repo_dir)

    def create_cmd(self):

        """Method:  create_cmd

        Description:  Create a git command line instance.

        Note:  An existing git instance must already been initialized.

        Arguments:

        """

        if self.gitrepo:
            self.gitcmd = self.gitrepo.git

    def create_init(self, repo_dir=None):

        """Method:  create_init

        Description:  Create an instance to an existing git repository or
            creates a new git repository and directory if the repository
            directory does not exist.

        Arguments:
            repo_dir -> Git repository path name.

        """

        if repo_dir:
            self.repo_dir = repo_dir

        self.gitinit = git.Repo.init(self.repo_dir)


class GitMerge(GitClass):

    """Class:  GitMerge

    Description:  Class that handles operations of merging a non-local git
        repository with a remote git repository.

    Methods:
        __init__
        create_gitrepo
        set_remote
        is_remote
        process_dirty
        process_untracked
        get_dirty
        get_untracked
        is_dirty
        is_untracked
        git_fetch
        rename_br
        git_co
        priority_merge
        git_pu
        commits_diff
        is_commits_ahead
        is_commits_behind
        is_remote_branch
        detach_head
        get_br_name
        remove_branch

    """

    def __init__(self, repo_name, git_dir, url, branch, mod_branch):

        """Method:  __init__

        Description:  Initialization of an instance of the GitMerge class.

        Arguments:
            repo_name -> Name of git repository.
            git_dir -> Directory path to the local git repository.
            url -> URL to the remote git repository.
            branch -> Name of branch at remote to be merged with.
            mod_branch -> Name of temporary branch to be merged into remote.

        """

        self.git_dir = git_dir

        super(GitMerge, self).__init__(self.git_dir)

        self.repo_name = repo_name
        self.url = url
        self.mod_branch = mod_branch
        self.branch = branch
        self.remote_info = None
        self.br_commit = None
        self.rm_files = []
        self.chg_files = []
        self.new_files = []

    def create_gitrepo(self):

        """Method:  create_gitrepo

        Description:  Creates git repo and git command line instances.

        Arguments:

        """

        super(GitMerge, self).create_repo()
        super(GitMerge, self).create_cmd()

    def set_remote(self):

        """Method:  set_remote

        Description:  Sets the url to the origin to a remote git repository.

        Arguments:

        """

        self.gitcmd.remote("set-url", "origin", self.url)

    def is_remote(self):

        """Method:  is_remote

        Description:  Checks to see if remote git repository exists.

        Arguments:
            (output) True|False -> Is URL a remote git repository.

        """

        try:
            self.remote_info = self.gitcmd.ls_remote(self.url)
            return True

        except git.exc.GitCommandError:
            return False

    def process_dirty(self, option="revert"):

        """Function:  process_dirty

        Description:  Process any dirty files.

        Arguments:
            (input) option -> revert|commit - options for the changes.

        """

        # Process deleted files.
        if not self.rm_files:
            self.rm_files = [item.a_path
                             for item in self.gitrepo.index.diff(None)
                             if item.change_type == "D"]

        if self.rm_files:
            if option == "revert":
                self.gitrepo.index.checkout(self.rm_files, force=True)

            elif option == "commit":
                self.gitrepo.index.remove(self.rm_files, working_tree=True)
                self.gitrepo.index.commit("Commit removed files")

        # Process modified files.
        if not self.chg_files:
            self.chg_files = [item.a_path
                              for item in self.gitrepo.index.diff(None)
                              if item.change_type == "M"]

        if self.chg_files:
            if option == "revert":
                self.gitrepo.index.checkout(self.chg_files, force=True)

            elif option == "commit":
                self.gitrepo.index.add(self.chg_files)
                self.gitrepo.index.commit("Commit modified files")

    def process_untracked(self, option="remove"):

        """Function:  process_untracked

        Description:  Process any untracked (new) files.

        Arguments:
            (input) option -> add|remove - Options allowed for untracked files.

        """

        if not self.new_files:
            self.new_files = self.gitrepo.untracked_files

        if self.new_files:
            if option == "add":
                self.gitrepo.index.add(self.new_files)
                self.gitrepo.index.commit("Add new files")

            elif option == "remove":
                for f_name in self.new_files:

                    if os.path.isdir(os.path.join(self.git_dir, f_name)):
                        shutil.rmtree(os.path.join(self.git_dir, f_name))

                    else:
                        gen_libs.rm_file(os.path.join(self.git_dir, f_name))

    def get_dirty(self):

        """Function:  get_dirty

        Description:  Find any dirty (i.e. removed or modified) files and
            update appropriate attributes.

        Arguments:

        """

        # Deleted files.
        self.rm_files = [item.a_path for item in self.gitrepo.index.diff(None)
                         if item.change_type == "D"]

        # Modified files.
        self.chg_files = [item.a_path for item in self.gitrepo.index.diff(None)
                          if item.change_type == "M"]

    def get_untracked(self):

        """Function:  get_untracked

        Description:  Find any untracked (i.e. new) files and update
            appropriate attribute.

        Arguments:

        """

        self.new_files = self.gitrepo.untracked_files

    def is_dirty(self):

        """Function:  is_dirty

        Description:  Check to see if there is any dirty objects.

        Arguments:
            (output) True|False -> If dirty objects detected.

        """

        return self.gitrepo.is_dirty()

    def is_untracked(self):

        """Function:  is_untracked

        Description:  Check to see if there is any new objects not tracked.

        Arguments:
            (output) True|False -> If untracked objects detected.

        """

        return self.gitrepo.is_dirty(untracked_files=True)

    def git_fetch(self, cnt=0):

        """Function:  git_fetch

        Description:  Fetch from the remote Git repository the master branch.

        Arguments:
            (input) cnt -> Number of recursive calls on method.
            (output) status -> True|False - Success of command.
            (output) msg -> Dictionary of return error code.

        """

        status = True
        msg = {}

        try:
            self.gitcmd.fetch()

        except git.exc.GitCommandError as (code):
            if code.status == 128 and cnt < 5:
                time.sleep(5)
                cnt += 1
                status, msg = self.git_fetch(cnt)

            else:
                status = False
                msg["status"] = code.status
                msg["stderr"] = code.stderr
                msg["command"] = code.command

        return status, msg

    def rename_br(self, branch=None):

        """Function:  rename_br

        Description:  Rename the current branch to a new name.

        Arguments:
            (input) branch -> Name of new branch.
            (output) status -> True|False - Success of command.
            (output) msg -> Dictionary of return error code.

        """

        status = True
        msg = {}

        if not branch:
            branch = self.mod_branch

        try:
            self.gitcmd.branch(branch)

        except git.exc.GitCommandError as (code):
            status = False
            msg["status"] = code.status
            msg["stderr"] = code.stderr
            msg["command"] = code.command

        return status, msg

    def git_co(self, branch=None):

        """Function:  git_co

        Description:  Git checkout to another branch.

        Arguments:
            (input) branch -> Name of branch to checkout.
            (output) status -> True|False - Success of command.
            (output) msg -> Dictionary of return error code.

        """

        status = True
        msg = {}

        if not branch:
            branch = self.branch

        try:
            self.gitcmd.checkout(branch)

        except git.exc.GitCommandError as (code):
            status = False
            msg["status"] = code.status
            msg["stderr"] = code.stderr
            msg["command"] = code.command

        return status, msg

    def priority_merge(self, branch=None, **kwargs):

        """Function:  priority_merge

        Description:  Merge of a new branch with an existing branch, with
            the priority on the new branch.

        Arguments:
            (input) branch -> Name of branch to merge with current branch.
            (input) **kwargs:
                allow -> True|False - Allow merge of unrelated histories.
            (output) status -> True|False - Success of command.
            (output) msg -> Dictionary of return error code.

        """

        status = True
        msg = {}

        if not branch:
            branch = self.mod_branch

        arg_list = ["--no-ff", "-s", "recursive", "-X", "theirs", branch]

        if kwargs.get("allow", False):
            arg_list.append("--allow-unrelated-histories")

        try:
            self.gitcmd.merge(arg_list)

        except git.exc.GitCommandError as (code):
            status = False
            msg["status"] = code.status
            msg["stdout"] = code.stdout
            msg["command"] = code.command
            msg["stderr"] = code.stderr

        return status, msg

    def git_pu(self, cnt=0, tags=False):

        """Function:  git_pu

        Description:  Git push to remote respository.

        Arguments:
            (input) cnt -> Number of recursive calls on method.
            (input) tags -> True|False - Push tags instead.
            (output) status -> True|False - Success of command.
            (output) msg -> Dictionary of return error code.

        """

        status = True
        msg = {}
        option = None

        if tags:
            option = "--tags"

        try:
            self.gitcmd.push(option)

        except git.exc.GitCommandError as (code):
            if code.status == 128 and cnt < 5:
                time.sleep(5)
                cnt += 1
                status, msg = self.git_pu(cnt)

            else:
                status = False
                msg["status"] = code.status
                msg["stderr"] = code.stderr
                msg["command"] = code.command

        return status, msg

    def commits_diff(self, data_str):

        """Function:  commits_diff

        Description:  Compares a branch with another branch and returns a count
            on the number of commits difference between the two branches.
                0 -> Branch not ahead of other branch.
                >0 ->  Branch is ahead of other branch by N commits.

        Note:
            The data_str will contain the order of the branches being compared,
                whether local to remote or remote to local.
            The format of the data_str is:
                Local to Remote:
                    "BRANCH_NAME..origin/BRANCH_NAME"
                Remote to Local:
                    "origin/BRANCH_NAME..BRANCH_NAME"

        Arguments:
            (input) data_str -> Contains the order of branches to be compared.
            (output) -> N commits difference between branches.

        """

        return sum(1 for _ in self.gitrepo.iter_commits(data_str))

    def is_commits_ahead(self, branch):

        """Function:  is_commits_ahead

        Description:  Compares the local branch with the remote branch and
            returns a count on whether local branch is ahead of remote branch.
            Output:
                0 -> Local branch not ahead of remote branch.
                >0 ->  Local branch is ahead of remote branch by N commits.

        Arguments:
            (input) branch -> Branch being compared.
            (output) -> N commits local branch ahead of remote branch.

        """

        return self.commits_diff("origin/" + branch + ".." + branch)

    def is_commits_behind(self, branch):

        """Function:  is_commits_behind

        Description:  Compares the local branch with the remote branch and
            returns a count on whether local branch is behind remote branch.
            Output:
                0 -> Local branch not behind remote branch.
                >0 ->  Local branch is behind remote branch by N commits.

        Arguments:
            (input) branch -> Branch being compares.
            (output) -> N commits local branch behind remote branch.

        """

        return self.commits_diff(branch + "..origin/" + branch)

    def is_remote_branch(self, branch):

        """Function:  is_remote_branch

        Description:  Determines if the branch exist in remote git repository.

        Arguments:
            (input) branch -> Branch name.
            (output) True|False -> The branch is in the remote git repo.

        """

        try:
            self.br_commit = self.gitcmd.rev_parse("--verify", branch)
            return True

        except git.exc.GitCommandError:
            return False

    def detach_head(self):

        """Function:  detach_head

        Description:  Checkouts the head to the latest commit ID.  This is to
            allow the head to become deatched.

        Arguments:

        """

        self.gitcmd.checkout(str(self.gitrepo.active_branch.commit.hexsha))

    def get_br_name(self):

        """Function:  get_br_name

        Description:  Return the current branch name.

        Arguments:
            (output) Current branch name.

        """

        return self.gitrepo.active_branch.name

    def remove_branch(self, branch, no_chk=False):

        """Function:  remove_branch

        Description:  Remove branch name passed to method.

        Arguments:
            (input) branch -> Branch name.
            (input) no_chk -> True|False - Suspend checking if current branch.
            (output) status -> True|False - Status of remove command.
            (output) msg -> Error messages, if any.

        """

        status = True
        msg = None

        if no_chk or branch != self.get_br_name():
            self.gitrepo.delete_head(branch)

        else:
            status = False
            msg = "WARNING: Cannot remove branch if current branch."

        return status, msg


class GitConfig(GitClass):

    """Class:  GitConfig

    Description:  Class that handles configuration of the local git repository.

    Methods:
        __init__
        get_email
        get_user
        set_email
        set_user

    """

    def __init__(self, repo_dir):

        """Method:  __init__

        Description:  Initialization of an instance of the GitConfig class.
            Create a git.Repo.init instance to an existing git repository or
            creates a new git repository if one does not exist.  Initializes
            Config reader and writer instances.

        Arguments:
            repo_dir -> Directory path to a local git repo.

        """

        super(GitConfig, self).__init__(repo_dir)

        self.gitinit = git.Repo.init(self.repo_dir)
        self.reader = self.gitinit.config_reader()
        self.writer = self.gitinit.config_writer()

    def get_email(self):

        """Function:  get_email

        Description:  Return the email address bound to the git repository.

        Arguments:
            (output) Email address.

        """

        return self.reader.get_value("user", "email")

    def get_user(self):

        """Function:  get_user

        Description:  Return the user name bound to the git repository.

        Arguments:
            (output) User name.

        """

        return self.reader.get_value("user", "name")

    def set_email(self, email):

        """Function:  set_email

        Description:  Set the email address for the local git repository.

        Arguments:
            (input) email -> Email address to be bound to local git repo.

        """

        return self.writer.set_value("user", "email", email).release()

    def set_user(self, name):

        """Function:  set_user

        Description:  Set the user name for the local git repository.

        Arguments:
            (input) name -> User name to be bound to local git repo.

        """

        return self.writer.set_value("user", "name", name).release()
