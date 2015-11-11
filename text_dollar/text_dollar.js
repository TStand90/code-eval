var fs  = require("fs");

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {
        var dollarAmount = parseInt(line.replace(/\r/gm, ""));

        var textAmount = '';

        if (dollarAmount == 0) {
            console.log('ZeroDollar');
        }
        else {
            textAmount += get_billion(dollarAmount);
            textAmount += get_million(dollarAmount);
            textAmount += get_thousands(dollarAmount);
            textAmount += get_hundreds(dollarAmount);

            if (textAmount) {
                console.log(textAmount + 'Dollars');
            }
        }
    }
});

function get_billion(amount) {
    var billionAmount = get_string_of_number(Math.floor(amount / 1000000000));

    if (billionAmount) {
        return billionAmount + 'Billion';
    }
    else {
        return billionAmount;
    }
}

function get_million(amount) {
    var millionAmount = '';

    var hundredsPlace = Math.floor(amount / 100000000);
    var tensPlace = Math.floor((amount / 1000000) % 100);
    var onesPlace = Math.floor(amount / 1000000);

    millionAmount += get_hundreds_place(hundredsPlace);
    millionAmount += get_tens_place(tensPlace);

    if (tensPlace > 19 || tensPlace < 10) {
        millionAmount += get_ones_place(onesPlace);
    }

    if (millionAmount) {
        millionAmount += 'Million';
    }

    return millionAmount;
}

function get_thousands(amount) {
    var thousandsAmount = '';

    var hundredsPlace = Math.floor(amount / 100000);
    var tensPlace = Math.floor((amount / 1000) % 100);
    var onesPlace = Math.floor(amount / 1000);

    thousandsAmount += get_hundreds_place(hundredsPlace);
    thousandsAmount += get_tens_place(tensPlace);

    if (tensPlace > 19 || tensPlace < 10) {
        thousandsAmount += get_ones_place(onesPlace);
    }

    if (thousandsAmount) {
        thousandsAmount += 'Thousand';
    }

    return thousandsAmount;
}

function get_hundreds(amount) {
    var hundredsAmount = '';

    var hundredsPlace = Math.floor(amount / 100);
    var tensPlace = Math.floor(amount % 100);
    var onesPlace = amount;

    hundredsAmount += get_hundreds_place(hundredsPlace);
    hundredsAmount += get_tens_place(tensPlace);

    if (tensPlace > 19 || tensPlace < 10) {
        hundredsAmount += get_ones_place(onesPlace);
    }

    return hundredsAmount;
}

function get_ones_place(number) {
    return get_string_of_number(number);
}

function get_tens_place(number) {
    return get_tens_string_of_number(number);
}

function get_hundreds_place(number) {
    var numberString = get_string_of_number(number);

    if (numberString) {
        return numberString + 'Hundred';
    }
    else {
        return '';
    }
}

function get_string_of_number(number) {
    if ((number % 10) == 1) {
        return 'One';
    }
    else if ((number % 10) == 2) {
        return 'Two';
    }
    else if ((number % 10) == 3) {
        return 'Three';
    }
    else if ((number % 10) == 4) {
        return 'Four';
    }
    else if ((number % 10) == 5) {
        return 'Five';
    }
    else if ((number % 10) == 6) {
        return 'Six';
    }
    else if ((number % 10) == 7) {
        return 'Seven';
    }
    else if ((number % 10) == 8) {
        return 'Eight';
    }
    else if ((number % 10) == 9) {
        return 'Nine';
    }
    else {
        return '';
    }
}

function get_tens_string_of_number(number) {
    if (number == 10) {
        return 'Ten';
    }
    else if (number == 11) {
        return 'Eleven';
    }
    else if (number == 12) {
        return 'Twelve';
    }
    else if (number == 13) {
        return 'Thirteen';
    }
    else if (number == 14) {
        return 'Fourteen';
    }
    else if (number == 15) {
        return 'Fifteen';
    }
    else if (number == 16) {
        return 'Sixteen';
    }
    else if (number == 17) {
        return 'Seventeen';
    }
    else if (number == 18) {
        return 'Eighteen';
    }
    else if (number == 19) {
        return 'Nineteen';
    }
    else if ((Math.floor(number / 10) % 10) == 2) {
        return 'Twenty';
    }
    else if ((Math.floor(number / 10) % 10) == 3) {
        return 'Thirty';
    }
    else if ((Math.floor(number / 10) % 10) == 4) {
        return 'Forty';
    }
    else if ((Math.floor(number / 10) % 10) == 5) {
        return 'Fifty';
    }
    else if ((Math.floor(number / 10) % 10) == 6) {
        return 'Sixty';
    }
    else if ((Math.floor(number / 10) % 10) == 7) {
        return 'Seventy';
    }
    else if ((Math.floor(number / 10) % 10) == 8) {
        return 'Eighty';
    }
    else if ((Math.floor(number / 10) % 10) == 9) {
        return 'Ninety';
    }
    else {
        return '';
    }
}