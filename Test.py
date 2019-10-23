# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:30:29 2019

@author: czzo
"""

from sklearn import datasets

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

from AutomaticAI import ParticleSwarmOptimization as pso_algorithm


#--- MAIN ---------------------------------------------------------------------+
def main():
    # load the MNIST digits dataset
    mnist = datasets.load_digits()
    
    X = mnist.data
    y = mnist.target
   
    # Splitting the data into training set, test set and validation set
    x_train, x_test, y_train, y_test = train_test_split(X, y)

    num_particles=5
    num_iterations=30
    
    pso = pso_algorithm.PSO(particle_count=num_particles, distance_between_initial_particles=0.7, evaluation_metric=accuracy_score)
    
    best_metric, best_model = pso.fit(X_train=x_train,
                                      X_test=x_test,
                                      Y_train=y_train,
                                      Y_test=y_test,
                                      maxiter=num_iterations,
                                      verbose=True,
                                      max_distance=0.05)
            
    print("BEST")
    print(best_metric)
    print(best_model)


if __name__ == "__main__":
    main()