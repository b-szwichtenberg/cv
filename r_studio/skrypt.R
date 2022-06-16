#Zadanie 1
akcje <- tatry$Close
x <- as.Date(tatry$Date)
plot(x,akcje, xlab = "2020",ylab = "Kurs (PLN)")
hist(akcje,xlab = "Kurs (PLN)",ylab = "Frekwencja",main = "Histogram kursów zamkniêcia")

#Zadanie 2
mean(akcje)
sd(akcje)
library(moments)
skewness(akcje)
kurtosis(akcje)

#Zadanie 3
library(MASS)
library(fitdistrplus)
XX <- rnorm(100,mean(akcje),sd(akcje))
fit <- fitdistr(XX,"normal")
fit
m1 <- fit$estimate[[1]]
s1 <- fit$estimate[[2]]
YY <- rlnorm(100,mean(akcje),sd(akcje))
fit2 <- fitdistr(YY,"log-normal")
fit2
m2 <- fit2$estimate[[1]]
s2 <- fit2$estimate[[2]]

#Zadanie 4
par(mfrow=c(2,2))
plot.legend <- c("norm", "log")
denscomp(list(fn, ft), legendtext = plot.legend)
qqcomp(list(fn, ft), legendtext = plot.legend)
cdfcomp(list(fn, ft), legendtext = plot.legend)
ppcomp(list(fn, ft), legendtext = plot.legend)

gofstat(list(fn, ft),  fitnames = c("normal", "t"))


#Czêœæ 2!!!!! (zwroty)

#zadanie 1
zwrot <- tatry$Close
R = diff(log zwrot)
date <- as.Date(tatry$Date)
plot(R,ylab = "Wartoœæ zwrotu")
hist(R,xlab = "Zwroty",ylab = "Frekwencja",main = "Histogram zwrotów")

#zadanie 2
#Identycznie jak w czêœci 1 tylko dla zmiennej R
mean(R) itd.

#zadanie 3
library(MASS)
library(fitdistrplus)
XX <- rnorm(100,mean(R),sd(R))
fit <- fitdistr(XX,"normal")
fit
m1 <- fit$estimate[[1]]
s1 <- fit$estimate[[2]]
YY <- rlnorm(100,mean(R),sd(R))
fit2 <- fitdistr(YY,"log-normal")
fit2
m2 <- fit2$estimate[[1]]
s2 <- fit2$estimate[[2]]

#zadanie 4
par(mfrow=c(2,2))
plot.legend <- c("norm", "log")
denscomp(list(fn, ft), legendtext = plot.legend)
qqcomp(list(fn, ft), legendtext = plot.legend)
cdfcomp(list(fn, ft), legendtext = plot.legend)
ppcomp(list(fn, ft), legendtext = plot.legend)

gofstat(list(fn, ft),  fitnames = c("normal", "t"))