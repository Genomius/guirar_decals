$(document).ready(function () {
    var csrf = $('input[name=csrfmiddlewaretoken]').val();

    $(".decal_to_cart").click(function () {
        $.ajax({
            url: '/cart/',
            type: 'post',
            data: {
                'csrfmiddlewaretoken': csrf,
                'decal_id': $(this).data('id')
            },
            dataType: 'json',
            success: function (data) {
                    alert('Товар добавлен в корзину<br><a href="/cart/" class="notice-cart-link">Перейти в корзину</a>');
            },
            error : function (error) {
                console.log(error);
            }
        });
    });

    $(".order-btn").click(function(){

    });
});