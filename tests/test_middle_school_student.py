from school_schedule.middle_school_student import MiddleSchoolStudent

def test_new_valid_middle_school_student_gets_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation = True)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert ellis.gets_transportation

def test_new_valid_middle_school_student_with_defaults():
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]
    
    student1 = MiddleSchoolStudent(name, grade, classes)

    assert student1.name == name
    assert student1.grade == grade
    assert student1.classes == classes
    assert len(student1.classes) == 1
    assert student1.gets_transportation == False
    

def test_middle_school_student_summary_with_transportation():
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    student1 = MiddleSchoolStudent(name, grade, classes, gets_transportation = True)
    
    summary = student1.summary()

    expected_summary = "Ellis is a junior enrolled in 1 classes: Painting\nThis student receives transportation."

    assert summary == expected_summary

def test_middle_school_student_summary_without_transportation():
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    student1 = MiddleSchoolStudent(name, grade, classes, gets_transportation = False)
    
    summary = student1.summary()

    expected_summary = "Ellis is a junior enrolled in 1 classes: Painting\nThis student does not receive transportation."

    assert summary == expected_summary
