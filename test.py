import rpy2.robjects as robjects

A = robjects.r("""
library(fscaret)
dataset_SO <- read.csv(file = 'C:/Users/pymnb/OneDrive/Desktop/for SA/15Dataset_SO_Tiers1.csv', header = F)
dt = sort(sample(nrow(dataset_SO), nrow(dataset_SO)*.8))
train<-dataset_SO[dt,]
test<-dataset_SO[-dt,]
myFS <- fscaret(train, test, myTimeLimit = 5, preprocessData=F, Used.funcRegPred=c("ridge", with.labels=TRUE, supress.output=FALSE, no.cores=12)
myRES_tab <- myFS$VarImp$matrixVarImp.MSE[1:31,]
""")
print(A)

# "bstTree","bayesglm" , "cubist", "enet" , "kknn" , "knn" , "lars" , "lasso" , "mlp" , "mlpWeightDecay" , "pcr" , "pls" , "ppr" , "relaxo" , "ridge" , "rpart"