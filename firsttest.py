from sklearn import tree
clf = tree.DecisionTreeClassifier()
#list of lists of [height weight shoe_size] data for Trainig set
X = [[123,432,567], [553,523,569], [111,323,453], [901,342,222], [676,876,789], [454,666,786], [989,887,777]]

Y = [['cat'], ['dog'], ['dog'], ['cat'], ['cat'], ['dog'], ['cat']]
clf = clf.fit(X,Y)
#list of data for testing the model
prediction = clf.predict([[100,200,300]])

print(prediction)
