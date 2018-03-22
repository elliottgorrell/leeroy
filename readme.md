## A Rasa NLU and Rasa CORE sample

I've setup this little demo to show a basic RASA setup and try and make it as easy to follow along for the team as possible to bootstrap your learning about this tool (The docs were great however all the components and terminology takes awhile to get your head around)

## Dependencies
You will need to have the following:

`Python`: I recommend using **Python3**, I had some problems when trying to run this using the python2.7 engine.

`Pip`: The python package manager, you will need this to install all the python packages required. (You will need pip3 if you are using python3.6)

`npm`: The NodePackageManager, used for installing javascript packages. Once you have this the only javascript pacakge used is **chatito** (for generating training data) will be installed automatically by pip

`make`: This is optional as this is just an easy way of exposing the main steps to be run in this project. I've just used a makefile which actually does nothing fancy except run a couple commands so you can always just copy paste them out. If you don't have make and you have a mac (http://osxdaily.com/2014/02/12/install-command-line-tools-mac-os-x/).

`RASA_NLU`: This is the rasa python library which acts a nice wrapper for creating a model for our bot. We will train this model, with its purpose being to take in unstructured input (natural language from a user) and extract out structured data that can be used to determine what a user wants. RASA NLU doesn't do the heavy lifting itself but allows you to plug in backend NLU libraries. I have gone with the recommended starting point which is [Spacy](https://spacy.io/).

`RASA_CORE`: This is a framework for designing dialog flow, creating a server which handles chat and responds to you and doing interactive training with your bot. It is made up of **yaml** and **markdown** files to structure the dialogueflow and then python classes are used for advanced actions.

`Spacy`: The chosen NLP backend framework. We will need to get this package and also download a "model" for it which are based on language, domain and size. You can get very large specialised models for training in certain situations.
Note: I originally tried to use the default small english package **en_core_web_sm** as when you run your training this model needs to be loaded and the smaller library loads about 10x faster. However was getting this weird error [[1]](#1.) so ended up using the rasa recommended **en_core_web_md**.

I won't list how to install the language compilers and package managers but feel free to slack me if you have trouble :). To install the project specific stuff - run the following:

```
pip3 install rasa_nlu
pip3 install spacy
python3 -m spacy download en_core_web_md
```


## Getting Started

### Generate training data
I haven't included any of the training data or models you will generate. Partly because it will make the git repo bigger and partly because it will make it clearer whats happening!

First of all we will use **chatito** which is a small tool for generating RASA training data. Inside `generate_training_data` is an intents folder which are some intents I have created using the chatito DSL (Domain specific language). Chatito will generate a bunch of sentences using the synonym placeholders and whether the word is optional. Check out https://github.com/rodrigopivi/Chatito for more info.

You can either run `node generateTrainingData.js` or use the makefile and run `make generate-training-data`. This will populate the `leeroy/data/training/nlu` with a bunch of json files that RASA will use to build a model

### Generate RASA NLU model
`make train-nlu` will get **rasa_nlu** to load out training data, load the Spacy backend and create a model which is what we will train the bot dialogue on. There will be a pretty big delay while the Spacy model is loaded then model creation begin.

The model creation will go through a few steps which can be seen in nlu_model_config.json in the **pipeline** object. I haven't looked too much into what each one does but for example **ner_crf** is used for identifying named entites such as people and places.

When it is finished you will have new content in `models/nlu/default/current`

### Create a dialogue policy
In rasa you construct hypothetical conversational flows using RASAs **story** format. It is a markdown file where you declare when an intent is picked up what the action form your bot should be, recording conversations means the flow of intents and actions is recordered and the more stories the better a policy that can be generated. At `data/training/story.md` you can see I have created one story for each intent and the action to perform for that intent (very simple). There is also one generated story from a small interactive training session I did with Leeroy.
Enough of this lets create the policy `make train-dialogue`.

### Lets do some interactive training
You can start up the bot and have a conversation where after every action Leeroy asks you to confirm if what happened was correct or not. If it wasn't you tell leeroy what he should of done or heard. When you are finished you can press `0` and append the story to the `data/training/stories.md` file

### you can also just spin him up and have a yarn
`make run` will get leeroy up and running so you can have a chat if you are lonely.



## TODO
[x] Create a package to generate training data using chatito  
[x] Write Readme and structure the project so it is easier to follow  
[] Train the bot so it can actually following dialogue  
[] Look into viability of incorporating in some models/stories/apis to automatically   solve mundane everyday chat like weather, time etc.  
[] Plug it into Slack (either using rasa_core or [Janis](janis.ai))  
[] Develop a decision matrix around rasa stack


## References


##### 1.
```
Traceback (most recent call last):
  File "/usr/local/Cellar/python/3.6.4_4/Frameworks/Python.framework/Versions/3.6/lib/python3.6/runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "/usr/local/Cellar/python/3.6.4_4/Frameworks/Python.framework/Versions/3.6/lib/python3.6/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/usr/local/lib/python3.6/site-packages/rasa_nlu/train.py", line 125, in <module>
    do_train(config)
  File "/usr/local/lib/python3.6/site-packages/rasa_nlu/train.py", line 114, in do_train
    interpreter = trainer.train(training_data)
  File "/usr/local/lib/python3.6/site-packages/rasa_nlu/model.py", line 157, in train
    updates = component.train(working_data, self.config, **context)
  File "/usr/local/lib/python3.6/site-packages/rasa_nlu/classifiers/sklearn_intent_classifier.py", line 94, in train
    X = np.stack([example.get("text_features") for example in training_data.intent_examples])
  File "/usr/local/lib/python3.6/site-packages/numpy/core/shape_base.py", line 353, in stack
    raise ValueError('all input arrays must have the same shape')
ValueError: all input arrays must have the same shape
make: *** [train-nlu] Error 1
```
