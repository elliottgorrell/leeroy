## Greeting
* greeting
   - utter_greet

## User asks for open houses
* checkOpenHouses
  - action_check_open_houses

## User wants to know what bot can do
* listActions
  - utter_what_I_can_do

## User says goodby
* farewell
  - utter_goodbye

## Master tries to tricks us
* wtf
  - utter_default

## Generated Story -6774732796759264827
* greeting
    - utter_greet
* listActions
    - utter_what_I_can_do
    - utter_what_I_can_do
* wtf
    - utter_default
* checkOpenHouses{"when": "today"}
    - slot{"when": "today"}
    - action_check_open_houses
* checkProperties
* checkProperties
* wtf
    - utter_default
    - export
