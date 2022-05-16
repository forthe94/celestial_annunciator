export const authProvider = {
    // login: ({username, password}) => {
    //     let istToken = false
    //     const request = new Request(AUTH_URL, {
    //         method: 'POST',
    //         body: JSON.stringify({username, password}),
    //         headers: new Headers({'Content-Type': 'application/json'}),
    //     });
    //     return fetch(request)
    //         .then(response => {
    //             if (response.status < 200 || response.status >= 300) {
    //                 throw new Error(response.statusText);
    //             }
    //             return response.json();
    //         })
    //         .then(({id, token, groups, image, name}) => {
    //             groups.forEach(function (receivedItem) {
    //                 json.authGroups.forEach(function (jsonItem) {
    //                     if (jsonItem === receivedItem.name) {
    //                         localStorage.setItem('id', id);
    //                         localStorage.setItem('token', token);
    //                         localStorage.setItem('image', image);
    //                         localStorage.setItem('name', name);
    //                         istToken = true;
    //                     }
    //                 });
    //             });
    //             return istToken;
    //         })
    //         .catch(err => {
    //             return false
    //         });
    // },
    // checkError: ({status}) => {
    //     if (status === 401 || status === 403) {
    //         localStorage.removeItem('token');
    //         return false;
    //     }
    //     return true;
    // },
    checkAuth: () => {
        console.log(document.cookie.split(";"))
        // return document.cookies.get('sessionid')
        //     ? true
        //     : false;
    }
    // getPermissions: () => {
    //     return Promise.resolve();
    // },
    // logout: () => {
    //     return true;
    // },
}