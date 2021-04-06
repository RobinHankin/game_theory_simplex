# this is a difference of three, eg: player A has 8 marbles and B has 5


from sage.numerical.backends.generic_backend import get_solver
w = MixedIntegerLinearProgram(solver = "GLPK")
x = w.new_variable()


NUM = 134



def f(n,j):
    out = [i*0 for i  in range(n)]
    out[j+0] = 0.5
    out[j+1] = 1
    out[j+2] = 1
    out[j+3] = 0.5
    return(out)

w.set_objective(  sum([-x[i] for i in range(NUM)]))

for noz in range(NUM-3):
    w.add_constraint(sum([f(NUM,noz)[i]*x[i] for i in range(NUM)]) >=1 )


for nox in range(NUM):
    w.add_constraint(x[nox] >= 0)



w.solve()

#w.add_constraint(sum([f(9,1)[i]*x[i] for i in range(9)]) >=1 )
#w.add_constraint(sum([f(9,2)[i]*x[i] for i in range(9)]) >=1 )
#w.add_constraint(sum([f(9,3)[i]*x[i] for i in range(9)]) >=1 )
#w.add_constraint(sum([f(9,4)[i]*x[i] for i in range(9)]) >=1 )
#w.add_constraint(sum([f(9,5)[i]*x[i] for i in range(9)]) >=1 )

#w.add_constraint(0.5*x[0] + 1.0*x[1] + 1.0*x[2]  + 0.5*x[3] + 0.0*x[4] + 0.0*x[5] + 0.0*x[6]  + 0.0*x[7] + 0.0*x[8] >= 1)
#w.add_constraint(0.0*x[0] + 0.5*x[1] + 1.0*x[2]  + 1.0*x[3] + 0.5*x[4] + 0.0*x[5] + 0.0*x[6]  + 0.0*x[7] + 0.0*x[8] >= 1)
#w.add_constraint(0.0*x[0] + 0.0*x[1] + 0.5*x[2]  + 1.0*x[3] + 1.0*x[4] + 0.5*x[5] + 0.0*x[6]  + 0.0*x[7] + 0.0*x[8] >= 1)
#w.add_constraint(0.0*x[0] + 0.0*x[1] + 0.0*x[2]  + 0.5*x[3] + 1.0*x[4] + 1.0*x[5] + 0.5*x[6]  + 0.0*x[7] + 0.0*x[8] >= 1)
#w.add_constraint(0.0*x[0] + 0.0*x[1] + 0.0*x[2]  + 0.0*x[3] + 0.5*x[4] + 1.0*x[5] + 1.0*x[6]  + 0.5*x[7] + 0.0*x[8] >= 1)
#w.add_constraint(0.0*x[0] + 0.0*x[1] + 0.0*x[2]  + 0.0*x[3] + 0.0*x[4] + 0.5*x[5] + 1.0*x[6]  + 1.0*x[7] + 0.5*x[8] >= 1)

#w.add_constraint(x[0] >= 0)
#w.add_constraint(x[1] >= 0)
#w.add_constraint(x[2] >= 0)
#w.add_constraint(x[3] >= 0)
#w.add_constraint(x[4] >= 0)
#w.add_constraint(x[5] >= 0)
#w.add_constraint(x[6] >= 0)
#w.add_constraint(x[7] >= 0)
#w.add_constraint(x[8] >= 0)


