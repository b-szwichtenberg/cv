akcje <- tatry$Close
R = diff(log(akcje))
akcje2 <- mwtrade$Kurs_zam
R2 = diff(log(akcje))
df <- data.frame(R=R,R2=R2)
colMeans(df)
cov(R,R2)
cor(R,R2)
M <- cbind(R,R2)
cov(M)
cor(M)

d <- density(R)
d2 <- density(R2)
plot(d,col="red",xlab = "log zwrot",
     ylab = "gêstoœæ",
     main = "Wykres gêstoœci")
lines(d2,col="blue")

lz1 <- tatry4$log
lz2 <- mwtrade4$logz
lf <- data.frame(lz1=lz1,lz2=lz2)
sr <- colMeans(lf)
mr <- cov(lf)
funkcja <- function(lz1, lz2) dmnorm(cbind(lz1, lz2), sr, mr)
z <- outer(lz1, lz2, funkcja)
contour(lz1, lz2, z)
persp(lz1, lz2, z, theta = -30, phi = 25,shade = 0.75, col = "lightblue", expand = 0.5, r = 2,ltheta = 25, ticktype = "detailed",xlab = "R",ylab = "R2")

mu <- colMeans(df)
Sigma <- cov(df)
df <- data.frame(R=R,R2=R2)
n <- dim(M)[1]

fit.n <- fit.norm(M)
mu.n <- fit.n$mu
Sigma.n <- as.matrix(fit.n$Sigma)
X.n <- rmnorm(n,mu.n,Sigma.n)


par(mfrow=c(1,3))
plot(M, xlim=c(-0.15,0.15),ylim=c(-0.10,0.10))
plot(X.n,xlim=c(-0.15,0.15),ylim=c(-0.10,0.10))


par(mfrow=c(1,2))
qqplot(mahalanobis(df, colMeans(df), cov(df)), R, col="red", pch=19, xlab = "mahalanobis_distance", ylab="R",xlim=c(0,25),ylim=c(-0.2,0.2))
qqplot(mahalanobis(df, colMeans(df), cov(df)), R2, col="blue", pch=19, xlab = "mahalanobis_distance", ylab="R2",xlim=c(0,25),ylim=c(-0.2,0.2))

df <-data.frame(R=R,R2=R2)
library(MVN)
result = mvn(data = df, mvnTest = "mardia")
result2 = mvn(data = df, mvnTest= "hz" )
result
result2