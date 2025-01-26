class Event:
    @staticmethod
    def validate_precondition(event_data: dict):
        if not isinstance(event_data, dict):
            raise ValueError("Invalid data type.")
        if "before" not in event_data or "after" not in event_data:
            raise ValueError("Missing keys.")
        
class LoginEvent(Event):
    @staticmethod
    def validate_precondition(event_data: dict, a: list):
        super().validate_precondition(event_data)
        if "session" not in event_data["after"]:
            raise ValueError("Session key is missing.")
