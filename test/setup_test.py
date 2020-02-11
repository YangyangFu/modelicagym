def test_pyfmi():
	from pyfmi import load_fmu
	model = load_fmu("ModelicaGym_CartPole.fmu",
                     kind="CS")

	model.reset()
	model.setup_experiment(start_time=0)
	model.initialize()
	opts = model.simulate_options()
	opts['ncp'] = 50
	opts['initialize'] = False
	model.set("f", -1)
	model.simulate(start_time=0, final_time=2, options=opts)
	model.set("f", -1)
	model.simulate(start_time=2, final_time=3, options=opts)
	print("PyFMI is available and successfully simulating.")

# set visualise=True requires the docker to render on X11 server, which is not available currently.
def test_gym(visualize=False):
    import gym
    env = gym.make('CartPole-v0')
    env.reset()
    for _ in range(1000):
        if visualize:
            env.render(mode='rgb_array')
        env.step(env.action_space.sample())
    env.close()
    print("OpenAI Gym is available and successfully working.")


if __name__ == '__main__':
    test_pyfmi()
    test_gym()
