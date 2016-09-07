# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import zipfile
import os
import shortuuid
import shutil

from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from djangotrellostats.apps.repositories.forms import CommitForm, DeleteCommitForm, MakeAssessmentForm
from djangotrellostats.apps.repositories.models import Commit, PyLintMessage
from djangotrellostats.apps.repositories.pylinter import DirPylinter


@login_required
def add(request, board_id, repository_id):
    member = request.user.member
    try:
        board = member.boards.get(id=board_id)
        repository = board.repositories.get(id=repository_id)
    except ObjectDoesNotExist:
        raise Http404

    commit = Commit(board=board, repository=repository)

    if request.method == "POST":
        form = CommitForm(request.POST, request.FILES, instance=commit)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse("boards:repositories:view_repository", args=(board_id, repository_id)))

    else:
        form = CommitForm(instance=commit)

    replacements = {"form": form, "board": board, "member": member, "repository": repository}
    return render(request, "repositories/commits/add.html", replacements)


# Delete a commit
@login_required
def delete(request, board_id, repository_id, commit_id):
    member = request.user.member
    try:
        board = member.boards.get(id=board_id)
        repository = board.repositories.get(id=repository_id)
        commit = repository.commits.get(id=commit_id)
    except ObjectDoesNotExist:
        raise Http404

    if request.method == "POST":
        form = DeleteCommitForm(request.POST)

        if form.is_valid() and form.cleaned_data.get("confirmed"):
            commit.delete()
            return HttpResponseRedirect(reverse("boards:repositories:view_repository", args=(board_id, repository_id)))

    else:
        form = DeleteCommitForm()

    replacements = {"form": form, "board": board, "member": member, "repository": repository, "commit": commit}
    return render(request, "repositories/commits/delete.html", replacements)


# View assessment report
def view_assessment_report(request, board_id, repository_id, commit_id):
    member = request.user.member
    try:
        board = member.boards.get(id=board_id)
        repository = board.repositories.get(id=repository_id)
        commit = repository.commits.get(id=commit_id)
    except ObjectDoesNotExist:
        raise Http404

    pylint_messages = commit.pylint_messages.all()

    replacements = {
        "board": board, "member": member, "repository": repository, "commit": commit,
        "pylint_messages": pylint_messages
    }
    return render(request, "repositories/commits/assessment/view_report.html", replacements)


def assess_code_quality(request, board_id, repository_id, commit_id):
    member = request.user.member
    try:
        board = member.boards.get(id=board_id)
        repository = board.repositories.get(id=repository_id)
        commit = repository.commits.get(id=commit_id)
    except ObjectDoesNotExist:
        raise Http404

    if request.method == "POST":
        form = MakeAssessmentForm(request.POST)

        if form.is_valid() and form.cleaned_data.get("confirmed"):
            language = form.cleaned_data["language"]
            if language == "python":
                return _assess_python_code_quality(request, member, board, repository, commit)
            elif language == "php":
                return _assess_php_code_quality(request, member, board, repository, commit)
            else:
                raise Http404
    else:
        form = MakeAssessmentForm()

    replacements = {"form": form, "board": board, "member": member, "repository": repository, "commit": commit}
    return render(request, "repositories/commits/assessment/make_assessment.html", replacements)


# Assess quality of the PHP code of this commit
@transaction.atomic
def _assess_php_code_quality(request, member, board, repository, commit):
    pass


# Assess quality of the Python code of this commit
@transaction.atomic
def _assess_python_code_quality(request, member, board, repository, commit):

    code_file_path = settings.MEDIA_ROOT+"/"+commit.code.name
    output_file_path = u"/tmp/{0}-{1}".format(commit.commit, shortuuid.uuid())

    zip_ref = zipfile.ZipFile(code_file_path, 'r')
    zip_ref.extractall(output_file_path)
    zip_ref.close()

    dir_pylinter = DirPylinter(output_file_path)
    pylinter_results = dir_pylinter.run()
    PyLintMessage.create_all(commit, pylinter_results)

    shutil.rmtree(output_file_path, ignore_errors=True)

    replacements = {
        "board": board, "member": member, "repository": repository, "commit": commit, "pylinter_results": pylinter_results,
    }
    return render(request, "repositories/commits/assessment/python/assess_code.html", replacements)
