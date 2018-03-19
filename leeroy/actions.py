from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet


class ActionCheckOpenHouses(Action):
    def name(self):
        return 'action_check_open_houses'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("No Open Houses implementation yet")
        return []
