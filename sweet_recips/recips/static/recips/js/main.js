$(function() {
  //GLOBAL VARIABLES
  $inputValue = $('#inputValue');
  $divSuggestList = $('#suggest-ingredients');
  $divListeIngredient = $('.liste-ingredients');
  //NORMAL VARIABLES
  $addIngredient = $('.add-ingredient');
  $helpText = $('.help-text');
  $submit = $('#submit');
  $inputWidth = $inputValue.width();
  $divSuggestList.css('width', $inputWidth);//style width
  $eltNumber = 0;
  //init ingredients_select by user
  ingredients_select = []
  //init sys ingredients
  const ingredients = list_ingredients;//list object ingredient
  const ingredient_names = [] //names of ingredients
  //loop to get just names of ingredients
  for (const ingredient of ingredients){
    ingredient_names.push(ingredient.name)
  }

  /*this function add ingredient choiced by user in a form and
  showing list of selected ingredients from user*/
  const addIngredientInForm = () =>{
    //Tesxt alert
    $alert = $('#empty-add');
    $alert.css('color', 'rgb(85,0,0)');
    $alert.css('fontWeight', 'bolder');
    $alert.css('textShadow', '0px 3px 2px black');
    /*create a table to verify if new ingredient from user
    is not yet in list_ingredients*/
    $tableValue = []
    $form = $('form');
    $inputElts = $('form :input');
    for (input of $inputElts){
      $tableValue.push(input.value);
    }

    $ingredient_exist = false;
    //loop to compare if inputValue is in tableValue
    for (const value of $tableValue){
      if (value === $inputValue.val()){
        $alert.text(`l'ingrédient "${inputValue.value}" a déjà été ajouté !`);
        $ingredient_exist = true;
      }
    }

    //conformity verification
    if ($inputValue.val() === ""){
      $alert.text("Insérer un ingredient pour ajouter !");
    }else if(ingredient_names.indexOf($inputValue.val()) === -1){
      $alert.text(`Désolé l'ingredient "${$inputValue.val()}" n'est pas disponible`);
    }else if (!$ingredient_exist){
      $eltNumber++;//increment element number created for unique identification
      /*creating of pElt to show in frontend, ingredient selection by user*/
      let pElt = document.createElement('p');
      pElt.setAttribute('id', `pElt${$eltNumber}`);
      pElt.textContent = inputValue.value;

      //create a button to cancel or remove ingredient select
      let buttonCancel = document.createElement('button');
      buttonCancel.setAttribute('id', `btn${$eltNumber}`);
      buttonCancel.classList.add('btn-x');
      buttonCancel.textContent = 'x';
      buttonCancel.style.background = '#da80a6';
      buttonCancel.style.border = '1px solid black';
      buttonCancel.style.borderRadius = '10px';

      //creating div to content pElt with button x
      let divParent = document.createElement('div');
      divParent.appendChild(pElt);
      divParent.appendChild(buttonCancel);
      divParent.style.display = 'flex';
      divParent.style.justifyContent = 'space-between';
      divParent.style.alignItems = 'baseline';
      divParent.style.marginTop = '2px';
      //find url_image with compare inputValue and each entry in list object ingredient
      for (const ingredient of ingredients){
        if (ingredient.name === inputValue.value){
          url_img = ingredient.url_img;
        }
      }
      divParent.style.background = `white url(${url_img}) no-repeat center center`;
      divParent.style.backgroundSize = "contain";
      divParent.style.borderRadius = "10px";
      divParent.style.padding = '15px';
      //add div parent to divListeIngredient
      $divListeIngredient.append(divParent);

      /*create input formulaire hiiden
      to send with post method*/
      let input = document.createElement('input');
      input.setAttribute('value', inputValue.value);
      input.setAttribute('name', inputValue.value)
      let formElt = document.querySelector('form');
      formElt.appendChild(input);

      //delete texte of alert
      alert.textContent = '';

      //action to remove
      buttonCancel.addEventListener('click', function(){
        //remove input ingredient from list
        ingredients_select.pop(inputValue);
        //remove div content pElt and button x
        divParent.remove();
        //remove too from form, input element
        formElt.removeChild(input);
      });
    }
  }

  /*button to add ingredient in table ingredients select and
  create a input form*/
  $addIngredient.on('click', () => {
      addIngredientInForm();
    });

  //when focus clear the input Value
  inputValue.addEventListener('focus', () => {
    inputValue.value = '';
    inputValue.style.background = 'rgba(10, 10,10, 0.8)';
    inputValue.style.color = 'white';
  });

  inputValue.addEventListener('input', (e) => {
    //clear divSuggestList
    $divSuggestList.html('');
    $divSuggestList.css('display', 'none');
    /*for each ingredient in ingredients we verifie
    if value input exists in liste*/
    for (const ingredient of ingredients){
      if ((ingredient.name.indexOf(e.target.value) === 0) && (e.target.value !== '')){
        let ahref = document.createElement('a');
        ahref.href = '#';
        ahref.style.color = "black";
        let pElt = document.createElement('p');
        pElt.setAttribute('id', 'suggest_para');
        pElt.textContent = ingredient.name;
        pElt.style.background = `url(${ingredient.url_img}) no-repeat center center`;
        pElt.style.backgroundSize = "contain";
        pElt.style.height = "70px";
        pElt.style.paddingTop = "22px";
        pElt.style.borderBottom = "4px solid #da80a6";
        pElt.style.color = '#da80a6';
        pElt.style.fontWeight = 'bold';
        ahref.appendChild(pElt);
        $divSuggestList.append(ahref);
        $divSuggestList.css('display', 'block');

        //action to click on pElt
        //add it in input and in form and in showing ingredients selected
        ahref.addEventListener('click', function(e){
          e.preventDefault();
          inputValue.value = pElt.textContent
          $divSuggestList.css('display', 'none');

          //action to add ingredeint in form and showing ingredients selected
          addIngredientInForm()
        });
      }
    }
  });

  submit.addEventListener('click', (e) => {
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
