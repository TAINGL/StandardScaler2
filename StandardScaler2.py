class StandardScaler2:
    def __init__ (self):
        self.params_ = {'mean': None , 'std': None}

    def fit(self, X):
        self.mean_ = np.mean(X, axis=0)
        self.std_ = np.std(X, axis=0)
        self.params_ = {'mean': self.mean_ , 'std': self.std_}
        return self
    
    def transform(self, X):
        return (X - self.mean_)/self.std_
    
    def fit_transform(self,X):
        return self.fit(X).transform(X)