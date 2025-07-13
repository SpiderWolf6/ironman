import yaml
from pathlib import Path
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, task, crew

AGENTS_YAML = Path("src/ironman/config/agents.yaml")
TASKS_YAML = Path("src/ironman/config/tasks.yaml")

@CrewBase
class Ironman:
    def __init__(self):
        with open(AGENTS_YAML, "r") as f:
            self._agents_config = yaml.safe_load(f)

        with open(TASKS_YAML, "r") as f:
            self._tasks_config = yaml.safe_load(f)

    # Agents
    @agent
    def suit_brain(self) -> Agent:
        return Agent(config=self._agents_config["suit_brain"], verbose=True)

    @agent
    def input_simulator(self) -> Agent:
        return Agent(config=self._agents_config["input_simulator"], verbose=True)

    @agent
    def threat_assessment(self) -> Agent:
        return Agent(config=self._agents_config["threat_assessment"], verbose=True)

    @agent
    def combat_tactics(self) -> Agent:
        return Agent(config=self._agents_config["combat_tactics"], verbose=True)

    @agent
    def weapons_controller(self) -> Agent:
        return Agent(config=self._agents_config["weapons_controller"], verbose=True)

    @agent
    def defense_shield(self) -> Agent:
        return Agent(config=self._agents_config["defense_shield"], verbose=True)

    @agent
    def environmental_monitor(self) -> Agent:
        return Agent(config=self._agents_config["environmental_monitor"], verbose=True)

    @agent
    def biometrics_monitor(self) -> Agent:
        return Agent(config=self._agents_config["biometrics_monitor"], verbose=True)

    @agent
    def emergency_response(self) -> Agent:
        return Agent(config=self._agents_config["emergency_response"], verbose=True)

    @agent
    def diagnostics(self) -> Agent:
        return Agent(config=self._agents_config["diagnostics"], verbose=True)

    @agent
    def mobility_assist(self) -> Agent:
        return Agent(config=self._agents_config["mobility_assist"], verbose=True)

    @agent
    def energy_management(self) -> Agent:
        return Agent(config=self._agents_config["energy_management"], verbose=True)

    # Tasks
    @task
    def simulate_input_task(self, scenario_type="random") -> Task:
        prompt = (
            f"Simulate a '{scenario_type}' test scenario for the Iron Man suit. "
            "Include user intent, location, environment conditions, and urgency."
        )
        return Task(
            config=self._tasks_config["simulate_input_task"],
            agent=self.input_simulator(),
            prompt=prompt  # override default prompt using input
        )
    
    @task
    def threat_assessment_task(self) -> Task:
        return Task(config=self._tasks_config["threat_assessment_task"], agent=self.threat_assessment())

    @task
    def combat_mode_recommendation_task(self) -> Task:
        return Task(config=self._tasks_config["combat_mode_recommendation_task"], agent=self.combat_tactics())

    @task
    def weapon_activation_task(self) -> Task:
        return Task(config=self._tasks_config["weapon_activation_task"], agent=self.weapons_controller())

    @task
    def shield_activation_task(self) -> Task:
        return Task(config=self._tasks_config["shield_activation_task"], agent=self.defense_shield())

    @task
    def environment_monitoring_task(self) -> Task:
        return Task(config=self._tasks_config["environment_monitoring_task"], agent=self.environmental_monitor())

    @task
    def health_monitoring_task(self) -> Task:
        return Task(config=self._tasks_config["health_monitoring_task"], agent=self.biometrics_monitor())

    @task
    def diagnostics_task(self) -> Task:
        return Task(config=self._tasks_config["diagnostics_task"], agent=self.diagnostics())

    @task
    def mobility_support_task(self) -> Task:
        return Task(config=self._tasks_config["mobility_support_task"], agent=self.mobility_assist())

    @task
    def energy_check_task(self) -> Task:
        return Task(config=self._tasks_config["energy_check_task"], agent=self.energy_management())

    @task
    def emergency_check_task(self) -> Task:
        return Task(config=self._tasks_config["emergency_check_task"], agent=self.emergency_response())

    @task
    def strategic_decision_task(self) -> Task:
        return Task(config=self._tasks_config["strategic_decision_task"], agent=self.suit_brain())

    @crew
    def crew(self, input_task) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=[
                input_task,  # This is the one dynamically generated from user input
                self.threat_assessment_task(),
                self.combat_mode_recommendation_task(),
                self.weapon_activation_task(),
                self.shield_activation_task(),
                self.environment_monitoring_task(),
                self.health_monitoring_task(),
                self.diagnostics_task(),
                self.mobility_support_task(),
                self.energy_check_task(),
                self.emergency_check_task(),
                self.strategic_decision_task(),
            ],
            process=Process.sequential,
            verbose=True,
        )
