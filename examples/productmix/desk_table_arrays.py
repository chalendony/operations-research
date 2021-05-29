from ortools.linear_solver import pywraplp

"""
Problem: Product Mix
Using arrays to define a model 
"""

# Create the data
def createdata():
    data = {}
    data["decision_names"] = ["desks", "tables"]
    data["constraint_names"] = ["wood", "labor", "machine_time"]
    data["constraint_coeffs"] = [
        [3,5], 
        [60,120],  
        [50,20]
    ]
    data["bounds"] = [3600, 96000, 48000]
    data["obj_coeffs"] = [700, 900]

    data['num_vars'] = len(data["decision_names"])
    
    # TODOs
    # should assert dimensions
    # move instance to own module/class 
    # create unit tests for the class 
    # create base class and all can inherit same properties

    return data


def main():
    data = createdata()
    # declare the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')
    # Define the decision variables
    x={}
    infinity = solver.infinity()
    nr_decision_vars = len(data["decision_names"])
    print(nr_decision_vars)
    for j in range(nr_decision_vars):
        print(f"the value of j {j}")
        x[j] = solver.NumVar(0, infinity, 'x[%i]' % j) # used later, scope needed
    print('Number of variables =', solver.NumVariables())

    # set constraints
    nr_constraints = len(data["constraint_names"])
    for i in range(nr_constraints):
        # create a constraint
        contraint = solver.RowConstraint(0, data["bounds"][i], data["constraint_names"][i])
        for j in range(nr_decision_vars):
            contraint.SetCoefficient(x[j], data["constraint_coeffs"][i][j])

    print('Number of constraints =', solver.NumConstraints())

    # define objective
    objective = solver.Objective()
    for j in range(nr_decision_vars):
        objective.SetCoefficient(x[j], data["obj_coeffs"][j])
    objective.SetMaximization()

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Objective value =', solver.Objective().Value())
        for j in range(data['num_vars']):
            print(x[j].name(), ' = ', x[j].solution_value())
        print()
        print('Problem solved in %f milliseconds' % solver.wall_time())
        print('Problem solved in %d iterations' % solver.iterations())
        print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
    else:
        print('The problem does not have an optimal solution.')


if __name__ == '__main__':
  main()