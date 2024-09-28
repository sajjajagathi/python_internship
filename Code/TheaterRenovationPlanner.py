# Defining the RenovationPlan class
class RenovationPlan:
    def __init__(self, project_id, description, start_date, end_date, budget):
        self.project_id = project_id
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
    
    def update_plan(self, description, start_date, end_date, budget):
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
    
    def display_plan(self):
        return f"Project ID: {self.project_id}, Description: {self.description}, " \
               f"Start Date: {self.start_date}, End Date: {self.end_date}, Budget: {self.budget}"


# Defining the TheaterRenovationPlanner class to manage renovation plans and monitor impacts
class TheaterRenovationPlanner:
    def __init__(self):
        self.renovation_plans = []  # List to store renovation plans
    
    # Add a new renovation plan
    def add_plan(self, project_id, description, start_date, end_date, budget, user_input=False):
        new_plan = RenovationPlan(project_id, description, start_date, end_date, budget)
        self.renovation_plans.append(new_plan)
        if user_input:
            print(f"\nThank you! Your renovation plan has been successfully added: {new_plan.display_plan()}")
        else:
            print(f"\nRenovation Plan Added: {new_plan.display_plan()}")
    
    # Remove a renovation plan by project_id
    def remove_plan(self, project_id):
        self.renovation_plans = [plan for plan in self.renovation_plans if plan.project_id != project_id]
        print(f"\nRenovation Plan with Project ID {project_id} has been removed.")
    
    # Update an existing renovation plan
    def update_plan(self, project_id, description, start_date, end_date, budget):
        for plan in self.renovation_plans:
            if plan.project_id == project_id:
                plan.update_plan(description, start_date, end_date, budget)
                print(f"\nRenovation Plan Updated: {plan.display_plan()}")
    
    # List all renovation plans
    def list_all_plans(self):
        print("\nListing All Renovation Plans:")
        if not self.renovation_plans:
            print("No renovation plans available.")
        else:
            for plan in self.renovation_plans:
                print(plan.display_plan())
    
    # Allow the user to choose a plan by selecting from the list of plans
    def select_plan(self):
        if not self.renovation_plans:
            print("No renovation plans available to select.")
            return None
        else:
            print("\nPlease select a renovation plan from the list below:")
            for i, plan in enumerate(self.renovation_plans):
                print(f"{i+1}. {plan.display_plan()}")
            try:
                choice = int(input("\nEnter the number of the plan you want to select: ")) - 1
                if 0 <= choice < len(self.renovation_plans):
                    return self.renovation_plans[choice].project_id
                else:
                    print("Invalid choice, please try again.")
                    return None
            except ValueError:
                print("Invalid input, please enter a number.")
                return None

    # Plan and schedule theater renovations
    def plan_theater_renovations(self, project_id):
        for plan in self.renovation_plans:
            if plan.project_id == project_id:
                print(f"\nPlanning Renovation for Project ID: {project_id}")
                print(f"Start Date: {plan.start_date}, End Date: {plan.end_date}, Budget: {plan.budget}")
                print(f"Renovation for Project {project_id} has been scheduled.")
    
    # Monitor the impacts of renovations on theater attendance and satisfaction
    def monitor_renovation_impacts(self, impact_data):
        # Impact data should be a dictionary with project_id as key and impact details as value
        print("\nMonitoring Renovation Impacts:")
        for project_id, impact in impact_data.items():
            print(f"Project ID: {project_id}, Impact: {impact}")


# Menu-driven function to interact with the user
def menu():
    planner = TheaterRenovationPlanner()

    # Predefined plans (5-7 predefined plans)
    predefined_plans = [
        (1, "Stage renovation", "2023-01-01", "2023-03-01", 50000),
        (2, "Lighting upgrade", "2023-04-01", "2023-05-01", 30000),
        (3, "Seating replacement", "2023-06-01", "2023-07-01", 75000),
        (4, "Sound system upgrade", "2023-08-01", "2023-09-15", 45000),
        (5, "Lobby renovation", "2023-10-01", "2023-11-01", 60000),
        (6, "Projection system upgrade", "2023-11-15", "2023-12-15", 40000),
        (7, "Fire safety upgrade", "2023-12-20", "2024-01-30", 35000)
    ]

    for plan in predefined_plans:
        planner.add_plan(*plan)

    while True:
        print("\n------ Theater Renovation Planner Menu ------")
        print("1. Add a new renovation plan")
        print("2. Update an existing renovation plan")
        print("3. Remove a renovation plan")
        print("4. List all renovation plans")
        print("5. Plan and schedule a renovation")
        print("6. Monitor renovation impacts")
        print("7. Exit")
        
        choice = input("\nSelect an option (1-7): ")
        
        if choice == '1':  # Add a new renovation plan
            project_id = int(input("Enter Project ID: "))
            description = input("Enter Description: ")
            start_date = input("Enter Start Date (YYYY-MM-DD): ")
            end_date = input("Enter End Date (YYYY-MM-DD): ")
            budget = float(input("Enter Budget: "))
            planner.add_plan(project_id, description, start_date, end_date, budget, user_input=True)
        
        elif choice == '2':  # Update an existing renovation plan
            project_id = planner.select_plan()
            if project_id:
                description = input("Enter New Description: ")
                start_date = input("Enter New Start Date (YYYY-MM-DD): ")
                end_date = input("Enter New End Date (YYYY-MM-DD): ")
                budget = float(input("Enter New Budget: "))
                planner.update_plan(project_id, description, start_date, end_date, budget)
        
        elif choice == '3':  # Remove a renovation plan
            project_id = planner.select_plan()
            if project_id:
                planner.remove_plan(project_id)
        
        elif choice == '4':  # List all renovation plans
            planner.list_all_plans()
        
        elif choice == '5':  # Plan and schedule a renovation
            project_id = planner.select_plan()
            if project_id:
                planner.plan_theater_renovations(project_id)
        
        elif choice == '6':  # Monitor renovation impacts
            num_projects = int(input("Enter the number of projects to monitor: "))
            impact_data = {}
            for _ in range(num_projects):
                project_id = int(input("Enter Project ID: "))
                impact = input("Enter Impact (e.g., Increased attendance by 15%): ")
                impact_data[project_id] = impact
            planner.monitor_renovation_impacts(impact_data)
        
        elif choice == '7':  # Exit the program
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice! Please select a valid option.")

# Run the menu-driven program
menu()
