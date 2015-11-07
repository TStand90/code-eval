var fs  = require("fs");

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {
        line = line.replace(/\r/gm, ""); // For Windows.

        var arr = line.split(" "); // Splits the string by space

        var capitalizedWords = [];

        for (var i = 0; i < arr.length; i++) {
            var currentWord = arr[i];
            var newWord = ""
            for (var x = 0; x < currentWord.length; x++) {
                if (x == 0) {
                    newWord += currentWord[x].toUpperCase();
                }
                else {
                    newWord += currentWord[x];
                }
            }
            capitalizedWords.push(newWord);
        }

        console.log(capitalizedWords.join(' '));
    }
});