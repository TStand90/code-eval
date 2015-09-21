var fs  = require("fs");

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {
        line = line.replace(/\r/gm, ""); // For Windows.

        var age = parseInt(line);

        if (age >= 0 && age <= 2) {
            console.log("Still in Mama's arms");
        } else if (age >= 3 && age <= 4){
            console.log("Preschool Maniac");
        } else if (age >= 5 && age <= 11) {
            console.log("Elementary school");
        } else if (age >= 12 && age <= 14) {
            console.log("Middle school");
        } else if (age >= 15 && age <= 18) {
            console.log("High school");
        } else if (age >= 19 && age <= 22) {
            console.log("College");
        } else if (age >= 23 && age <= 65) {
            console.log("Working for the man");
        } else if (age >= 66 && age <= 100) {
            console.log("The Golden Years");
        } else {
            console.log("This program is for humans");
        }
    }
});