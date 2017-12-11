#-*-encoding:UTF-8-*-
""" generateParameterSpace Module
Generate the parameters' space according to the rules configured
by the user in this module. Allows non-linear increments.
"""

# Librairies
import numpy as np
from numpy.random import randint as rand
import itertools as it

class parameterSpace:
    def __init__(self):
        # Initialisation
        # paramters:          start, inc, stop
        self.params = {'f0' : [100, 100, 1000],
                       'PS' : [-0.01, -0.01, -0.01],
                       'PH' : [0, 1 ,1],
                       'inh': [0, 0.5, 10],
                       'SnR' : [1, 0.08,1]}

        self.parameter_space = dict.fromkeys(self.params)
        self.N_samples = None # number of samples to generate

        # Generating parameters
        self.generate_parameter_space()
        self.permutations_array = self.make_permutations()
        self.param_dataset_dict = self.perm_to_dict()
        
    def perm_to_dict(self):
        """ Converts the permutations into a list of dictionnaries for the 
        audioEngine module
        
        Returns:
            param_dataset: array of dict
        """
        
        temp_dict = dict.fromkeys(self.params)
        N_set_of_params = len(self.permutations)
        output_dict_param = [temp_dict.copy() for i in xrange(N_set_of_params)]
        
        for i in xrange(N_set_of_params):
            output_dict_param[i]['f0']  = np.copy(self.permutations[i][0])
            output_dict_param[i]['PS']  = np.copy(self.permutations[i][1])
            output_dict_param[i]['PH']  = np.copy(self.permutations[i][2])
            output_dict_param[i]['inh'] = np.copy(self.permutations[i][3])
            output_dict_param[i]['SnR'] = np.copy(self.permutations[i][4])
            
        return output_dict_param
    
    def generate_parameter_space(self):
        """ Generate all the values of the parameters specfied in the __init__
        function: [start, increment, end]. It allows non linear increment

        Returns
            - self.parameterSpace: dictionnaire, where each paramter's
            name is a key and its value is a list of values
        """

        for key, value in self.params.iteritems():
            # Extracing params
            start = value[0]
            stop = value[2]
            inc = value[1]

            # Vector
            self.parameter_space[key] = np.arange(start, stop+inc, inc)
            
    def make_permutations(self):
        """ Does all the permutations generated by the parameter space
        
        returns:
            - permutations: N*param array containig all the permutations possible
        """
        
        # Generating permutations
        f0 = self.parameter_space['f0']
        PS = self.parameter_space['PS']
        PH = self.parameter_space['PH']
        inh= self.parameter_space['inh']
        SnR= self.parameter_space['SnR']
        
        self.permutations = np.array(list(it.product(f0, PS, PH, inh, SnR)))
        self.N_samples = len(self.permutations)
        
                
        return self.permutations

