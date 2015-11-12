var fs  = require("fs");

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {
        var amount = parseInt(line.replace(/\r/gm, ""));
        var numberOfCoins = 0;

        numberOfCoins += get_coins(amount, 5);
        amount = get_remaining_coins(amount, 5);

        numberOfCoins += get_coins(amount, 3);
        amount = get_remaining_coins(amount, 3);

        numberOfCoins += amount;

        console.log(numberOfCoins);
    }
});

function get_coins(amount, value) {
    return Math.floor(amount/value);
}

function get_remaining_coins(amount, remaining) {
    return amount % remaining;
}