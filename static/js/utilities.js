export const utilities = {
    // формируем карточку билета
    ticketCard: (item) => {
        let data = {
            id: item.id,
            validatingAirlineCodes: item.validatingAirlineCodes[0],
            duration: utilities.durationParser(item.itineraries[0].duration),
            segmentsLength: item.itineraries[0].segments.length,
            segments: item.itineraries[0].segments,
            startTime: utilities.getStartTime(item.itineraries[0].segments),
            endTime: utilities.getStartTime(item.itineraries[0].segments),
            numberOfBookableSeats: item.numberOfBookableSeats,
            total: item.price.total,
            grandTotal: item.price.grandTotal,

        }
        let itemDiv = `
            <div key=${item.id} class="ticketCardContent">
                <div class="ticketCardLeftColumn">
                    <div class="ticketCardPrice">${data.grandTotal} Р</div>
                </div>
                <div class="ticketCardRightColumn">
                    <div class="ticketCardCompany">
                        <div>${data.validatingAirlineCodes}</div>
                        <div>Мест ${data.numberOfBookableSeats}</div>
                    </div>
                    <div class="ticketCardInformationFlight">
                        <div>${data.startTime}</div>
                        <div class="ticketCardRoute">
                            <div>В пути ${data.duration}</div>
                            <hr>
                            <div>
                                <div>Пересадок ${data.segmentsLength}</div>
                            </div>
                        </div>
                        <div>${data.endTime}</div>
                    </div>
             
                </div>
               
            </div>
        `;
        // numberOfBookableSeats - Количество мест для бронирования

        return itemDiv
    },
    listCard: (args, listCard) => {
        const {
            data,
        } = args
        console.log(args)
        let list = ""
        data.forEach(item => {
            list += `<div class=${listCard}>${utilities.ticketCard(item)}</div>`
        })
        return list
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
    getStartTime(segments) {
        return utilities.getDateTime(segments[0].departure.at)
    },
    getEndTime(segments) {
        let dateTime = '';
        segments.forEach(item => {
            dateTime = utilities.getDateTime(item.arrival.at);
        })
        return dateTime;
    }
}