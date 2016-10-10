import pickle

data=[["python","perl"],[0,0]]

with open("language.pickle","wb") as f:
    pickle.dump(data,f)
