$(function () {
    $('[data-toggle="tooltip"]').tooltip();
});
function calculateTotal() {
    var total = 0;
    var cards = document.getElementsByClassName("card");
    for (var i = 0; i < cards.length; i++) {
        var card = cards[i];
        var price = parseFloat(card.getElementsByClassName("price")[0].value);
        var quantity = parseInt(card.getElementsByClassName("quantity")[0].value);
      total += price * quantity;
    }

    document.getElementById("totalPrice").innerHTML = "Total Price: $" + total.toFixed(2);
}