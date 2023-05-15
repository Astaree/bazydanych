currTableKeys = [];
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
            btn.setAttribute('onclick', `openModal("create", '${table}')`);
            li.appendChild(btn);
            nav_table.appendChild(li);

            li = document.createElement('li');
            btn = document.createElement('button');
            btn.innerHTML = "Delete element";
            btn.setAttribute('onclick', `openModal("delete",'${table}')`);
            li.appendChild(btn);
            nav_table.appendChild(li);

            li = document.createElement('li');
            btn = document.createElement('button');
            btn.innerHTML = "Update element";
            btn.setAttribute('onclick', `openModal("update",'${table}')`);
            li.appendChild(btn);
            nav_table.appendChild(li);

            const tableDataElem = document.getElementById('table-data');
            tableDataElem.innerHTML = '';

            //check if data is empty
            if (data.length > 0) {
                let keys = JSON.stringify(Object.keys(data[0]));
                keys = keys.replace(/[\[\]"]+/g, '');
                keys = keys.split(',');
                currTableKeys = keys;
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

function openModal(action, table) {
    const dialog = document.querySelector('dialog');
    const form = document.getElementById('input-form');
    switch (action) {
        case "create":
            currTableKeys.forEach(key => {
                form.appendChild(document.createElement('label'));
                form.lastChild.innerHTML = key;
                form.appendChild(document.createElement('input'));
                form.lastChild.setAttribute('name', key);
            });
    }
    dialog.showModal();
}

function closeModal() {
    const dialog = document.querySelector('dialog');
    dialog.close();
}

function createNew() {

}

function deleteElement() {
    alert("deleteElement");
}

function updateElement() {
    alert("updateElement");
}