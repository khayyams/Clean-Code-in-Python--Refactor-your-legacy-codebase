class Event:
    def meets_condition(self, event_data: dict) -> bool:
        return False

class LoginEvent(Event):
    def meets_condition(self, event_data: dict) -> bool:
        return (
            event_data["before"]["session"] == 0
            and event_data["after"]["session"] == 1
        )

class LogoutEvent(Event):
    def meets_condition(self, event_data: dict) -> bool:
        return (
            event_data["before"]["session"] == 1
            and event_data["after"]["session"] == 0
        )