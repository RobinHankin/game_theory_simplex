# we have two players:
# Player I,  row player, maximizing player.
# Player II, col player, minimizing player.

# Payoffs are to player I.  This is why he is the maximizing player.

require(Oarray)
points_won <- function(rM,cM){  # This is a matrix for the final two
                                        # rounds.  It returns a matrix
                                        # whose entries are the the
                                        # number of points (win=1,
                                        # draw=0.5) won by player I, the
                                        # row player.  Canonical use:
                                        # points_won(5,8) Thus the row
                                        # player (I) has 5 marbles and
                                        # the col player (II) has 8.
    # points_won(5.8)[3,4] = 

    
    if (rM>cM){
        return(2-t(Recall(cM,rM)))   # NB arguments swapped over
    } else if(rM == cM){
        out <- matrix(1,rM+1,cM+1) # either one win and one loss; or two draws
    } else {  # default case: rM < cM
        out <- matrix(1,rM+1,cM+1)
        d <- row(out)-col(out)
        out[d == 0    ] <- 0.5
        out[d == rM-cM] <- 0.5
        
        out[ (d<0) & (d>rM-cM)] <- 0
    }
    out <- as.Oarray(out,offset=0)
#    dimnames(out) <- list(I=0:rM,II=0:cM)
#    rownames(out) <- NULL
#    colnames(out) <- NULL
    return(out)
}

# first round: row player plays i (i=0,1,...,n) and the col player plays j (j=0,...,n)


allocation_I  <- 10  # row player; maximizing player; player I
allocation_II <- 10  # col player; minimizing player; player II

for(play_I in 0:allocation_I){  
    for(play_II in 0:allocation_II){  
        mI  <- allocation_I  - play_I
        mII <- allocation_II - play_II

        if(play_I>play_II){ # player I wins first round, needs to win only one of the following
            payoff_matrix <- points_won(rM=mI, cM = mII)   # player I is the row player, (5,8)
        } else if(play_I<play_II){ # player I loses first round, needs to win both following
            payoff_matrix <- points_won(rM=allocation_I - play_I, cM=allocation_II - play_II)-1
        } else if(play_I == play_II){ # draw
            payoff_matrix <- points_won(rM=allocation_I - play_I, cM=allocation_II - play_II) # uniform
        } else {
            stop("This cannot happen")
        }

        print(payoff_matrix)
    }


}


