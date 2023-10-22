document.querySelectorAll('.card').forEach(card => {
    const addToCartButton = card.querySelector('.add-to-cart');
    addToCartButton.addEventListener('click', () => {
        addToCartButton.textContent = "Товар добавлен!"
        setTimeout(() => {
            addToCartButton.textContent = 'Добавить в корзину';
          }, 2000); 
    });
  });

window.addEventListener('click', function(event) {
  if (event.target.classList.contains('add-to-cart')) {
    const card = event.target.closest(".card")
    
    const productInfo = {
      title: card.querySelector('.card-title').textContent,
      price: card.querySelector('.product-price').textContent,
      image: card.querySelector('.product-img').src,
      id: card.dataset.id
    }
    console.log(productInfo)
    // Получите текущий список товаров в корзине из локального хранилища
    let cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

    // Добавьте новый товар в корзину
    cartItems.push(productInfo);

    // Сохраните обновленный список товаров в локальное хранилище
    localStorage.setItem('cartItems', JSON.stringify(cartItems));
    


    

}})
  

    
