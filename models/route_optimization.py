from stable_baselines3 import DQN
import gym

def train_rl_model(env):
    # Create and train the DQN model
    model = DQN('MlpPolicy', env, verbose=1)
    model.learn(total_timesteps=100000)
    
    # Save the model
    model.save('models/route_optimization_dqn')

def optimize_route(model, current_state):
    # Use the trained model to optimize the route
    action, _ = model.predict(current_state)
    return action