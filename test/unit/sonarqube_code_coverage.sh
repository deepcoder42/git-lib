#!/bin/bash
# Unit test code coverage for SonarQube to cover all modules.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=git_class test/unit/git_class/gitmerge_init.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_detach_head.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_get_br_name.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_remove_branch.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_create_gitrepo.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_set_remote.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_is_remote.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_process_dirty.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_process_untracked.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_is_dirty.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_is_untracked.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_git_fetch.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_rename_br.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_git_co.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_priority_merge.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_git_pu.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_commits_diff.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_is_commits_ahead.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_is_commits_behind.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_is_remote_branch.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_get_dirty.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_get_untracked.py
coverage run -a --source=git_class test/unit/git_class/gitclass_init.py
coverage run -a --source=git_class test/unit/git_class/gitclass_create_repo.py
coverage run -a --source=git_class test/unit/git_class/gitclass_create_init.py
coverage run -a --source=git_class test/unit/git_class/gitclass_create_cmd.py
coverage run -a --source=git_class test/unit/git_class/gitconfig_init.py
coverage run -a --source=git_class test/unit/git_class/gitconfig_get_email.py
coverage run -a --source=git_class test/unit/git_class/gitconfig_get_user.py
coverage run -a --source=git_class test/unit/git_class/gitconfig_set_email.py
coverage run -a --source=git_class test/unit/git_class/gitconfig_set_user.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
coverage xml -i

