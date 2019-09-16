#Rosenbrock function
#a=1
#b=100

f <- function(x,y)
{
  return((1 - x)^2 + 100 * (y - x^2)^2)
}

x0 <- 5
y0 <- 5

T0 <- 1000
T <- T0
Itr <- 0
maxItr <- 2000
Lkmax <- 50
minZita <- 10
m <- 0

repeat{
  
  Itr <- Itr + 1
  L <- 0
  Zita <- 0
  
  repeat{
    
    x <- x0 + runif(1,-0.5,0.5)
    y <- y0 + runif(1,-0.5,0.5)
    r <- runif(1,0,1)
    
    delE <- f(x,y) - f(x0,y0)
    
    if(delE < 0){
      x0 <- x
      y0 <- y
      m <- m + 1
    }else if(r < exp(-delE / T)){
      x0 <- x
      y0 <- y
      m <- m + 1
    }
    
    L <- L + 1
    Zita <- Zita + m
    
    if((L >= Lkmax) || (Zita >= minZita)){break}
  }
  T = T * 0.8
  
  if(Itr >= maxItr){break}
}

print(c(x0,y0))
print(f(x0,y0))
