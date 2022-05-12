function addField()
{
    var table = document.getElementById('tbl');
	var myTd,myInput;
	var myTr = document.createElement('tr');
	var rowCount = table.rows.length;
	var disp = document.getElementById('display');
	myTr.setAttribute('class','unit-table');
	rowNum = document.createElement('td');
	var rowNumText = document.createTextNode(rowCount + 1 + ")");
	rowNum.appendChild(rowNumText);
	myTd = document.createElement('td');
    myInput = document.createElement('input');
    myInput.setAttribute('type','text');
    myTd.appendChild(myInput);
    myTr.appendChild(rowNum);
	myTr.appendChild(myTd);
	table.appendChild(myTr);
}

function getCol(col)
{
	matrix = document.getElementById('tbl');
	var column = [];
	for(var i=0; i<matrix.length; i++){
		column.push(matrix[i][col]);
	}
	return column;
	
}

alert(column);