function getValues(table, element_id) {
  var tableValue = "<ul>";
  var tableRef = document.getElementById(table);
  for (var i = 0, row; (row = tableRef.rows[i]); i++) {
    var rowValue = row.cells[0].innerHTML;
    tableValue += rowValue ? "<li>" + rowValue + "</li>" : "";
  }
  tableValue += "</ul>";
  document.getElementById(element_id).value = tableValue;
}

function getAllData() {
  getValues("ingredientTbl", "final_ingredients");
  getValues("stepsTbl", "final_steps");
}

function addValue(table, element_id) {
  // Get values that need to be save
  var element = document.getElementById(element_id).value;
  var stringValue = element ? element : " ";

  var tbodyRef = document
    .getElementById(table)
    .getElementsByTagName("tbody")[0];

  // Insert a row at the end of table
  var newRow = tbodyRef.insertRow(-1);

  // Insert a cell at the end of the row
  var newCell = newRow.insertCell(0);

  // Append a text node to the cell
  var newText = document.createTextNode(stringValue);
  newCell.appendChild(newText);

  newCell = newRow.insertCell(1);
  var newElem = document.createElement("input");
  newElem.setAttribute("type", "button");
  newElem.setAttribute("class", "btn btn-primary");
  newElem.setAttribute("value", "Delete Row");
  newElem.setAttribute("onclick", "SomeDeleteRowFunction(this)");
  newCell.appendChild(newElem);
}

window.SomeDeleteRowFunction = function SomeDeleteRowFunction(o) {
  var p = o.parentNode.parentNode;
  p.parentNode.removeChild(p);
};
