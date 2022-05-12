

export const utilities = {
    // формируем карточку билета
    ticketCard: (item) => {
        let data = {
            id: item.id,
            validatingAirlineCodes: item.validatingAirlineCodes[0],
            itineraries: item.itineraries,
            numberOfBookableSeats: item.numberOfBookableSeats,
            total: item.price.total,
            grandTotal: item.price.grandTotal,

        }
       const itineraries = utilities.itineraries(data)

        return `
            <div key=${item.id} class="ticketCardContent">
                <div class="ticketCardLeftColumn">
                    <div class="ticketCardPrice">${data.grandTotal} Р</div>
                </div>
                <div class="ticketCardCentralColumn">
                    ${itineraries}
                </div>
                <div class="ticketCardRightColumn">
                    <div class="ticketCardRightColumnElement">
                        <div>
                            <img title="Сохранить запрос" type="saveRequest" key="${item.id}" src="static/img/bell.png">
                        </div>
                        <input type="button" value="Купить">
                    </div>
                </div>
               
            </div>
        `;
        // numberOfBookableSeats - Количество мест для бронирования
    },
    itineraries: (data) => {
    let itinerariesItem= ""

    // формиируем рейсы
        if (Array.isArray(data.itineraries)){
            data.itineraries.forEach(itemItineraries => {
                itinerariesItem += `
                <div class="ticketCardCompanyItineraries">
                    <div class="ticketCardCompany">
                        <div>${data.validatingAirlineCodes}</div>
                        <div>Мест ${data.numberOfBookableSeats}</div>
                    </div>

                    <div class="ticketCardInformationFlight">
                        <div>${utilities.getStartTime(itemItineraries.segments)}</div>
                        <div class="ticketCardRoute">
                            <div>В пути ${utilities.durationParser(itemItineraries.duration)}</div>
                            <hr>
                            <div>
                                <div>Пересадок ${itemItineraries.segments.length - 1}</div>
                            </div>
                        </div>
                        <div>${utilities.getEndTime(itemItineraries.segments)}</div>
                    </div>
                </div>
                `
            })
        }

     return itinerariesItem;
    },
    dataCard: (item) => {
        return {
            id: item.id,
            validatingAirlineCodes: item.validatingAirlineCodes[0],
            duration: utilities.durationParser(item.itineraries[0].duration),
            segmentsLength: item.itineraries[0].segments.length - 1,
            segments: item.itineraries[0].segments,
            startTime: utilities.getStartTime(item.itineraries[0].segments),
            endTime: utilities.getEndTime(item.itineraries[0].segments),
            numberOfBookableSeats: item.numberOfBookableSeats,
            total: item.price.total,
            grandTotal: item.price.grandTotal,
        }
    },
    listData: (args) => {
        const {
            data
        } = args
        const itemData = {};

        if (Array.isArray(data)) {
            data.forEach(item => {
                itemData[item.id] = utilities.dataCard(item);
            })
            return itemData
        }
    },
    listCard: (args, listCard) => {
        const {
            data
        } = args

        let list = ""
        if (Array.isArray(data)) {
            data.forEach(item => {
                list += `<div class=${listCard}>${utilities.ticketCard(item)}</div>`
            })
            return list
        }
    },
    durationParser: (duration) => {
        let time = duration
        time = time.replace('PT', '')
        time = time.replace('H', 'ч ')
        time = time.replace('M', 'м')
        return time
    },
    getDateTime: (datetime) => {
        let data = datetime.split('T');
        return `<p>${data[0]}</p><p>${data[1]}</p>`
    },
    getStartTime: (segments) => {return utilities.getDateTime(segments[0].departure.at)},
    getEndTime: (segments) => {
    return utilities.getDateTime(segments[segments.length - 1].arrival.at);
    }
}