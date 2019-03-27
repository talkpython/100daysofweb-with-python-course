const foodBalanceWrapper = document.getElementById("foodBalanceWrapper")
foodBalanceWrapper.style.display = "none";

// provided: vanilla JS autocomplete
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


// provided: handle form submission to not do it as inline JS
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
  // get all table cells (tds) and sum the calories = td with kcal
}

function updateTotalKcal(){
  // write the total kcal count into  the total id, if 0 hide the
  // foodBalanceWrapper div
}

function emptyFoodPicker(){
  // reset the foodPicker ID value
}

function removeRow(){
  // remove a table row and update the total kcal
  // https://stackoverflow.com/a/53085148
}

function updateFoodLog(){
  // udate the food table with the new food, building up the inner dom
  // elements, including adding a delete button / onclick handler
  // finally call updateTotalKcal and emptyFoodPicker
}
