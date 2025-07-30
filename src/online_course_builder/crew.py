# online_course_builder/crewy.py

from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os

@CrewBase
class OnlineCourseBuilder():
    """Online Course Builder Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def curriculum_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['curriculum_designer'],
            verbose=True
        )

    @agent
    def lesson_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['lesson_planner'],
            verbose=True
        )

    @agent
    def quiz_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['quiz_generator'],
            verbose=True
        )

    @task
    def curriculum_task(self) -> Task:
        return Task(
            config=self.tasks_config['curriculum_task'],
            output_file='output/curriculum.md'
        )

    @task
    def lesson_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['lesson_planning_task'],
            output_file='output/lesson_plan.md'
        )

    @task
    def quiz_task(self) -> Task:
        return Task(
            config=self.tasks_config['quiz_task'],
            output_file='output/quizzes.md'
        )

    @crew
    def crew(self) -> Crew:
        os.makedirs("output", exist_ok=True)

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
