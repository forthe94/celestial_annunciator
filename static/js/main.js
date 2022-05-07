import {dataProvider} from "./dataProvider.js";
import {utilities} from "./utilities.js";

const listeningInputs =
    {
        originLocationCode: 'originLocationCode',
        destinationLocationCode: 'destinationLocationCode'
    };
const dataForm = {}
let timer;
const secTimeOut = 1;
let dataCard = [];

window.onload = function () {
    let arrayCity = '';
    const selectAllInputs = document.querySelectorAll('div > input');
    const inputSubmit = document.getElementById('formSearch');
    const outputSearch = document.getElementById('outputSearch');


    // вешаем проверку на нажатие в не области контестного меню, чтобы его отключить
    document.querySelector('body').addEventListener('click', (e) => checkingContextMenuClick(e));

    // добавляем обработчик событий на input
    selectAllInputs.forEach(item => {
        if (item.name === listeningInputs[item.name])
            item.addEventListener('input', (e) => handlerSelectInput(e));
        item.addEventListener('input', (e) => handlerInput(e));
    })
    inputSubmit.addEventListener('submit', (e) => handlerSubmit(e));

    // обработчик ввода данных из input
    const handlerInput = (e) => {
        if(e.target.type === 'text'){
            dataForm[e.target.name] = e.target.getAttribute('code');
        }
        else
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
                .then(res => {
                    contextMenuInput(e, res);
                    if(res.length)
                        document.getElementById(e.target.name).style.display = "flex"
                })
        }, secTimeOut*1000)
    }

    // обработчик отправки данных из формы
    const handlerSubmit = (e) => {
        e.preventDefault()
        clearTimeout(timer);
        const url = `${document.location.origin}/flight_search`;
        const request = dataProvider.get(url, dataForm);
        request
            .then(res => {
                //заносим данные в именнованный массив
                dataCard  = utilities.listData(res);
                //добавляем список билетов на сайт
                outputSearch.innerHTML = utilities.listCard( res, 'listCard');
                return true
            })
            .then(res => {
                const imgSave = document.querySelectorAll("img[type='saveRequest']")
                imgSave.forEach(item => {
                    item.addEventListener("click", (e)=>{
                        const url = `${document.location.origin}/save_search`;
                        const itemData = dataCard[e.target.getAttribute('key')];
                        const request = dataProvider.get(url,itemData);
                        request.then(res => {
                            console.log(res)
                        })
                    })
                })
            })
    }

    // Формирование контекстного меню
    const contextMenuInput = (e, res) => {
        let contextList = "";
        let contexMenu = "";

        const divContextMenu = document.getElementById(e.target.name);
        if (res.length) {
            res.forEach(i => {
                contextList += `<li code=${i['code']}>${i['name']}</li>`;
            })
            contexMenu = `<ul>${contextList}</ul>`;
            divContextMenu.innerHTML = contexMenu;
            let liList = document.querySelectorAll("li[code]")
            liList.forEach(i => i.addEventListener('click', (event) => handlerSelectContextMenu(e, event.target)))
        }
        if (res.length === 1) {
            let liItem = document.querySelector("li[code]");
            handlerSelectContextMenu(e, liItem);
        }
    }

    // обработчик выбора вариантов из меню
    const handlerSelectContextMenu = (e, item) => {
        e.target.value = item.innerHTML;
        e.target.setAttribute("code", item.getAttribute('code'));
        dataForm[e.target.name] = item.getAttribute('code');

        document.getElementById(e.target.name).style.display = "none"
    }

    // отключаем все контекстные меню
    const checkingContextMenuClick = (e) => {
        for( let i in listeningInputs)
            document.getElementById(i).style.display = "none"
    }
}