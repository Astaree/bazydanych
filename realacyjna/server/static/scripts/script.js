currTableKeys = [];

function createElement(tag, attributes = {}, innerHTML = '') {
    const element = document.createElement(tag);
    for (let attr in attributes) {
        element.setAttribute(attr, attributes[attr]);
    }
    element.innerHTML = innerHTML;
    return element;
}

async function getTable(table) {
    try {
        const response = await fetch(`/api/${table}`);
        const data = await response.json();

        const find_table = document.getElementById('find_table');
        const nav_table = document.getElementById('nav_table');
        const tableDataElem = document.getElementById('table-data');

        find_table.innerHTML = '';
        nav_table.innerHTML = '';
        tableDataElem.innerHTML = '';

        const createButton = createElement('button', {
            onclick: `openModal("create", '${table}')`
        }, 'Create element');
        const deleteButton = createElement('button', {
            onclick: `openModal("delete", '${table}')`
        }, 'Delete element');
        const updateButton = createElement('button', {
            onclick: `openModal("update", '${table}')`
        }, 'Update element');

        nav_table.append(createElement('li', {}, createButton.outerHTML));
        nav_table.append(createElement('li', {}, deleteButton.outerHTML));
        nav_table.append(createElement('li', {}, updateButton.outerHTML));

        let keys = [];
        let hasData = true;

        if (data.message === "No data in table") {
            keys = data.keys;
            currTableKeys = keys;
        } else {
            keys = Object.keys(data[0]);
            currTableKeys = keys;
        }

        if (table !== "students_major" && table !== "students_dormitory") {
            keys.forEach(key => {
                const input = createElement('input', {
                    type: 'text',
                    placeholder: key,
                    name: key
                });
                find_table.append(createElement('th', {}, input.outerHTML));
            });

            const findButton = createElement('button', {
                onclick: `filter('${table}')`
            }, 'Find');
            find_table.append(createElement('th', {}, findButton.outerHTML));
        }

        if (data.message === "No data in table") {
            tableDataElem.append(createElement('tr'));
            const noDataCell = createElement('td', {}, 'No data in table');
            tableDataElem.lastChild.append(noDataCell);
            return;
        }

        if (table !== "students_major" && table !== "students_dormitory") {
            keys.forEach(key => {
                tableDataElem.append(createElement('th', {}, key));
            });

            data.forEach(row => {
                const rowElement = createElement('tr');
                keys.forEach(key => {
                    const cell = createElement('td', {}, row[key]);
                    rowElement.append(cell);
                });
                tableDataElem.append(rowElement);
            });
        } else {
            const tableHead = createElement('thead', { id: 'table-head' });
            keys.forEach(key => {
                if (key === "id") return;
                if (key === "student_id" || key === "major_id" || key === "dormitory_id") {
                    const th = createElement('th', {}, key.split('_')[0]);
                    tableHead.append(th);
                } else {
                    const th = createElement('th', {}, key);
                    tableHead.append(th);
                }
            });
            tableDataElem.append(tableHead);

            for (const row of data) {
                const rowElement = createElement('tr');
                for (const key of keys) {
                    if (key === "student_id" || key === "major_id" || key === "dormitory_id") {
                        let id;
                        if (key === "student_id") {
                            id = row[key];
                            const studentResponse = await fetch(`/api/students/${id}`);
                            const studentData = await studentResponse.json();
                            const studentKeys = Object.keys(studentData).filter(k => {
                                return (
                                    k !== "date_of_birth" &&
                                    k !== "gender" &&
                                    k !== "join_date" &&
                                    k !== "semester"
                                );
                            });
                            studentKeys.forEach(studentKey => {
                                const cell = createElement('td', {}, studentData[studentKey]);
                                rowElement.append(cell);
                            });
                            const colspan = studentKeys.length;
                            document.getElementById('table-head').childNodes.forEach(node => {
                                if (node.innerHTML === "student") {
                                    node.setAttribute('colspan', colspan);
                                }
                            });
                        } else if (key === "major_id") {
                            id = row[key];
                            const majorResponse = await fetch(`/api/majors/${id}`);
                            const majorData = await majorResponse.json();
                            const majorKeys = Object.keys(majorData).filter(k => {
                                return (
                                    k !== "staff_id" &&
                                    k !== "university_id" &&
                                    k !== "office"
                                );
                            });
                            majorKeys.forEach(majorKey => {
                                const cell = createElement('td', {}, majorData[majorKey]);
                                rowElement.append(cell);
                            });
                            const colspan = majorKeys.length;
                            document.getElementById('table-head').childNodes.forEach(node => {
                                if (node.innerHTML === "major") {
                                    node.setAttribute('colspan', colspan);
                                }
                            });
                        } else if (key === "dormitory_id") {
                            id = row[key];
                            const dormitoryResponse = await fetch(`/api/dormitories/${id}`);
                            const dormitoryData = await dormitoryResponse.json();
                            const dormitoryKeys = Object.keys(dormitoryData).filter(k => {
                                return (
                                    k !== "occupancy" &&
                                    k !== "capacity" &&
                                    k !== "zip" &&
                                    k !== "state"
                                );
                            });
                            dormitoryKeys.forEach(dormitoryKey => {
                                const cell = createElement('td', {}, dormitoryData[dormitoryKey]);
                                rowElement.append(cell);
                            });
                            const colspan = dormitoryKeys.length;
                            document.getElementById('table-head').childNodes.forEach(node => {
                                if (node.innerHTML === "dormitory") {
                                    node.setAttribute('colspan', colspan);
                                }
                            });
                        }
                    }
                }
                tableDataElem.append(rowElement);
            }
        }
    } catch (error) {
        console.error(error);
    }
}


