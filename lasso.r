setwd('E:/¿Î³Ì/¸ç´ó/Business Analytics/project/data')
data=read.csv("scaled_X_final.csv")
neighberhoods=cbind(data[,6],data[,56:106])
neighberhoods=unique(neighberhoods)
neighberhoods=neighberhoods[,2:52]
data=data[1:3000,]
data=cbind(data[,1],data[,7:158])
a=names(data)
a[1]='reviews'
names(data)=a
X1=data[,2:50]
X2=data[,51:101]
X3=data[,103:153]

X_f=cbind(X1,X2)
X_c=cbind(X1,X3)
for (i in 1:49){
  for (j in 1:51){
    X_f[paste(names(X1)[i],names(X2)[j],sep='___')]=X1[,i]*X2[,j]
    X_c[paste(names(X1)[i],names(X3)[j],sep='___')]=X1[,i]*X3[,j]
  }
}
X_f=cbind(data['reviews'],X_f)
X_c=cbind(data['reviews'],X_c)

library(leaps)
library(glmnet)
x1 <- model.matrix(reviews ~ ., X_f)
y1 <- X_f$reviews
l=seq(2,6,length=41)
cv.out1 <- cv.glmnet(x1, y1, alpha=1,type.measure="mse", lambda=l, nfolds=10) 
plot(cv.out1)
cv.out1$lambda.min
out=glmnet(x1,y1,alpha=1,lambda=cv.out1$lambda.min)
r1=coef(out)

x2 <- model.matrix(reviews ~ ., X_c)
y2 <- X_c$reviews
l=seq(2,6,length=41)
cv.out2 <- cv.glmnet(x2, y2, alpha=1,type.measure="mse", lambda=l, nfolds=10) 
plot(cv.out2)
cv.out2$lambda.min
out=glmnet(x2,y2,alpha=1,lambda=cv.out2$lambda.min)
r2=coef(out)

#write.table(cbind(X_f[,1:101],X_f[,r1@i[r1@i>101]]),"t1.csv",row.names=FALSE,col.names=TRUE,sep=",")
#write.table(cbind(X_c[,1:101],X_c[,r2@i[r2@i>101]]),"t2.csv",row.names=FALSE,col.names=TRUE,sep=",")
case=read.csv("sample case.csv")
case=case[,7:106]
case=case[,1:49]
case=cbind(case,neighberhoods)
for (i in 1:49){
  for ( j in 1:51){
    case[paste(names(case)[i],names(neighberhoods)[j],sep='___')]=case[,i]*neighberhoods[,j]
  }
}
case=cbind(case[,1],case)
write.table(cbind(case[,1:101],case[,r1@i[r1@i>101]]),"sample_case_data.csv",row.names=FALSE,col.names=TRUE,sep=",")


