#!/bin/bash
# Unit testing program for the git_class.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit test:  git_class.py"
test/unit/git_class/gitmerge_init.py
test/unit/git_class/gitmerge_detach_head.py
test/unit/git_class/gitmerge_get_br_name.py
test/unit/git_class/gitmerge_remove_branch.py
test/unit/git_class/gitmerge_create_gitrepo.py
test/unit/git_class/gitmerge_set_remote.py
test/unit/git_class/gitmerge_is_remote.py
test/unit/git_class/gitmerge_process_dirty.py
test/unit/git_class/gitmerge_process_untracked.py
test/unit/git_class/gitmerge_is_dirty.py
test/unit/git_class/gitmerge_is_untracked.py
test/unit/git_class/gitmerge_git_fetch.py
test/unit/git_class/gitmerge_rename_br.py
test/unit/git_class/gitmerge_git_co.py
test/unit/git_class/gitmerge_priority_merge.py
test/unit/git_class/gitmerge_git_pu.py
test/unit/git_class/gitmerge_commits_diff.py
test/unit/git_class/gitmerge_is_commits_ahead.py
test/unit/git_class/gitmerge_is_commits_behind.py
test/unit/git_class/gitmerge_is_remote_branch.py
test/unit/git_class/gitmerge_get_dirty.py
test/unit/git_class/gitmerge_get_untracked.py
test/unit/git_class/gitclass_init.py
test/unit/git_class/gitclass_create_repo.py
test/unit/git_class/gitclass_create_init.py
test/unit/git_class/gitclass_create_cmd.py
test/unit/git_class/gitconfig_init.py
test/unit/git_class/gitconfig_get_email.py
test/unit/git_class/gitconfig_get_user.py
test/unit/git_class/gitconfig_set_email.py
test/unit/git_class/gitconfig_set_user.py

