function addField()
{
	// Get total rows
	var table = document.getElementById('tbl');
  	var rowCount = table.rows.length;
  	var rowNum = document.createElement('td');
  	var rowNumText = document.createTextNode(rowCount + 1 + ")");
  	rowNum.appendChild(rowNumText);
	
	// Get tbody, create new row
	var myTB = document.getElementById('tbdy');
	var myTr = myTB.insertRow(-1);
  	var myTd = document.createElement('td');
    var myInput = document.createElement('input');
    myInput.setAttribute('type','text');
  	myInput.setAttribute('id', 'input_row');
    myTd.appendChild(myInput);
    myTr.appendChild(rowNum);
  	myTr.appendChild(myTd);
}

function getCol()
{
	var table = document.getElementById('tbl');
	var column = [];
	for(var i = 0; i<table.rows.length; i++){
		column.push(table.rows[i].cells[1].childNodes[0].value);
	}
	alert(column);
	return column;
}

function removeField()
{
	var table = document.getElementById('tbl')
	var rowCount = table.rows.length;
	if(rowCount > 24){
		table.deleteRow(-1);
	} 
}
