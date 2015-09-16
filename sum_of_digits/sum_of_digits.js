var fs  = require("fs");

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {
        line = line.replace(/\r/gm, ""); // For Windows.

        sum_of_digits = 0;

        for (var i = 0; i < line.length; i++) {
            sum_of_digits += parseInt(line[i]);
        }

        console.log(sum_of_digits);
    }
});