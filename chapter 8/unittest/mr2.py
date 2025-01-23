from mrstatus import MergeRequestExtendedStatus, MergeRequestException

class MergeRequest:
    def __init__(self):
        self._context = {
            "upvotes": set(),
            "downvotes": set(),
        }
        self._status = MergeRequestExtendedStatus.OPEN

    def close(self):
        self._status = MergeRequestExtendedStatus.CLOSED

    def _cannot_vote_if_closed(self):
        if self._status == MergeRequestExtendedStatus.CLOSED:
            raise MergeRequestException(
                "can't votes on a closed merge request"
            )

    @property
    def status(self):
        if self._context["downvotes"]:
            return MergeRequestExtendedStatus.REJECTED
        elif len(self._context["upvotes"]) >= 2:
            return MergeRequestExtendedStatus.APPROVED
        return MergeRequestExtendedStatus.PENDING

    def upvote(self, by_user):
        self._cannot_vote_if_closed()
        self._context["downvotes"].discard(by_user)
        self._context["upvotes"].add(by_user)

    def downvote(self, by_user):
        self._cannot_vote_if_closed()
        self._context["upvotes"].discard(by_user)
        self._context["downvotes"].add(by_user)