//init sys ingredients
const ingredients = list_ingredients;//list object ingredient
if (pageName === "home") {
  $(function() {
    /*PAGE HOME CODE */
    //GLOBAL VARIABLES
    let inputValue = $('.inputValue');
    let divSuggestList = $('.suggest-ingredients');
    let divListeIngredient = $('.liste-ingredients');
    //NORMAL VARIABLES
    let addIngredient = $('.add-ingredient');
    let helpText = $('.help-text');
    let submit = $('#submit');
    inputWidth = inputValue.width()
    divSuggestList.width(inputWidth);//style width
    let eltNumber = 0;
    //init ingredients_select by user
    ingredients_select = []
    const ingredient_names = [] //names of ingredients
    //loop to get just names of ingredients
    for (const ingredient of ingredients){
      ingredient_names.push(ingredient.name)
    }
  
    /*this function add ingredient choiced by user in a form and
    showing list of selected ingredients from user*/
    const addIngredientInForm = () =>{
      //Tesxt alert
      let alert = $('#empty-add');
      alert.css('color', 'rgb(85,0,0)');
      alert.css('fontWeight', 'bolder');
      alert.css('textShadow', '0px 3px 2px black');
      /*create a table to verify if new ingredient from user
      is not yet in list_ingredients*/
      let tableValue = []
      let form = $('form');
      let inputElts = $('form :input');
      for (inputElt of inputElts){
        let valueInput = $(inputElt)
        tableValue.push(valueInput.val());
      }
  
      let ingredient_exist = false;
      //loop to compare if inputValue is in tableValue
      for (const value of tableValue){
        if (value === inputValue.val()){
          alert.text(`l'ingrédient "${inputValue.val()}" a déjà été ajouté !`);
          ingredient_exist = true;
        }
      }
  
      //conformity verification
      if (inputValue.val() === ""){
        alert.text("Insérer un ingredient pour ajouter !");
      }else if(ingredient_names.indexOf(inputValue.val()) === -1){
        alert.text(`Désolé l'ingredient "${inputValue.val()}" n'est pas disponible`);
      }else if (!ingredient_exist){
        eltNumber++;//increment element number created for unique identification
        /*creating of pElt to show in frontend, ingredient selected by user*/
        let p = document.createElement('p');
        let pElt = $(p)
        pElt.attr('id', `pElt${eltNumber}`);
        pElt.text(inputValue.val());
  
        //create a button to cancel or remove ingredient select
        let button = document.createElement('button');
        let buttonCancel = $(button)
        buttonCancel.attr({'id': `btn${eltNumber}`, 'class': 'btn-x'});
        buttonCancel.text('x');
        buttonCancel.css('background', '#da80a6');
        buttonCancel.css('border', '1px solid black');
        buttonCancel.css('borderRadius', '10px');
  
        //creating div to content pElt with button x
        let div = document.createElement('div');
        let divParent = $(div)
        divParent.append(pElt);
        divParent.append(buttonCancel);
        divParent.css('display', 'flex');
        divParent.css('justifyContent', 'space-between');
        divParent.css('alignItems', 'baseline');
        divParent.css('marginTop', '2px');
        //find url_image with compare inputValue and each entry in list object ingredient
        for (const ingredient of ingredients){
          if (ingredient.name === inputValue.val()){
            url_img = ingredient.url_img;
          }
        }
        divParent.css('background', `white url(${url_img}) no-repeat center center`);
        divParent.css('backgroundSize', "contain");
        divParent.css('borderRadius', "10px");
        divParent.css('padding', '15px');
        //add div parent to divListeIngredient
        divListeIngredient.prepend(divParent);
  
        /*create input formulaire hiiden
        to send with post method*/
        let input = document.createElement('input');
        let ingredientInput = $(input)
        ingredientInput.attr({'value': inputValue.val(), 'name': inputValue.val()});
        form.append(ingredientInput);
  
        //delete texte of alert
        alert.text('');
  
        //action to remove
        buttonCancel.on('click', function(){
          //remove input ingredient from list
          ingredients_select.pop(inputValue);
          //remove div content pElt and button x
          divParent.remove();
          //remove too from form, input element
          ingredientInput.remove();
        });
      }
    }
    
    const createListSuggest = (eltVal, defaultAction=true) => {
      //clear divSuggestList
      divSuggestList.html('');
      divSuggestList.height('auto');
      divSuggestList.css('display', 'none');
      /*for each ingredient in ingredients we verifie
      if value input exists in liste*/
      for (const ingredient of ingredients){
        if ((ingredient.name.indexOf(eltVal) === 0) && (eltVal !== '')){
          let a = document.createElement('a');
          let ahref = $(a);
          ahref.attr('href', '#');
          ahref.css('color', "black");
          let p = document.createElement('p');
          let pElt = $(p);
          pElt.text(ingredient.name);
          pElt.css('fontSize', '0.9em');
          pElt.css('background', `url(${ingredient.url_img}) no-repeat center center`);
          pElt.css('backgroundSize', "70px, 40px");
          pElt.css('height', "70px");
          pElt.css('paddingTop', "22px");
          pElt.css('borderBottom', "1px solid #da80a6");
          pElt.css('color', '#da80a6');
          pElt.css('fontWeight', 'bold');
          ahref.append(pElt);
          divSuggestList.append(ahref);
          divSuggestList.css('display', 'block');
          divSuggestList.css('zIndex', '4');
  
          if (divSuggestList.height() > 250){
            divSuggestList.height(250);
            divSuggestList.css('overflowY', 'auto');
          }
          /*action to click on pElt
          add it in input and in form and in showing ingredients selected*/
          ahref.on('click', function(e){
            e.preventDefault();
            inputValue.val(pElt.text())
            divSuggestList.css('display', 'none');
            //action to add ingredeint in form and showing ingredients selected
            if (defaultAction === true){
              addIngredientInForm();
            }        
          });
        }
      }
    }
  
    /*button to add ingredient in table ingredients select and
    create a input form*/
    addIngredient.on('click', () => {
        addIngredientInForm();
      });
  
    //when focus clear the input Value
    (inputValue).on('focus', () => {
      inputValue.val('');
      inputValue.css('background', 'rgba(10, 10,10, 0.8)');
      inputValue.css('color', 'white');
      divSuggestList.css('display', 'none');
    });
  
    inputValue.on('input', (e) => {
      eltVal = e.target.value;
      createListSuggest(eltVal);
    });
  
    submit.on('click', (e) => {
      if ($('.liste-ingredients :input').length < 1){
        e.preventDefault();
        let alert = document.getElementById('empty-submit');
        alert.style.display = 'inline-block';
        alert.style.textShadow = '0px 3px 2px black';
        alert.style.fontWeight = 'bolder';
        alert.style.borderRadius = '15px';
        alert.textContent = "La liste des ingredients est vide ! veuillez inserer les ingredients";
        alert.style.color = 'rgb(85,0,0)';
      }
    });
  });
  
} else if(pageName === "create-recipe") {
    $(function() {
      /*==========================================================================================*/
      /*PAGE CREATE RECIPE CODES*/
      //init a first line
      let lineNumber = 1;
      //create line to add ingredient 
      const createLine = () => {
        let lineIngredient = document.createElement('tr');
        let line = $(lineIngredient);
        line.html(`\    
          <td><input type="number" name="quantity-ingredient${lineNumber}"></td>\
          <td><input type="text" name="indication-ingredient${lineNumber}"></td>\
        `);
        let colElt = document.createElement('td');
        let input = document.createElement('input');
        $(input).attr('name', `name-ingredient${lineNumber}`);
        $(colElt).append(input);
        line.prepend(colElt);

        let cancel = document.createElement('a');
        let cancelLine = $(cancel);
        cancelLine.attr('href', '#');
        cancelLine.text('x');
        line.append(cancelLine);

        let line2 = document.createElement('tr');
        let divSuggest = document.createElement('div');
        $(divSuggest).attr('class', 'suggestList');
        
        $(input).on('input', (e) => {
          $(divSuggest).html('');
          let ingredientFound = false;

          for (const ingredient of ingredients){
            if ((ingredient.name.indexOf(e.target.value) === 0) && (e.target.value !== '')){
              let a = document.createElement('a');
              $(a).attr('href', '#');
              $(a).html(`<p>${ingredient.name}</p>`);
              $(divSuggest).append(a);

              $(a).on('click', (e) => {
                e.preventDefault();
                $(input).val(ingredient.name);
                $(divSuggest).html('');
              });
              ingredientFound = true;
            }
          }

          if (!ingredientFound && (e.target.value !== "")){
            $(divSuggest).html(`<span style="color: red">Ingredient non disponible</span>\
            </br>Cliquez <a href="#">ici</a> pour l'ajouter`);
            $(input).css('border', '2px solid red');
          }
        });

        $(line2).append(divSuggest);

        //cancel line ingredient
        cancelLine.click((e) => {
          e.preventDefault();
          line.remove();
        });    
        return $('table').append(lineIngredient).append(line2);
      }

      //init first line 
      createLine();
      //action to create new line ingredient 
      $('#btn-add-line').click((e) => {
        lineNumber++;
        e.preventDefault();
        createLine();
      });
    });
}