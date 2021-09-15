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
    var totalCards = document.getElementById('total_cards1').rows[1].cells[1].childNodes[0].value
    var column = [];
    column.push(totalCards)
    for(var i = 0; i<table.rows.length; i++){
        column.push(table.rows[i].cells[1].childNodes[0].value);
    }
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    $.ajax({
        headers: {'X-CSRFToken': csrftoken},
        url: 'get_custom_bingo',
        type: 'POST',
        data: {'arr':column},
        success:function (response) {
          if (response=='Error Code 1') {
            var modal1 = document.getElementById("error1-Modal");
            var span1 = document.getElementsByClassName("close")[0];
            modal1.style.display = "block";
            span1.onclick = function() {
              modal1.style.display = "none";
            }
            window.onclick = function(event) {
              if (event.target == modal1) {
                modal1.style.display = "none";
              }
            }
          }
          else if (response=='Error Code 2') {
            var modal2 = document.getElementById("error2-Modal");
            var span2 = document.getElementsByClassName("close")[1];
            modal2.style.display = "block";
            span2.onclick = function() {
              modal2.style.display = "none";
            }
            window.onclick = function(event) {
              if (event.target == modal2) {
                modal2.style.display = "none";
              }
            }
          }
          else if (response=='Error Code 3') {
            var modal3 = document.getElementById("error3-Modal");
            var span3 = document.getElementsByClassName("close")[2];
            modal3.style.display = "block";
            span3.onclick = function() {
              modal3.style.display = "none";
            }
            window.onclick = function(event) {
              if (event.target == modal3) {
                modal3.style.display = "none";
              }
            }
          }
          else {download(response, 'BINGO_CARDS.pdf', 'application/pdf' );
        }},
        error:function () {
          var modal4 = document.getElementById("error3-Modal");
            var span4 = document.getElementsByClassName("close")[0];
            modal4.style.display = "block";
            span4.onclick = function() {
              modal4.style.display = "none";
            }
            window.onclick = function(event) {
              if (event.target == modal4) {
                modal4.style.display = "none";
              }
            }
          }
      });
};  

function removeField()
{
	var table = document.getElementById('tbl')
	var rowCount = table.rows.length;
	if(rowCount > 25){
		table.deleteRow(-1);
	} 
}

function getCol_classic()
{
  var totalCards = document.getElementById('total_cards2').rows[1].cells[1].childNodes[0].value;
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    $.ajax({
        headers: {'X-CSRFToken': csrftoken},
        url: 'get_classic_bingo',
        type: 'POST',
        data: {'cards':totalCards},
        success:function (response) {
          if (response=='Error Code 1') {
            var modal1 = document.getElementById("error1-Modal");
            var span1 = document.getElementsByClassName("close")[0];
            modal1.style.display = "block";
            span1.onclick = function() {
              modal1.style.display = "none";
            }
            window.onclick = function(event) {
              if (event.target == modal1) {
                modal1.style.display = "none";
              }
            }
          }
          else if (response=='Error Code 2') {
            var modal2 = document.getElementById("error2-Modal");
            var span2 = document.getElementsByClassName("close")[1];
            modal2.style.display = "block";
            span2.onclick = function() {
              modal2.style.display = "none";
            }
            window.onclick = function(event) {
              if (event.target == modal2) {
                modal2.style.display = "none";
              }
            }
          }
          else if (response=='Error Code 3') {
            var modal3 = document.getElementById("error3-Modal");
            var span3 = document.getElementsByClassName("close")[2];
            modal3.style.display = "block";
            span3.onclick = function() {
              modal3.style.display = "none";
            }
            window.onclick = function(event) {
              if (event.target == modal3) {
                modal3.style.display = "none";
              }
            }
          }
          else {download(response, 'BINGO_CARDS.pdf', 'application/pdf' );
        }},
        error:function () {
          var modal4 = document.getElementById("error3-Modal");
            var span4 = document.getElementsByClassName("close")[0];
            modal4.style.display = "block";
            span4.onclick = function() {
              modal4.style.display = "none";
            }
            window.onclick = function(event) {
              if (event.target == modal4) {
                modal4.style.display = "none";
              }
            }
          }
      });
}