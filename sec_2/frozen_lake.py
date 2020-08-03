from itertools import count

import gym
from matplotlib import pyplot as plt


def play(env) -> float:
    score = 0
    for t in count(0, 1):
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        score += reward
        if done:
            return score


def main():
    n_games = 1000
    step = 10
    env = gym.make('FrozenLake-v0')
    results = []
    for i_episode in range(n_games):
        env.reset()
        results.append(play(env))

    win_pct = []
    for i in range(0, len(results), step):
        win_pct.append(sum(results[i:i+step]) / step)
    plt.plot(win_pct)
    plt.show()
    env.close()


if __name__ == '__main__':
    main()
