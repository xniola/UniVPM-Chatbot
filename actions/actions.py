# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionPianoStudiInformatica(Action):

    def name(self) -> Text:
        return "action_piano_studi_informatica"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=  "Ecco il piano di studi LM per Ingegneria Informatica e dell'Automazione!")
        dispatcher.utter_message(image= 'https://www.ingegneria.univpm.it/sites/www.ingegneria.univpm.it/files/ingegneria/guida_ingegneria/guida_2021_2022/pdf_270/IM12_LM_IA_20.pdf')
        
        return []
