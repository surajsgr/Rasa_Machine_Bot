from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
# from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

def train_nlu(data, configs, model_dir):
	training_data = load_data(data)
	trainer = Trainer(RasaNLUConfig(configs))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'machinenlu')
def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/machinenlu')
	print(interpreter.parse("what are the number of TASKI swingo 5000 seafreight machines?"))
if __name__ == '__main__':
	# train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
	run_nlu()