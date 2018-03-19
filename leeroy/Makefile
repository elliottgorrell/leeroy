
run:
	python3 -m rasa_core.run -d models/policy/current -u models/nlu/current

train-nlu:
	python3 -m rasa_nlu.train -c nlu_model_config.json --fixed_model_name current

train-dialogue:
	python3 bot.py train-dialogue

