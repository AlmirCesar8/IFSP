var i = 0;
var x = 0;
var y = 0;

i = x = 100;
y = 200;

do {
    if (i % 19 == 0) {
        console.log("O primeiro número divisivel por 19");
        console.log("entre " + x + " e " + y + " = " + i);
        break;
    }
    i++;
} while (i<y);