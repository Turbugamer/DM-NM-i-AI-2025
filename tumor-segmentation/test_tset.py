from PyTsetlinMachine.tm import MultiClassTsetlinMachine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Bitstrenger og labels
X = [...]  # Liste av bitstrenger (0/1), f.eks. fra convertToBitstrings()
y = [...]  # Liste av labels, 0 = normal, 1 = kreft

# Del opp data i trening og testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Lag og tren modellen
tm = MultiClassTsetlinMachine(number_of_clauses=100, T=50, s=3.9)
tm.fit(X_train, y_train, epochs=100)

# Evaluer nøyaktighet
y_pred = tm.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("Nøyaktighet:", acc)

# Lagre modellen til fil
#with open("tm_model.pkl", "wb") as f:
#    pickle.dump(tm, f)