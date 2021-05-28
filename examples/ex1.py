from ortools.linear_solver import pywraplp

# declare the solver
solver = pywraplp.Solver.CreateSolver('SCIP')

# Create the variables x1 and x2.
# x1: desks
# x2: tables
x1 = solver.NumVar(0, solver.infinity(), 'x1')
x2 = solver.NumVar(0, solver.infinity(), 'x2')

# Constraints
# wood
solver.Add(3 * x1 + 5 * x2 <= 3600) 

# labor
solver.Add(60 * x1 + 120 * x2 <= 96000) 

# machine time
solver.Add(50 * x1 + 20 * x2 <= 48000)

solver.Maximize(700 * x1 + 900 * x2)

status = solver.Solve()


if status == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    print('Objective value =', solver.Objective().Value())
    print('x1 =', x1.solution_value())
    print('x2 =', x2.solution_value())
else:
    print('The problem does not have an optimal solution.')

print('\nAdvanced usage:')
print('Problem solved in %f milliseconds' % solver.wall_time())
print('Problem solved in %d iterations' % solver.iterations())