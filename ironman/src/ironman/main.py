import os
from dotenv import load_dotenv
from .crew import Ironman

load_dotenv()

def run():
    ironman_crew = Ironman()
    
    scenario_type = input("Enter scenario type (e.g., 'combat', 'rescue', 'stealth'): ").strip()
    input_task = ironman_crew.simulate_input_task(scenario_type)
    crew = ironman_crew.crew(input_task)

    print("\n=== SIMULATING USER-SPECIFIED SCENARIO ===\n")

    crew.kickoff()

if __name__ == "__main__":
    run()
