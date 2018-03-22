const fs = require ("fs");
const path = require ("path");
const chatito = require ("chatito");

const trainingDataDir = "../leeroy/data/training/nlu/"


let chatitoIntents = fs.readdirSync("./intents").filter( filename => {
  const fileExtension = filename.split(".")[1]
  if (fileExtension == "chatito" ) { return true ; }
});

chatitoIntents.forEach(filename => {
  const chatitoGrammar = fs.readFileSync("./intents/" + filename, "utf8");
  const dataset = chatito.datasetFromString(chatitoGrammar);

  const rasaDataset = JSON.stringify( { "rasa_nlu_data" : { "common_examples" : dataset } }, null, 2);

  fs.writeFileSync(trainingDataDir + filename.split(".")[0] + ".json", rasaDataset);
})
