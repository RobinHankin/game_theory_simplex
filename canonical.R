
# figures out optimal strategy using Equations 16 and 17 of Ferguson with an offset.


# thing to be optimized is c(v,p1,p2,...,pn)

require(linprog)

minmax <- function(A,give=FALSE){
    n <- dim(A)[1]
    out <-
        solveLP(cvec=rep(1,n),bvec=rep(1,n),Amat=t(A),const.dir=rep(">=",n),maximum=FALSE)
    if(give){
        return(out)
    } else {
        jj <- out$solution
        value <- 1/sum(jj)
        jj <- jj/sum(jj)
        names(jj) <- rownames(A)
        return(list(probs=jj,value=value))
    }
}
        
