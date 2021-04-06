# two players, I and II, with rM and cM marbles respectively, assume
# rM < cM.  Perfect information game.  There are two rounds.  In the
# first, players play 'x' and 'y' respectively. x and y are integers
# with x <= rM, y <= cM.  x>y means player I wins the first round and
# x<y means player II wins the first round.  The remaining marbles
# [viz rM-x and rC-y] are played in the second round.  If rM-x > rC-y
# then player I wins the second round and if rM-x < rC-y then player
# II wins the second round.  Draws count as 50-50.

# Player I has fewer marbles than player II.  Player I therefore
# cannot win both rounds.  So the scoreline will be either 1-1 or 0-2.
# A scoreline of 1-1 means player I wins the game, a scoreline of 0-2
# mens player II wins the game.  So player I tries to win at least one
# round and player II tries to win both.


from sage.numerical.backends.generic_backend import get_solver
w = MixedIntegerLinearProgram(solver = "GLPK")
x = w.new_variable()

rM = 11
cM = 13


#def f(rM,cM):   # rowplayer marbles,colplayermarbles; matrix is rM+1
                 # rows by cM+1 columns; off-by-one due to possibility
                 # of playing zero marbles

    #out = matrix(QQ,rM+1,cM+1,0)


def f(rM,cM):   # rowplayer marbles,colplayermarbles; matrix is rM+1
    out = matrix(QQ,rM+1,cM+1,0)
    for r in range(rM+1):
        out[r] = [0 for i in range(r)] + [0.5] + [1 for i in range(cM-rM-1)] + [0.5] + [0 for i in range(rM-r)]
    return out


M = f(rM,cM)     # payoff matrix

w.set_objective(  sum([-x[i] for i in range(cM+1)]))  # set_objective maximizes; so we minimize sum(x).

for noz in range(rM+1):
    w.add_constraint(sum([M[noz][i]*x[i] for i in range(cM+1)]) >=1 )

for nox in range(cM):
    w.add_constraint(x[nox] >= 0)

w.solve()

ans=[w.get_values(x[i]) for i in range(cM+1)]
