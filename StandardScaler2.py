class StandardScaler2:
    def __init__(self):
        self._X = X
        pass
        
    def fit(self, X):
        
        if (type(X) == np.ndarray):
            self.mean_ = np.mean(X, axis=0)
            self.std_ = np.std(X - self.mean_, axis=0)
            self.params_ = {'mean': self.mean_ , 'std': self.std_}
            
        elif(type(X) == pd.DataFrame):
            for i in range(len(X.columns)):
                df_to_array = pd.Series(X[X.columns[i]]) 
                df_to_array.to_numpy(dtype ='float32')
                self.mean_ = [np.mean(X[X.columns[i]], axis=0) for i in range(len(X.columns))]
                self.std_ = [np.std(X[X.columns[i]] - self.mean_[i], axis=0) for i in range(len(X.columns))]
                self.params_ = {'mean': self.mean_ , 'std': self.std_}
        else:
            print("Données en entrées non acceptées")
            pass

    def transform(self, X):
        if (self.params_):
            if (type(X) == np.ndarray):
                return X - self.mean_[i]/self.std_[i]
            else:
                data = [X[X.columns[i]][j] - self.mean_[i]/self.std_[i] for i in range(len(X.columns)) for j in range(len(X))]
                n = len(X.columns)
                data_size = [data[i * n:(i + 1) * n] for i in range((len(data) + n - 1) // n )]  
                df = pd.DataFrame(data_size, index = range(len(X)), columns = X.columns)
                return df
        else:
            print("Etape du fit est manquant")
            pass
        
    def fit_transform(self,X):
        return self.fit(X).transform(X)