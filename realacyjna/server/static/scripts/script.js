function getTable(table) {
    fetch(`/api/${table}`)
        .then(response => response.json())
        .then(data => {
            // update the table data placeholder with the new data
            console.log(data);
            const nav_table = document.getElementById('nav_table');
            nav_table.innerHTML = '';
            
            let li = document.createElement('li');
            let btn = document.createElement('button');
            btn.innerHTML = "Create element";
            btn.setAttribute('onclick', `createNew('${table}')`);
            li.appendChild(btn);
            nav_table.appendChild(li);

            li = document.createElement('li');
            btn = document.createElement('button');
            btn.innerHTML = "Delete element";
            btn.setAttribute('onclick', `deleteElement('${table}')`);
            li.appendChild(btn);
            nav_table.appendChild(li);

            li = document.createElement('li');
            btn = document.createElement('button');
            btn.innerHTML = "Update element";
            btn.setAttribute('onclick', `updateElement('${table}')`);
            li.appendChild(btn);
            nav_table.appendChild(li);

            const tableDataElem = document.getElementById('table-data');
            tableDataElem.innerHTML = '';

            //check if data is empty
            if (data.length > 0) {
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
        }
        else {
            tableDataElem.innerHTML = "No data in table";
        }


        })
        .catch(error => console.error(error));
}

