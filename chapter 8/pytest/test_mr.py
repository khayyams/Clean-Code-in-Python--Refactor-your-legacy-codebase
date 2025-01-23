from mr import MergeRequest, MergeRequestExtendedStatus, MergeRequestException
import pytest

# test equalities
def test_simple_rejected():
    merge_request = MergeRequest()
    merge_request.downvote("maintainer")
    assert merge_request.status == MergeRequestExtendedStatus.REJECTED

def test_just_created_is_pending():
    assert MergeRequest().status == MergeRequestExtendedStatus.PENDING

def test_pending_awaiting_review():
    merge_request = MergeRequest()
    merge_request.upvote("core-dev")
    assert merge_request.status == MergeRequestExtendedStatus.PENDING


# test exepctions
def test_invalid_types():
    merge_request = MergeRequest()
    pytest.raises(TypeError, merge_request.upvote, {"invalid-object"})

def test_cannot_vote_on_closed_merge_request():
    merge_request = MergeRequest()
    merge_request.close()
    pytest.raises(MergeRequestException, merge_request.upvote, 'dev1')
    with pytest.raises(
        MergeRequestException,
        match="can't vote on a closed merge request",
    ):
        merge_request.downvote('dev1')

# if __name__ == "__main__":
#     pytest.main()