const fs = require('fs');
const chatito = require("chatito");

var dslDefinitionString = fs.readFileSync('dsl.json', 'utf8');

const dataset = chatito.datasetFromString(dslDefinitionString);

fs.writeFile('training_data.json', dataset, (err) => {
    if (err)
        return console.log(err);
});
