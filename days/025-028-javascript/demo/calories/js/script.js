const foodBalanceWrapper = document.getElementById("foodBalanceWrapper")
foodBalanceWrapper.style.display = "none";

// https://goodies.pixabay.com/javascript/auto-complete/demo.html
new autoComplete({
  selector: 'input[name="foodPicker"]',
  minChars: 2,
  source: function(term, suggest){
    term = term.toLowerCase();
    let choices = Object.keys(foodDb);  // defined in food.js
    let matches = [];
    for(i=0; i<choices.length; i++){
      let kcal = foodDb[choices[i]];
      if(kcal == 0){
        continue;
      }

      if(~choices[i].toLowerCase().indexOf(term)){
        let item = `${choices[i]} (${kcal} kcal)`;
        matches.push(item);
      }
    }
    suggest(matches);
  }
});


// handle form submission (best to not do it in the mark-up)
// https://stackoverflow.com/a/5384732
function processForm(e) {
    if (e.preventDefault) e.preventDefault();
    updateFoodLog();
    return false;
}

var form = document.getElementById('foodPickerForm');
if (form.attachEvent) {
    form.attachEvent("submit", processForm);
} else {
    form.addEventListener("submit", processForm);
}


// helpers
function recalculateTotal(){
  let tds = document.getElementsByTagName("td");
  let sum = 0, len = tds.length;
  for (var i = 0; i<len; i++) {
    if (tds[i].className == "kcal") {
      sum += parseFloat(tds[i].innerText);
    }
  }
  return sum;
}

function updateTotalKcal(){
  let sum = recalculateTotal();
  document.getElementById("total").innerHTML = parseInt(sum);

  // if 0 kcal hide kcal div
  if(sum == 0){
    foodBalanceWrapper.style.display = "none";
  } else {
    foodBalanceWrapper.style.display = "block";
  }
}

function emptyFoodPicker(){
  document.getElementById("foodPicker").value = '';
}

function removeRow(){
  // https://stackoverflow.com/a/53085148
  let td = event.target.parentNode;
  let tr = td.parentNode; // the row to be removed
  tr.parentNode.removeChild(tr);
  updateTotalKcal();
}

function updateFoodLog(){
  let selectedFood = document.getElementById("foodPicker").value;
  selectedFood = selectedFood.substr(0, selectedFood.lastIndexOf("(")).trim();
  let kcals = foodDb[selectedFood];

  if(kcals === undefined){
    alert('Unknown food, please try again');
    emptyFoodPicker();
    return;
  }

  let tbody = document.getElementById("foodBalanceBody");
  let newTableRow = document.createElement("tr");

  let col1 = document.createElement("td");
  let col2 = document.createElement("td");
  let col3 = document.createElement("td");

  col1.textContent = selectedFood;

  col2.textContent = parseInt(kcals);
  col2.className = "kcal";  // for calculation

  let deleteBtn = document.createElement("input");
  deleteBtn.onclick = removeRow;
  deleteBtn.type = 'button';
  deleteBtn.className = 'delete';
  col3.appendChild(deleteBtn);

  newTableRow.appendChild(col1);
  newTableRow.appendChild(col2);
  newTableRow.appendChild(col3);

  tbody.appendChild(newTableRow);

  updateTotalKcal();
  emptyFoodPicker();
}
