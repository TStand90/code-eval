var fs  = require("fs");

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {
        var line = parseInt(line.replace(/\r/gm, ""));

        var binaryString = (line >>> 0).toString(2);
        var numberOfOnes = 0;

        for (var eachChar = 0; eachChar < binaryString.length; eachChar++) {
            if (binaryString[eachChar] == '1') {
                numberOfOnes++;
            }
        }

        console.log(numberOfOnes);
    }
});