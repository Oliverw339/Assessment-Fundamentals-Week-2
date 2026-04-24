
from datetime import date


class Trainee:
    '''A class representing a trainee'''

    def __init__(self, name: str, email: str, date_of_birth: date):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = []

    def get_age(self) -> int:
        '''Returns the age of trainee in years '''
        date_today = date.today()
        age = date_today.year - self.date_of_birth.year - \
            ((date_today.month, date_today.day) <
             (self.date_of_birth.month, self.date_of_birth.day))
        if age < 0:
            raise ValueError("Invalid age, please amend date of birth")
        return age

    def add_assessment(self, assessment: Assessment) -> None:
        ''' Adds an Assessment to the trainee's list of assessments'''
        if isinstance(assessment, Assessment) is False:
            raise TypeError("Error that is not a valid type of assessment!")

        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        '''Returns an assessment by name from a list of assessments'''
        for assessment in self.assessments:
            if name == assessment.name:
                return assessment
        return None

    def get_assessment_of_type(self, type: str) -> list[Assessment]:
        '''Returns all assessments of the same type from a list of assessments'''
        collated_assessments = []
        for assessment in self.assessments:
            if assessment.type == type:
                collated_assessments.append(assessment)
        return collated_assessments


class Assessment:
    ''' A class representing an assessment '''

    def __init__(self, name: str, type: str, score: float):
        self.name = name
        self.type = type
        self.score = score
        if self.type not in ["multiple-choice", "technical", "presentation"]:
            raise ValueError("Error: That is not a valid type of assessment")
        if (0 <= self.score <= 100) is False:
            raise ValueError(
                "Error: That score is outside the vaild range of 0-100")


class MultipleChoiceAssessment(Assessment):
    ''' A subclass representing multiple-choice assessments'''

    def __init__(self, name: str, score: float):
        super().__init__(name, "multiple-choice", score)

    def calculate_score(self) -> float:
        '''Calculates a score weighted by 70%'''
        return self.score * 0.7


class TechnicalAssessment(Assessment):
    ''' A subclass representing technical assessments'''

    def __init__(self, name: str, score: float):
        super().__init__(name, "technical", score)

    def calculate_score(self) -> float:
        ''' Calculates a score weighted by 100%'''
        return self.score


class PresentationAssessment(Assessment):
    ''' A subclass representing presentation assessments'''

    def __init__(self, name: str, score: float):
        super().__init__(name, "presentation", score)

    def calculate_score(self) -> float:
        ''' Calculates a score weighted by 60%'''
        return self.score * 0.6


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(MultipleChoiceAssessment(
        "Python Basics", 90.1))
    trainee.add_assessment(TechnicalAssessment(
        "Python Data Structures", 67.4))
    trainee.add_assessment(MultipleChoiceAssessment("Python OOP", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
