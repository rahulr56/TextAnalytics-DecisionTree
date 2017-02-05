print "Setting up system"
print "Importing libraries"
import pandas as pd
import subprocess
from sklearn.tree import DecisionTreeClassifier, export_graphviz


## Read training Data file
print "Reading training dataset"
try:
    data = pd.read_csv(open('../DataSet/DigitRecognition/optdigits_raining.csv'))
except Exception as e:
    print "Error in opening Tarining Dataset"
    print "Error Message : "+str(e)
    exit(1)

## Read Test dataset
print "Reading test dataset"
try:
    testdata = pd.read_csv(open('../DataSet/DigitRecognition/optdigits_test.csv'))
except Exception as e:
    print "Failed to open testing data set : "+str(e)
    ip=input("Do you wish to continue(Y/N)?").lower()
    if ip.contanins('y'):
        print "Proceeding without test data set..."
        pass
    else:
        print "Exitting after Cleanup..."
        data.close()
        exit(1)

## Separate features and results in training dataset
print "Processing training dataset"
targetDataResult = (data['result']).reshape(-1,1)
targetFeatures = list(data.columns[:-1])
targetDataFeatures=data[targetFeatures]

## Fit the training data set into decision tree classifier
## This builds us a decision tree
print "Building a decision tree from training data"
dt = DecisionTreeClassifier(min_samples_split=15, random_state=9)
dt.fit(targetDataFeatures,targetDataResult)

print "Processing test dataset"
## Separate features and results in Test dataset
testtarget = testdata['result']
testFeatureList = list(testdata.columns[:-1])
testResults=testdata['result']
testFeatures=testdata[testFeatureList]

## Predict test data beased on the decision tree formed from training dataset
predictedTestResults=list(dt.predict(testFeatures))


actualTestResults=list(testResults)
print "Prediction complete"
print "Calculating Prediction results"
s=f=0
for i in range(len(actualTestResults)-2):
	if actualTestResults[i] == predictedTestResults[i]:
		s=s+1
	else:
		f=f+1
print "--------------------------------------------------------------------------"
print "\n\n"
print "Percentage of data that is predicted correctly is "+str(float(s)/len(actualTestResults)*100.0)
print "Percentage of data that is predicted wrong is "+str(float(f)/len(actualTestResults)*100.0)
print "Prediction rate is "+str(float(s)/len(actualTestResults)*100.0)
print "\n"
print "--------------------------------------------------------------------------"

print "Visualizing text of decision tree is stored in DigitalImageRecognitionDecisonTree.dot file"
with open("DigitalImageRecognitionDecisonTree.dot", 'w') as f:
	export_graphviz(dt, out_file=f,feature_names=testFeatureList)

#while True:
#    ans=raw_input("Do you want to predict a digit?(Y/N) ").strip()
#    if ans=='Y' or ans=='y':
#        digitToPredict=[]
#        r1=raw_input("Enter the 8x8 matrix to predict rating: \n").strip()
#        digitToPredict.append(r1.split(' '))
#        predict=[]
#        try:
#            predict=[int(digit) for digit in digitToPredict ]
#        except Exception as e:
#            print "Error in data"
#            print "Enter integer values only"
#            continue
#        if len(r1) == 64:
#            print predict
#            dt.predict(predict)
#            print str(list(dt.predict(predictionDataFeatures)))
#        else:
#            print "Incorrect data enetered"
#            print "Please enter data as 64 space separated integers"
#    elif ans=='N' or ans=='n':
#        print "Exitting.."
#        exit(0)
#    else:
#        print "Invalid Input"
