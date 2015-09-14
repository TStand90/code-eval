var fs  = require("fs");

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {       
        line = line.replace(/\r/gm, ""); // For Windows.

        var arr = line.split(" "); // Splits the string by space

        var fizz = arr[0];
        var buzz = arr[1];
        var max = arr[2];

        fizzbuzz_string = ""

        for (var i = 1; i <= max; i++) {
            if (i % fizz == 0 && i % buzz == 0) {
                fizzbuzz_string += "FB";
            }
            else if (i % fizz == 0) {
                fizzbuzz_string += "F";
            }
            else if (i % buzz == 0) {
                fizzbuzz_string += "B";
            }
            else {
                fizzbuzz_string += i;
            }
            
            if (i != max) {
                fizzbuzz_string += " ";    
            }
        }

        console.log(fizzbuzz_string)
    }
});