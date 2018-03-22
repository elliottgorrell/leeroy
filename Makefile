generate-training-data:
	cd 01_generate_training_data &&	npm install &&	npm start

run:
	cd leeroy && python3 -W ignore::DeprecationWarning bot.py run

train-nlu:
	cd leeroy && python3 -m rasa_nlu.train -c nlu_model_config.json --fixed_model_name current

train-dialogue:
	cd leeroy && python3 bot.py train-dialogue

interactive-story-training:
	cd leeroy && python3 interactive_training.py
