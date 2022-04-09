import {dataProvider} from "./dataProvider.js";

const listeningInputs =
    {
        fromCity: 'fromCity',
        toCity: 'toCity'
    };
const dataForm = {}
let timer;

window.onload = function () {
    const selectAllInputs = document.querySelectorAll('div > input');
    const inputSubmit = document.getElementById('formSearch');

    // добавляем обработчик событий на input
    selectAllInputs.forEach(item => {
        if (item.name === listeningInputs[item.name])
            item.addEventListener('input', (e) => handlerSelectInput(e));
        item.addEventListener('input', (e) => handlerInput(e));
    })
    inputSubmit.addEventListener('submit', (e) => handlerSubmit(e));
}

// обработчик ввода данных из input
const handlerInput = (e) => {
    dataForm[e.target.name] = e.target.value;
}

// обработка input type text
const handlerSelectInput = (e) => {
    const data = {};
    const url = `${document.location.origin}/airports_by_term`;
    const nameInput = e.target.name;
    clearTimeout(timer);
    data['term'] = e.target.value;
    // отправляем данные методом get

    timer = setTimeout(() => {
        const request = dataProvider.get(url, data);
        request
            .then(res => console.log(res))
    }, 2000)
}

// обработчик отправки данных из формы
const handlerSubmit = (e) => {
    e.preventDefault()
    clearTimeout(timer);
    const url = document.location.origin;
    const request = dataProvider.get(url, dataForm);
    request
        .then(res => console.log(res))
}
