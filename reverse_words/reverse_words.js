var fs  = require("fs");

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {
        line = line.replace(/\r/gm, ""); // For Windows.

        var words = line.split(" "); // Splits the string by space
        var reversedWords = [];

        for (var i = words.length - 1; i >= 0; i--) {
            var word = words[i]
            reversedWords.push(word);
        }

        console.log(reversedWords.join(' '));
    }
});