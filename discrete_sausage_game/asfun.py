# Function f() is the payoff matrix for the final stage (that is, the
# final *two* rounds) of the sausage game.  The first stage has been
# played and is assumed not to be a draw (if it *was* a draw, the
# whole game must be a draw as the only outcomes are DDD DWL DLW).

# OK, so there is an unequal number of marbles left over.  We assume
# that the row player (player I) won the first round.  The row player
# thus has strictly fewer marbles than the column player (player II).
# So the row player has to win one of the remaining rounds to win the
# overall game, and the column player (who has more marbles) has to
# win both.  That is, the winning outcomes for player I are WWL and
# WLW and the losing outcome is WLL [NB: WWW is impossible if the
# initial allocation is equal]

# This is a perfect information game.  There are three rounds.  In the
# first, players play 'x' and 'y' respectively.  Here x and y are
# integers with x <= rM, y <= cM.  x>y means player I wins the first
# round and x<y means player II wins the first round.  The remaining
# marbles [viz (rM-x) and (cM-y)] are played in the second round.  If
# (rM-x) > (cM-y) then player I wins the second round and if (rM-x) <
# (cM-y) then player II wins the second round.  Draws count as 50-50.

# So at the final stage the two players, I and II, with rM and cM
# marbles respectively, assume rM < cM [the 'r' stands for 'row' and
# the 'c' for column].  


from sage.numerical.backends.generic_backend import get_solver

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



def gamevalue(rM,cM):
    w = MixedIntegerLinearProgram(solver = "GLPK")
    x = w.new_variable()

    M = f(rM,cM)     # payoff matrix

    w.set_objective(  sum([-x[i] for i in range(cM+1)]))  # set_objective maximizes; so we minimize sum(x).

    for noz in range(rM+1):
        w.add_constraint(sum([M[noz][i]*x[i] for i in range(cM+1)]) >=1 )  

    for nox in range(cM):
        w.add_constraint(x[nox] >= 0)  # probabilities are non-negative



    w.solve()
            
    ans=[w.get_values(x[i]) for i in range(cM+1)]
    return ans
