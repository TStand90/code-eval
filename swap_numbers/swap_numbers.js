var fs  = require("fs");

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {
        line = line.replace(/\r/gm, ""); // For Windows.

        var words = line.split(" "); // Splits the string by space
        var newWords = [];

        for (var i = 0; i < words.length; i++) {
            var word = words[i][words[i].length-1];
            word += words[i].slice(1, words[i].length-1);
            word += words[i][0];
            newWords.push(word);
        }

        console.log(newWords.join(' '));
    }
});