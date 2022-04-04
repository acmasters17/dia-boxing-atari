import gym
from experimentConfiguration import NUMBER_OF_EXPERIMENTS


env = gym.make('Boxing-v0', render_mode="human")

print(env.action_space)
print(env.observation_space)

# Can do a simple punching bot
# Can map observation space to actions like he did in lectures then run a ga - lecture on 22 march
# Crossover and mutation 
for i in range (0,NUMBER_OF_EXPERIMENTS):
    print("Experiment - ", i)
    env.reset()
    totalRewardForRun = 0

    runFinished = False
    count = 0
    lastAction = 1
    while runFinished == False:
        # 18 different states for the action in boxing
        # 0 - do nothing - we want to throw fist then press zero to retract
        # 1 - throw fists and dont move      2 - move North
        # 3 - move East         4 - move West
        # 5 - move South         6 - move North East
        # 7 - move North West          8 - move South East
        # 9 - move South West
        # 10 - throw fist and move North           11 - throw fist and move East
        # 13 - throw fist and move South           14 - throw fists?
        # 15 - throw fists and move West 16 - throw fists and move East
        # 17


        if(count < 10):
            action = 3
        elif(count < 20):
            action = 5
        else:
            action = 13 if lastAction == 0 else 0
            lastAction = action
        
        count += 1
        observation, reward, done, info = env.step(action)
        totalRewardForRun = totalRewardForRun + reward
        runFinished = done
        


    # Final reward gets lower the better the score
    print("Total Reward for Run: ",totalRewardForRun)
    print("Number of loops: ", count)

    env.close()

