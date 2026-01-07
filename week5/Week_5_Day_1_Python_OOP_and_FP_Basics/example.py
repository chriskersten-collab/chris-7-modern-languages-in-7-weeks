class Application:
    def __init__(self, company: str, sent: int, response: bool = False):
        self.company = company
        self.sent = sent
        self.response = response
    
    def describe(self) -> str:
        return f"Applied to {self.company}, {self.sent} applications sent."
    
    def mark_responded(self):
        self.response = True

    def status(self) -> str:
        return "Responded" if self.response else "No response yet"

def total_hours(sessions: list[int]) -> int:
    return sum(sessions)

'''  backup from main.py
class StudySession:
    def __init__(self, topic: str, hours: int):
        self.topic = topic
        self.hours = hours

    def summary(self) -> str:
        return f"Studied {self.topic} for {self.hours} hours"
'''

    
if __name__ == "__main__":
    app1 = Application("TechCorp", 5)
    
    print(app1.status())
    app1.mark_responded()
    print(app1.status())

    sessions = [1, 2, 3, 2]

#    doubled = list(map(lambda h: h * 2, sessions))
#    filtered = list(filter(lambda h: h >= 2, sessions))

    doubled = [h * 2 for h in sessions]
    filtered = [h for h in sessions if h >= 2]

    print("Total hours studied:", total_hours(sessions))
    print("Doubled hours:", doubled)
    print("Filtered hours (>=2):", filtered)

