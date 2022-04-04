export const dataProvider = {
    get: (url, data) => {
        let sendUrl = `${url}?`;
        let firstElement = true;

        for (let i in data) {
            sendUrl += firstElement ? `${i}=${data[i]}` : `&${i}=${data[i]}`
            firstElement = false
        }

        return fetch(sendUrl)
            .then(response => {
                if (response.status < 200 || response.status >= 300) {
                    throw new Error(response.statusText);
                }
                return response.json();
            })
            .catch(err => {
                return false
            });
    },
    post: (url, data) => {
        const request = new Request(`${url}/`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json;charset=utf-8'},
            body: JSON.stringify(data)
        });
        return fetch(request)
            .then(response => {
                if (response.status < 200 || response.status >= 300) {
                    throw new Error(response.statusText);
                }
                return response.json();
            })
            .catch(error => console.log(error))
    },
}