

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


class Question:

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


class Quiz:

    def __init__(self, questions: list, name: str, type: str):
        self.questions = questions
        self.name = name
        self.type = type


class Marking:

    def __init__(self, quiz: Quiz) -> None:
        self.quiz = quiz
        _quiz = quiz

    def mark(self) -> int:
        total_score = len(self.quiz.questions)
        obtained_score = 0
        if len(self.quiz.questions) == 0:
            return obtained_score
        for question in self.quiz.questions:
            if question.chosen_answer == question.correct_answer:
                obtained_score += 1
        return int((obtained_score * 100) / total_score)

    def generate_assessment(self) -> Assessment:
        name = self.quiz.name
        type = self.quiz.type
        score = self.mark()
        if type == "multiple-choice":
            return MultipleChoiceAssessment(name, score)
        if type == "technical":
            return TechnicalAssessment(name, score)
        if type == "presentation":
            return PresentationAssessment(name, score)


if __name__ == "__main__":
    # Example questions and quiz
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")

    # Add an implementation for the Marking class below to test your code
# m = Marking(quiz)
# print(m.mark())
