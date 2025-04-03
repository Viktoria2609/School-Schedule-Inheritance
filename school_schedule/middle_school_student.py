from .student import Student

# add MiddleSchoolStudent here
class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation = False):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation

    def display_get_transportation_message(self):
        if self.gets_transportation:
            return "This student receives transportation."
        else:
            return "This student does not receive transportation."

    
    def summary(self):
        student_summary = super().summary()
        transportation_message = self.display_get_transportation_message()
        return "\n".join((student_summary, transportation_message))