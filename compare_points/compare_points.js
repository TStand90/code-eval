var fs  = require("fs");

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {
        inputs = line.split(' ');

        var O = parseInt(inputs[0]);
        var P = parseInt(inputs[1]);
        var Q = parseInt(inputs[2]);
        var R = parseInt(inputs[3]);

        var north = false;
        var south = false;
        var east = false;
        var west = false;

        if (Q > O) {
            east = true; 
        } else if (Q < O) {
            west = true; 
        }

        if (P > R) {
            south = true;
        } else if (P < R) {
            north = true;
        }

        result = ""

        if (north) {
            result += "N";
        } else if (south) {
            result += "S";
        }

        if (east) {
            result += "E";
        } else if (west) {
            result += "W";
        }

        if (!result) {
            result = "here";
        }

        console.log(result);
    }
});
