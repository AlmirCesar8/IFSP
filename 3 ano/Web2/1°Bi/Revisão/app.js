'use strict';

const switcher = document.querySelector('.btn');
switcher.addEventListener('click', function () {
    document.body.classList.toggle('dark-theme');

    var isDarkTheme = document.body.classList.contains('dark-theme'); // Verifica se a classe está presente
    if (isDarkTheme) {
        this.textContent = "Light Mode";
    } else {
        this.textContent = "Dark Mode";
    }

    console.log('current class name: ' + document.body.className);
});