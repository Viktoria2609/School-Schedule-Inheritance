from .student import Student

# add MiddleSchoolStudent here
class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation = False, clubs = None):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation
        self.clubs = clubs if clubs is not None else []

    def display_get_transportation_message(self):
        if self.gets_transportation:
            return "This student receives transportation."
        else:
            return "This student does not receive transportation."

    def display_clubs(self):
        club_str = ", ".join(self.clubs)

        if club_str:
           return f"{self.name} is a member of: {club_str}"
    
        return f"{self.name} hasn't joined a club yet."

    
    def summary(self):
        student_summary = super().summary()
        transportation_message = self.display_get_transportation_message()
        return "\n".join((student_summary, transportation_message))