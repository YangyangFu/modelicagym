from modelicagym.environment import ModelicaBaseEnv, FMIStandardVersion
import logging

logger = logging.getLogger(__name__)


class ModelicaCSEnv(ModelicaBaseEnv):
    """
    Wrapper class of ModelicaBaseEnv for convenient creation of environments that utilize
    FMU exported in co-simulation mode.
    Should be used as a superclass for all such environments.
    Implements abstract logic, handles different Modelica types (JModelica, Dymola) particularities.

    """

    def __init__(self, model_path, config, fmi_version, log_level,
                 simulation_start_time=0):
        """

        :param model_path: path to the model FMU. Absolute path is advised.
        :param config: dictionary with model specifications. For more details see ModelicaBaseEnv docs
        :param fmi_version: version of FMI standard used in FMU compilation.
        :param log_level: level of logging to be used in experiments on environment.
        """
        self.simulation_start_time = simulation_start_time
        self.fmi_version = fmi_version
        logger.setLevel(log_level)
        super(ModelicaCSEnv,self).__init__(model_path, "CS", config, log_level)

    def reset(self):
        """
        OpenAI Gym API. Restarts environment and sets it ready for experiments.
        In particular, does the following:
            * resets model
            * sets simulation start time to 0
            * sets initial parameters of the model
            * initializes the model
            * sets environment class attributes, e.g. start and stop time.
        :return: state of the environment after resetting
        """
        logger.debug("Experiment reset was called. Resetting the model.")

        self.model.reset()
        if self.fmi_version == FMIStandardVersion.second:
            self.model.setup_experiment(start_time=self.simulation_start_time)

        self._set_init_parameter()
        self.model.initialize()

        # get initial state of the model from the fmu
        self.start = self.simulation_start_time
        self.stop = self.simulation_start_time
        self.state = self.do_simulation()

        self.start = self.simulation_start_time
        self.stop = self.start + self.tau
        self.done = self._is_done()
        return self.state


class FMI1CSEnv(ModelicaCSEnv):
    """
    Wrapper class.
    Should be used as a superclass for all environments using FMU exported in co-simulation mode,
    FMI standard version 1.0.
    Abstract logic is implemented in parent classes.

    Refer to the ModelicaBaseEnv docs for detailed instructions on own environment implementation.
    """

    def __init__(self, model_path, config, log_level, simulation_start_time=0):
        super(FMI1CSEnv,self).__init__(model_path, config, FMIStandardVersion.first, log_level,
                         simulation_start_time=simulation_start_time)


class FMI2CSEnv(ModelicaCSEnv):
    """
    Wrapper class.
    Should be used as a superclass for all environments using FMU exported in co-simulation mode.
    FMI standard version 2.0.
    Abstract logic is implemented in parent classes.

    Refer to the ModelicaBaseEnv docs for detailed instructions on own environment implementation.
    """
    def __init__(self, model_path, config, log_level, simulation_start_time=0):
        super(FMI2CSEnv,self).__init__(model_path, config, FMIStandardVersion.second, log_level,
                         simulation_start_time=simulation_start_time)
