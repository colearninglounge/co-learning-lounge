from rasa.nlu.components import Component

class LocationExtractor(Component):
    """An API based location extractor component"""

    name = "location"
    provides = ["entities"]
    requires = []
    defaults = {}
    language_list = ["en"]
    print('initialised the class')

    def __init__(self, component_config=None):
        self.api_token = "c596f13460364db9915e6f3f98ffdac2"
        self.base_url = "https://api.dandelion.eu/datatxt/nex/v1/"
        self.min_confidence = 0.6
        super(LocationExtractor, self).__init__(component_config)

    def train(self, training_data, cfg, **kwargs):
        """Not needed, because it's done through API"""
        pass

    def convert_to_rasa(self, value):
        """Convert model output into the Rasa NLU compatible output format."""

        entity = {"value": value,
                  "entity": "location",
                  "extractor": "location_extractor"}

        return entity

    def process(self, message, **kwargs):
        """Retrieve the text message, pass it to the classifier
            and append the prediction results to the message class."""

        import requests

        list_cities = []
        params = {"token": self.api_token, "min_confidence": self.min_confidence}
        r = requests.get(self.base_url + "?text=" + message.text + "&include=types%2Cabstract%2Ccategories", params)
        all_locations = r.json()

        for x in all_locations["annotations"]:
            list_cities.append(x["label"])

        entity = self.convert_to_rasa(list_cities)

        message.set("entities", [entity], add_to_output=True)

    def persist(self, file_name, model_dir):
        """Pass because a pre-trained model is already persisted"""

        pass