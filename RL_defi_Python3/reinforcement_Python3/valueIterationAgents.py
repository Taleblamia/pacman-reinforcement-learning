# valueIterationAgents.py
# -----------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import mdp, util, sys

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
  """
      * Please read learningAgents.py before reading this.*

      A ValueIterationAgent takes a Markov decision process
      (see mdp.py) on initialization and runs value iteration
      for a given number of iterations using the supplied
      discount factor.
  """
  def __init__(self, mdp, discount = 0.9, iterations = 100):
    """
      Your value iteration agent should take an mdp on
      construction, run the indicated number of iterations
      and then act according to the resulting policy.
    
      Some useful mdp methods you will use:
          mdp.getStates()
          mdp.getPossibleActions(state)
          mdp.getTransitionStatesAndProbs(state, action)
          mdp.getReward(state, action, nextState)
    """
    self.mdp = mdp
    self.discount = discount
    self.iterations = iterations
    self.values = util.Counter() # A Counter is a dict with default 0
     
    "*** YOUR CODE HERE ***"
    self.best_actions = {}  # Dictionnaire pour stocker les meilleures actions pour chaque état
    
    for iteration in range(iterations):
      updated_values = util.Counter()  # Dictionnaire temporaire pour les valeurs mises à jour
        
        # Parcours de chaque état
      for state in self.mdp.getStates():
            possible_actions = self.mdp.getPossibleActions(state)
            
            if len(possible_actions) == 0:
                continue  # Si l'état n'a pas d'actions possibles, on passe à l'état suivant
            
            # Initialiser les variables pour suivre la meilleure action et la meilleure valeur
            best_action = None
            best_value = -sys.float_info.max  # Valeur initiale très faible pour comparer

            # Calculer la valeur pour chaque action
            for action in possible_actions:
                action_value = self.getQValue(state, action)  # Q-value pour l'état et l'action
                if action_value > best_value:
                    best_value = action_value  # Mettre à jour la meilleure valeur
                    best_action = action  # Mettre à jour la meilleure action
            
            # Stocker la meilleure action pour cet état
            self.best_actions[state] = best_action
            # Mettre à jour la valeur optimale pour cet état
            updated_values[state] = best_value
        
        # Mettre à jour les valeurs après l'itération
      self.values = updated_values
              
    
  def getValue(self, state):
    """
      Return the value of the state (computed in __init__).
    """
    return self.values[state]


  def getQValue(self, state, action):
    """
      The q-value of the state action pair
      (after the indicated number of value iteration
      passes).  Note that value iteration does not
      necessarily create this quantity and you may have
      to derive it on the fly.
    """
    "*** YOUR CODE HERE ***"
    stateprobPaires = self.mdp.getTransitionStatesAndProbs(state, action)
    #return a list of pairs (s', T(s,a,s'))
    #compute the expectation E
    E = 0.0
    for ss, T in stateprobPaires:
        E += T * (self.mdp.getReward(state, action, ss) + self.discount*self.values[ss])
    return E
  def getPolicy(self, state):
    """
      The policy is the best action in the given state
      according to the values computed by value iteration.
      You may break ties any way you see fit.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return None.
    """
    "*** YOUR CODE HERE ***"
    return self.best_actions.get(state)

  def getAction(self, state):
    "Returns the policy at the state (no exploration)."
    return self.getPolicy(state)
  
