import unittest
from mr2 import MergeRequest, MergeRequestExtendedStatus, MergeRequestException

class TestMergeRequestStatus(unittest.TestCase):
    # assertequals
    def test_simple_rejected(self):
        merge_request = MergeRequest()
        merge_request.downvote("maintainer")
        self.assertEqual(merge_request.status, MergeRequestExtendedStatus.REJECTED)

    def test_just_created_is_pending(self):
        self.assertEqual(MergeRequest().status, MergeRequestExtendedStatus.PENDING)

    def test_pending_awaiting_review(self):
        merge_request = MergeRequest()
        merge_request.upvote("core-dev")
        self.assertEqual(merge_request.status, MergeRequestExtendedStatus.PENDING)

    def test_approved(self):
        merge_request = MergeRequest()
        merge_request.upvote("dev1")
        merge_request.upvote("dev2")
        self.assertEqual(merge_request.status, MergeRequestExtendedStatus.APPROVED)

    # assertraises
    def test_cannot_upvote_on_closed_merge_request(self):
        merge_request = MergeRequest()
        merge_request.close()
        self.assertRaises(
            MergeRequestException, merge_request.upvote, "dev1"
        )

    def test_cannot_downvote_on_closed_merge_request(self):
        merge_request = MergeRequest()
        merge_request.close()
        self.assertRaisesRegex(
            MergeRequestException,
            "can't votes on a closed merge request",
            merge_request.downvote,
            "dev1",
        )

# if __name__ == "__main__":
#     unittest.main()