const fs = require('fs');
const chatito = require("chatito");

var dslDefinitionString = fs.readFileSync('chat.dsl', 'utf8');

var dataset = chatito.datasetFromString(dslDefinitionString);
var datasetString = JSON.stringify(dataset,null,2);

fs.writeFile('training_data.json', datasetString, (err) => {
    if (err)
        return console.log(err);
});
