var fs  = require("fs");

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {       
        line = line.replace(/\r/gm, ""); // For Windows.

        var result_string = "";

        for (var i = 0; i < line.length; i++) {
            if (line[i] == line[i].toUpperCase()) {
                result_string += line[i].toLowerCase();
            }
            else if (line[i] == line[i].toLowerCase()) {
                result_string += line[i].toUpperCase();
            }
            else {
                result_string += line[i];
            }
        }

        console.log(result_string);
    }
});