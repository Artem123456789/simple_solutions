

buyItem = function (id) {
    let url = '/buy/' + id
    let api_key = 'pk_test_51OQYDXI4sAvJvb02RCTOoKBcrPfhEoyWMjsmdwd0hIdqk7NnqTfK2R9DNBRVPT5wMQ0QSSc5GX6F7a4I0omtINGP00wtqe94BE'
    let stripe = Stripe(api_key, {locale: 'fr'});
    $.ajax(url, {
        type: 'GET',
        data: {},
        success: function (data, success, xhr) {
            return stripe.redirectToCheckout({ sessionId: data['id'] });
        },
    });
}

addToCart = function (stripePrice, itemName) {
    let stripePrices = JSON.parse(localStorage.getItem('stripePrices') || '[]')
    stripePrices.push(stripePrice)
    localStorage.setItem('stripePrices', JSON.stringify(stripePrices))
    alert('Товар: ' + itemName + ' добавлен в корзину')
}

addDiscount = function (discount) {
    let discounts = JSON.parse(localStorage.getItem('discounts') || '[]')
    discounts.push(discount)
    localStorage.setItem('discounts', JSON.stringify(discounts))
}

addTax = function (amount) {
    let cartSum = JSON.parse(localStorage.getItem('cartSum') || '0')
    cartSum += amount
    localStorage.setItem('cartSum', JSON.stringify(cartSum))
}

checkoutCart = function () {
    let stripePrices = JSON.parse(localStorage.getItem('stripePrices') || '[]')
    stripePrices = stripePrices.join(',')

    let discounts = JSON.parse(localStorage.getItem('discounts') || [])
    discounts = discounts.join(',')
    let currency = $("#currencies").val()

    let url = '/checkout/'
    let api_key = 'pk_test_51OQYDXI4sAvJvb02RCTOoKBcrPfhEoyWMjsmdwd0hIdqk7NnqTfK2R9DNBRVPT5wMQ0QSSc5GX6F7a4I0omtINGP00wtqe94BE'
    let stripe = Stripe(api_key, {locale: 'fr'});

    $.ajax(url, {
        type: 'POST',
        data: {
            stripe_prices: stripePrices,
            currency: currency,
            discounts: discounts,
        },
        success: function (data, success, xhr) {
            return stripe.redirectToCheckout({ sessionId: data['id'] });
        },
    });
}

clearCart = function () {
    localStorage.removeItem('stripePrices')
    localStorage.removeItem('discounts')
    localStorage.removeItem('cartSum')
    alert('Корзина очищена')
}
