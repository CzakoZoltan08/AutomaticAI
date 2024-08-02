from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

from AutomaticAI import ParticleSwarmOptimization as pso_algorithm


#--- MAIN ---------------------------------------------------------------------+
def main():
    boston_houses = datasets.load_boston()

    X = boston_houses.data
    y = boston_houses.target

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    num_particles=10
    num_iterations=20

    pso = pso_algorithm.PSO(particle_count=num_particles, distance_between_initial_particles=0.7, is_classification=False, evaluation_metric=r2_score)

    best_metric, best_model = pso.fit(X_train=x_train,
                                  X_test=x_test,
                                  Y_train=y_train,
                                  Y_test=y_test,
                                  maxiter=num_iterations,
                                  verbose=True,
                                  max_distance=0.05)
    
    print(best_model)
    print(best_metric)

if __name__ == "__main__":
    main()