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


            let keys;
            //check if data is empty
            if (data.message == "No data in table") {
                keys = data.keys;
                currTableKeys = keys;
            } else {
                keys = JSON.stringify(Object.keys(data[0]));
                keys = keys.replace(/[\[\]"]+/g, '');
                keys = keys.split(',');
                currTableKeys = keys;
            }
            //update search bar with the new keys

            const find_table = document.getElementById('find_table');
            find_table.innerHTML = '';
            find_table.appendChild(document.createElement('tr'));
            keys.forEach(key => {
                find_table.lastChild.appendChild(document.createElement('th'));
                find_table.lastChild.lastChild.appendChild(document.createElement('input'));
                find_table.lastChild.lastChild.lastChild.setAttribute('type', 'text');
                find_table.lastChild.lastChild.lastChild.setAttribute('placeholder', key);
                find_table.lastChild.lastChild.lastChild.setAttribute('name', key);
            }
            );
            find_table.lastChild.appendChild(document.createElement('th'));
            find_table.lastChild.lastChild.appendChild(document.createElement('button'));
            find_table.lastChild.lastChild.lastChild.innerHTML = "Find";
            find_table.lastChild.lastChild.lastChild.setAttribute('onclick', `filter('${table}')`);

            // update the content table headers with the new keys and 
            //fill the table with the  data

            const tableDataElem = document.getElementById('table-data');
            tableDataElem.innerHTML = '';
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
            console.log(table);
            if (table == "students_dormitory" || table == "students_major" || table == "university_major") {

            }
            else {

                currTableKeys.forEach(key => {
                    if (key == "id" || key == "student_count" || key == "join_date" || key == "semester") return;
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
            }
            break;
        case "delete":
            form.appendChild(document.createElement('label'));
            form.lastChild.innerHTML = "id";
            form.appendChild(document.createElement('input'));
            form.lastChild.setAttribute('name', 'id');
            form.lastChild.setAttribute('type', 'text');
            form.lastChild.setAttribute('placeholder', 'id');
            form.appendChild(document.createElement('button'));
            form.lastChild.innerHTML = "Delete";
            form.lastChild.setAttribute('onclick', `deleteElement('${table}')`);
            break;
        case "update":
            currTableKeys.forEach(key => {
                if (key == "student_count" || key == "join_date") return;
                form.appendChild(document.createElement('label'));
                form.lastChild.innerHTML = key;
                form.appendChild(document.createElement('input'));
                form.lastChild.setAttribute('name', key);
                form.lastChild.setAttribute('type', 'text');
                form.lastChild.setAttribute('placeholder', key);
            });
            form.appendChild(document.createElement('button'));
            form.lastChild.innerHTML = "Update";
            form.lastChild.setAttribute('onclick', `updateElement('${table}')`);
            break;
        default:
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
            console.log(response);
            closeModal();
            getTable(table);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function deleteElement(table) {
    let form = document.getElementById('input_form');
    fetch(`/api/${table}/${form["id"].value}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => response.json())
        .then(() => {

            if (response.status == 404) alert(data.message)
            closeModal();
            getTable(table);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function updateElement(table) {
    let form = document.getElementById('input_form');
    let data = {};
    currTableKeys.forEach(key => {
        if (key == "student_count" || key == "join_date" || key == "semester" || key == "leave_date") return;
        if (form[key].value != "") data[key] = form[key].value;;
    });
    fetch(`/api/${table}/${form["id"].value}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            if (response.status == 404) alert(data.message)
            closeModal();
            getTable(table);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function filter(table) {
    let form_table = document.getElementById('find_table');
    let data = {};

    form_table.childNodes[0].childNodes.forEach(node => {
        if (node.childNodes[0].value != "") data[node.childNodes[0].name] = node.childNodes[0].value;
    });
    if (Object.keys(data).length == 0) {
        getTable(table);
        return;
    }
    let quary = new URLSearchParams(data).toString();
    fetch(`/api/q${table}?${quary}`,
        {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        }
    )
        .then(response => response.json())
        .then(data => {
            const tableDataElem = document.getElementById('table-data');
            tableDataElem.innerHTML = '';
            tableDataElem.appendChild(document.createElement('tr'));
            currTableKeys.forEach(key => {
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
                currTableKeys.forEach(key => {
                    tableDataElem.lastChild.appendChild(document.createElement('td'));
                    tableDataElem.lastChild.lastChild.innerHTML = row[key];
                });
            });
        }
        )

}

