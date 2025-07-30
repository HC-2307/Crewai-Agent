import sys
from online_course_builder.crew import OnlineCourseBuilder

def run():
    """
    Run the OnlineCourseBuilder crew.
    """
    inputs = {
        'topic': 'Web Development for Beginners',
        'current_year': '2025'
    }

    OnlineCourseBuilder().crew().kickoff(inputs=inputs)