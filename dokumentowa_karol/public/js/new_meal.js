document.addEventListener('DOMContentLoaded', function() {
  let ingredientCounter = 1;

  document.getElementById('add-ingredient-button').addEventListener('click', function() {
    const ingredientsContainer = document.getElementById('ingredients-container');

    const ingredientRow = document.createElement('div');
    ingredientRow.className = 'ingredient-row';

    const nameLabel = document.createElement('label');
    nameLabel.setAttribute('for', `ingredient-name-${ingredientCounter}`);
    nameLabel.textContent = 'Name:';
    ingredientRow.appendChild(nameLabel);

    const nameInput = document.createElement('input');
    nameInput.type = 'text';
    nameInput.name = `ingredients[${ingredientCounter}][name]`;
    nameInput.required = true;
    ingredientRow.appendChild(nameInput);

    const quantityLabel = document.createElement('label');
    quantityLabel.setAttribute('for', `ingredient-quantity-${ingredientCounter}`);
    quantityLabel.textContent = 'Quantity:';
    ingredientRow.appendChild(quantityLabel);

    const quantityInput = document.createElement('input');
    quantityInput.type = 'number';
    quantityInput.name = `ingredients[${ingredientCounter}][quantity]`;
    quantityInput.required = true;
    ingredientRow.appendChild(quantityInput);

    ingredientsContainer.appendChild(ingredientRow);

    ingredientCounter++;
  });
});
