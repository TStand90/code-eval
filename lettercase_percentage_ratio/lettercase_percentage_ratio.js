var fs  = require("fs");

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {
        line = line.replace(/\r/gm, ""); // For Windows.

        var lowercase_sum = 0;
        var uppercase_sum = 0;

        for (var i = 0; i < line.length; i++) {
            if (line[i] == line[i].toUpperCase()) {
                uppercase_sum++;
            }
            else {
                lowercase_sum++;
            }
        }

        var lowercase_percentage = ((lowercase_sum / line.length) * 100);
        var uppercase_percentage = ((uppercase_sum / line.length) * 100);

        lowercase_percentage = lowercase_percentage.toFixed(2);
        uppercase_percentage = uppercase_percentage.toFixed(2);

        console.log("lowercase: " + lowercase_percentage +
            " uppercase: " + uppercase_percentage);
    }
});