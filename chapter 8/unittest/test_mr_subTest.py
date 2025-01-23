import unittest
from mr_parametrized import MergeRequest, MergeRequestExtendedStatus, MergeRequestException, AcceptanceThreshold

class TestMergeRequestStatus(unittest.TestCase):

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
            "can't vote on a closed merge request",
            merge_request.downvote,
            "dev1",
        )

class TestAcceptanceThreshold(unittest.TestCase):
    def setUp(self):
        self.fixture_data = (
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
        )

    def test_status_resolution(self):
        for context, expected in self.fixture_data:
            with self.subTest(context=context):
                status = AcceptanceThreshold(context).status()
                self.assertEqual(status, expected)



# if __name__ == "__main__":
#     unittest.main()