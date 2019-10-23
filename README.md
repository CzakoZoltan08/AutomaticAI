
AutomaticAI - A Hybrid Approach for Automatic Artificial Intelligence Algorithm Selection and Hyperparameter Tuning
===================================================================================================================

Introduction
----------------

This is method used for solving the problem of AI algorithm selection and hyperparameter tuning, without human intervention, in a fully automated way. The method is a hybrid approach, a combination between Particle Swarm Optimization and the Simulated Annealing.


Example Usage
----------------

from sklearn import datasets

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

from AutoAIAlgorithm.ParticleSwarmOptimization import PSO



def main():
    # load the MNIST digits dataset

    mnist = datasets.load_digits()
    
    X = mnist.data

    y = mnist.target
   
    # Splitting the data into training set, test set and validation set

    x_train, x_test, y_train, y_test = train_test_split(X, y)

    num_particles=5

    num_iterations=30
    
    pso = PSO(particle_count=num_particles,
              distance_between_initial_particles=0.7,
              evaluation_metric=accuracy_score)
    
    best_metric, best_model = pso.fit(X_train=x_train,
                                      X_test=x_test,
                                      Y_train=y_train,
                                      Y_test=y_test,
                                      maxiter=num_iterations,
                                      verbose=True,
                                      max_distance=0.05)
            
    print(best_metric)
    print(best_model)


if __name__ == "__main__":
    main()