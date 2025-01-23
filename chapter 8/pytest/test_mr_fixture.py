import pytest
from mr_parametrized import MergeRequest, MergeRequestExtendedStatus

@pytest.fixture
def rejected_mr():
    merge_request = MergeRequest()

    merge_request.downvote('dev1')
    merge_request.upvote('dev2')
    merge_request.downvote('dev3')
    merge_request.downvote('dev4')

    return merge_request


def test_simple_rejected(rejected_mr):
    assert rejected_mr.status == MergeRequestExtendedStatus.REJECTED

def test_rejected_with_approvals(rejected_mr):
    rejected_mr.upvote('dev2')
    rejected_mr.upvote('dev3')
    assert rejected_mr.status == MergeRequestExtendedStatus.REJECTED

def test_rejected_to_pending(rejected_mr):
    rejected_mr.upvote('dev1')
    assert rejected_mr.status == MergeRequestExtendedStatus.PENDING

def test_rejected_to_approved(rejected_mr):
    rejected_mr.upvote('dev1')
    rejected_mr.upvote('dev3')
    rejected_mr.upvote('dev4')
    assert rejected_mr.status == MergeRequestExtendedStatus.APPROVED