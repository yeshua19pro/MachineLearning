from sklearn import tree

caracteristicas = [[140, 0], [130, 0], [150, 1], [170, 1]]
frutas = ["naranja", "naranja", "manzana", "manzana"]

clasificador = tree.DecisionTreeClassifier()
clasificador = clasificador.fit(caracteristicas,frutas) #
print clasificador.predict([[150, 0]])