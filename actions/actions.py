# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from urllib import request
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests
import json
#
#
class ActionMeteo(Action):

    def name(self) -> Text:
        return "action_meteo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        r = requests.get(url='https://api.openweathermap.org/data/2.5/weather?lat=43.5894305&lon=13.4850167&appid=6686ada709b9b257d909aa5339fbf6c0')

        if r.status_code == 200:
            data=r.json()
            meteo = data['weather'][0]['main']
            descrizione = data['weather'][0]['description']
            temperatura = int(data['main']['temp'])-273
            output="Ho chiesto le condizioni metereologiche ad un mio amico inglese che sta all'università. Mi ha risposto così:'{}, {}'. La temperatura è di circa {} gradi centigradi.".format(meteo,descrizione,temperatura)
        else:
            output = "Non riesco a capire come sono ora le condizioni del meteo :("
        
        dispatcher.utter_message(text=output)
        
        return []