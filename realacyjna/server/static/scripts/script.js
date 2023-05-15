currTableKeys = [];
function getTable(table) {
    fetch(`/api/${table}`)
        .then(response => response.json())
        .then(data => {
            // update the table data placeholder with the new data
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
            let keys;
            //check if data is empty
            if (data.message == "No data in table") {
                console.log("you are in if loop");
                console.log(data.keys);
                keys = data.keys;
                currTableKeys = keys;
            } else {
                console.log("you are in else loop");
                console.log(data[0]);
                keys = JSON.stringify(Object.keys(data[0]));
                keys = keys.replace(/[\[\]"]+/g, '');
                keys = keys.split(',');
                currTableKeys = keys;
            }
            tableDataElem.appendChild(document.createElement('tr'));

            keys.forEach(key => {
                tableDataElem.lastChild.appendChild(document.createElement('th'));
                tableDataElem.lastChild.lastChild.innerHTML = key;
            });

            if (data.message == "No data in table") {
                tableDataElem.appendChild(document.createElement('tr'));
                tableDataElem.lastChild.appendChild(document.createElement('td'));
                tableDataElem.lastChild.lastChild.innerHTML = "No data in table";
                
                return;
            };
            data.forEach(row => {
                tableDataElem.appendChild(document.createElement('tr'));
                keys.forEach(key => {
                    tableDataElem.lastChild.appendChild(document.createElement('td'));
                    tableDataElem.lastChild.lastChild.innerHTML = row[key];
                });
            });

        })
        .catch(error => console.error(error));
}

function openModal(action, table) {
    let dialog = document.querySelector('dialog');
    let form = document.getElementById('input_form');
    form.innerHTML = '';
    switch (action) {
        case "create":
            currTableKeys.forEach(key => {
                if (key == "id" || key == "student_count" || key == "join_date" || key == "semester" || key == "leave_date") return;
                form.appendChild(document.createElement('label'));
                form.lastChild.innerHTML = key;
                form.appendChild(document.createElement('input'));
                form.lastChild.setAttribute('name', key);
                form.lastChild.setAttribute('type', 'text');
                form.lastChild.setAttribute('placeholder', key);
            });
            form.appendChild(document.createElement('button'));
            form.lastChild.innerHTML = "Create";
            form.lastChild.setAttribute('onclick', `createNew('${table}')`);
            break;
    }



    dialog.showModal();
}

function closeModal() {
    const dialog = document.querySelector('dialog');
    dialog.close();
}

function createNew(table) {
    let form = document.getElementById('input_form');
    let data = {};
    currTableKeys.forEach(key => {
        console.log(key);
        if (key == "id" || key == "student_count" || key == "join_date" || key == "semester" || key == "leave_date") return;
        data[key] = form[key].value;
    });
    fetch(`/api/${table}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            closeModal();
            getTable(table);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function deleteElement() {
    alert("deleteElement");
}

function updateElement() {
    alert("updateElement");
}