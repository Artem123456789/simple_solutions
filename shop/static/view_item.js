

buyItem = function (id) {
    let url = '/buy/' + id
    api_key = 'pk_test_51OQYDXI4sAvJvb02RCTOoKBcrPfhEoyWMjsmdwd0hIdqk7NnqTfK2R9DNBRVPT5wMQ0QSSc5GX6F7a4I0omtINGP00wtqe94BE'
    let stripe = Stripe(api_key,{locale: 'fr'});
    $.ajax(url, {
        type: 'GET',
        data: {},
        success: function (data, success, xhr) {
            return stripe.redirectToCheckout({ sessionId: data['id'] });
        },
    });
}