from distutils.core import setup
setup(
  name = 'AutomaticAI',         # How you named your package folder (MyLib)
  packages = ['AutomaticAI'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A Hybrid Approach for Automatic Artificial Intelligence Algorithm Selection and Hyperparameter Tuning',   # Give a short description about your library
  author = 'Czako Zoltan',                   # Type in your name
  author_email = 'czakozoltan08@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/CzakoZoltan08/AutomaticAI',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/CzakoZoltan08/AutomaticAI/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['AI', 'Arificial Intelligence', 'Particle Swarm Optimization', 'Simulated Annealing', 'Automatic Algorithm Selection', 'Automatic parameter optimization'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'sklearn',
          'numpy',
		  'scipy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Artificial Intelligence :: Automatic Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
	'Programming Language :: Python :: 3.7',
  ],
)