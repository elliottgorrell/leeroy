from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import warnings

from rasa_core import utils
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.events import SlotSet
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.memoization import MemoizationPolicy

logger = logging.getLogger(__name__)

def train_dialogue(domain_file="domain.yml",
                   model_path="models/nlu",
                   training_data_file="data/training/stories.md"):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy()])

    agent.train(
            training_data_file,
            max_history=3,
            epochs=400,
            batch_size=100,
            validation_split=0.2
    )

    agent.persist(model_path)
    return agent


def run(serve_forever=True):
    print("Loading agent...")
    interpreter = RasaNLUInterpreter("models/nlu/default/current")
    agent = Agent.load("", interpreter=interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")

    parser = argparse.ArgumentParser(
            description='starts the bot')

    parser.add_argument(
            'task',
            choices=["train-dialogue", "run"],
            help="what the bot should do - e.g. run or train?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "train-dialogue":
        train_dialogue()
    elif task == "run":
        run()
    else:
        warnings.warn("Need to pass either 'train-dialogue' or 'run' to use the script.")
        exit(1)
