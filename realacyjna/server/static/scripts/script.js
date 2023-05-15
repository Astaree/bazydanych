function getTable(table) {
    fetch(`/api/${table}`)
        .then(response => response.json())
        .then(data => {
            // update the table data placeholder with the new data
            const tableDataElem = document.getElementById('table-data');
            tableDataElem.innerHTML = '';
            
            let keys = JSON.stringify(Object.keys(data[0]));
            keys = keys.replace(/[\[\]"]+/g, '');
            keys = keys.split(',');
            tableDataElem.appendChild(document.createElement('tr'));

            keys.forEach(key => {
            tableDataElem.lastChild.appendChild(document.createElement('th'));
            tableDataElem.lastChild.lastChild.innerHTML = key;
            });

            data.forEach(row => {
                tableDataElem.appendChild(document.createElement('tr'));
                keys.forEach(key => {
                    tableDataElem.lastChild.appendChild(document.createElement('td'));
                    tableDataElem.lastChild.lastChild.innerHTML = row[key];
                });
            });


            console.log(keys);
            
        })
        .catch(error => console.error(error));
}