function openModal(action, table) {
    const dialog = document.querySelector('dialog');
    const form = document.getElementById('input_form');
    form.innerHTML = '';

    function createFormElement(type, attributes) {
        const element = document.createElement(type);
        Object.entries(attributes).forEach(([key, value]) => {
            element.setAttribute(key, value);
        });
        return element;
    }

    function createLabel(key) {
        const label = createFormElement('label', {});
        label.innerHTML = key;
        return label;
    }

    function createTextInput(name, placeholder) {
        const input = createFormElement('input', {
            type: 'text',
            name: name,
            placeholder: placeholder,
        });
        return input;
    }

    function createDropdownSelect(key, data) {
        const select = createFormElement('select', {
            id: `${key}_select`,
        });

        if (data.message == "No data in table") return select;

        const keys = Object.keys(data[0]);

        data.forEach(element => {
            let option = createFormElement('option', {});
            let elementFormat = keys
                .filter(k => k !== "id") // Exclude the "id" column from the display
                .map(k => `${k}: ${element[k]}`)
                .join(', ');
            option.innerHTML = elementFormat;
            select.appendChild(option);
        });

        return select;
    }

    function createButton(label, onclick) {
        const button = createFormElement('button', {
            onclick: onclick,
        });
        button.innerHTML = label;
        return button;
    }

    switch (action) {
        case "create":
            currTableKeys.forEach(key => {
                if (key == "id" || key == "student_count" || key == "join_date" || key == "semester") return;
                form.appendChild(createLabel(key));
                if (key != "staff_id" && key != "student_id" && key != "major_id" && key != "dormitory_id" && key != "university_id") {
                    form.appendChild(createTextInput(key, key));
                } else {
                    fetch(`/api/${key.split('_')[0]}`)
                        .then(response => response.json())
                        .then(data => {
                            form.appendChild(createDropdownSelect(key, data));
                        })
                        .catch(error => console.error(error));
                }
            });
            form.appendChild(createButton("Create", `createNew('${table}')`));
            break;

        case "delete":
            form.appendChild(createLabel("id"));
            form.appendChild(createTextInput("id", "id"));
            form.appendChild(createButton("Delete", `deleteElement('${table}')`));
            break;

        case "update":
            currTableKeys.forEach(key => {
                if (key == "student_count" || key == "join_date" || key == "semester" || key == "leave_date") return;
                form.appendChild(createLabel(key));
                if (key != "staff_id" && key != "student_id" && key != "major_id" && key != "dormitory_id" && key != "university_id") {
                    form.appendChild(createTextInput(key, key));
                } else {
                    fetch(`/api/${key.split('_')[0]}`)
                        .then(response => response.json())
                        .then(data => {
                            form.appendChild(createDropdownSelect(key, data));
                        })
                        .catch(error => console.error(error));
                }
            });
            form.appendChild(createButton("Update", `updateElement('${table}')`));
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
        if (key != "staff_id" && key != "student_id" && key != "major_id" && key != "dormitory_id" && key != "university_id") {
            data[key] = form[key].value;
        } else {
            data[key] = form[`${key}_select`].value.split(':')[1].trim().split(',')[0];
        }
    });
    console.log(data);
    fetch(`/api/${table}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
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
        if (key == "id" || key == "student_count" || key == "join_date" || key == "semester" || key == "leave_date") return;
        if (key != "staff_id" && key != "student_id" && key != "major_id" && key != "dormitory_id" && key != "university_id") {
            data[key] = form[key].value;
        } else {
            data[key] = form[`${key}_select`].value.split(':')[1].trim().split(',')[0];
        }
    });
    console.log(data);
    fetch(`/api/${table}/${form["id"].value}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => {
            response.json()
            console.log(data);
        })
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
    const formTable = document.getElementById('find_table');
    const data = {};
  
    const inputElements = formTable.querySelectorAll('input');
    inputElements.forEach(input => {
      if (input.value !== "") {
        data[input.name] = input.value;
      }
    });
  
    if (Object.keys(data).length === 0) {
      getTable(table);
      return;
    }
  
    const queryParams = new URLSearchParams(data).toString();
    const url = `/api/q${table}?${queryParams}`;
  
    fetch(url, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => response.json())
      .then(data => {
        const tableDataElem = document.getElementById('table-data');
        tableDataElem.innerHTML = '';
  
        if (data.message === "No data in table") {
          const rowElem = document.createElement('tr');
          const cellElem = document.createElement('td');
          cellElem.colSpan = currTableKeys.length;
          cellElem.innerHTML = "No data in table";
          rowElem.appendChild(cellElem);
          tableDataElem.appendChild(rowElem);
          return;
        }
  
        const headerRowElem = document.createElement('tr');
        currTableKeys.forEach(key => {
          const headerCellElem = document.createElement('th');
          headerCellElem.innerHTML = key;
          headerRowElem.appendChild(headerCellElem);
        });
        tableDataElem.appendChild(headerRowElem);
  
        data.forEach(row => {
          const rowElem = document.createElement('tr');
          currTableKeys.forEach(key => {
            const cellElem = document.createElement('td');
            cellElem.innerHTML = row[key];
            rowElem.appendChild(cellElem);
          });
          tableDataElem.appendChild(rowElem);
        });
      })
      .catch(error => console.error(error));
  }
  

