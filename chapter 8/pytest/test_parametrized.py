import pytest
from mr_parametrized import MergeRequestExtendedStatus , AcceptanceThreshold

@pytest.mark.parametrize("context,expected_status", (
    (
        {"downvotes": set(), "upvotes": set()},
        MergeRequestExtendedStatus.PENDING
    ),
    (
        {"downvotes": set(), "upvotes": {"dev1"}},
        MergeRequestExtendedStatus.PENDING,
    ),
    (
        {"downvotes": "dev1", "upvotes": set()},
        MergeRequestExtendedStatus.REJECTED,
    ),
    (
        {"downvotes": set(), "upvotes": {"dev1", "dev2"}},
        MergeRequestExtendedStatus.APPROVED,
    ),
),)
def test_acceptance_threshold_status_resolution(context, expected_status):
    assert AcceptanceThreshold(context).status() == expected_status