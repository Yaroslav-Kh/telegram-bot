<?php

$products = [
    (object)[
        'image'     => '/images/products/placeholder.jpg',
        'name'      => 'Lightsaber for Youngling',
        'currency'  => '$',
        'price'     => 300,
    ],
    (object)[
        'image'     => '/images/products/placeholder.jpg',
        'name'      => 'Lightsaber for Padawan',
        'currency'  => '$',
        'price'     => 900,
    ],
    (object)[
        'image'     => '/images/products/placeholder.jpg',
        'name'      => 'Lightsaber for Knight',
        'currency'  => '$',
        'price'     => 1500,
    ]
];


?>



<!doctype html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport"
        content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Shop</title>


    <link rel="stylesheet" href="css/style.css">
</head>

<body>
    <div id="main" class="wrapper">
        <div class="brand">
            <img class="brand__logo" class="img" src="/images/logo.svg">

        </div>


        <div class="products">
            <?php foreach($products as $product) : ?>
            <div class="product">
                <img src="<?= $product->image; ?>" alt="<?= $product->name; ?>" class="product__image">
                <div class="product__title"><?= $product->name; ?></div>
                <div class="product__price"><?= $product->currency; ?><?= $product->price; ?></div>
                <button data-product-button data-product-name="<?= $product->name; ?>" data-product-price="<?= $product->price; ?>" type="button" class="product__button">Buy</button>
            </div>
            <?php endforeach; ?>

        </div>

        <div data-checkout-modal class="modal">
            <form id="form" class="form">

                <div class="form__title">Checkout</div>
                <div class="form__field">
                    <label for="user_name">Username</label>
                    <input id="user_name" type="text" name="user_name">
                </div>
                <div class="form__field">
                    <label for="email">Email</label>
                    <input id="email" type="email" name="email">
                </div>
                <div class="form__field">
                    <label for="phone">Phone</label>
                    <input id="phone" type="text" name="phone">
                </div>
                <div class="form__field">
                    <label for="currency">Currency</label>
                    <select id="currency" name="currency">
                        <option value="USD">US Dollar</option>
                        <option value="USDC">USD Coin</option>
                    </select>
                </div>
                <div class="form__info">
                    <input type="hidden" name="product_name" value="">
                    <input type="hidden" name="product_price" value="">
                    <div class="form__price"><b data-form-name></b></div>
                    <div class="form__price">$<b data-form-price></b></div>
                </div>
                <div class="form__actions">
                    <button data-checkout-buy class="form__button form__button-checkout" type="button">Buy</button>
                    <button data-checkout-close class="form__button form__button-cancel" type="button">Cancel</button>
                </div>
            </form>
        </div>

    </div>

    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <script src="js/jquery.js"></script>
    <script src="app.js"></script>
    <script>

        const tg = window.Telegram.WebApp;
        const tgApi = new TgApi(tg);

        tg.expand()

        $('[data-product-button]').on('click', function () {
            $('[data-checkout-modal]').addClass('active');
            
            user = tgApi.user();

            //$('#user_name').val(user.first_name + ' ' + user.last_name);

            const name = $(this).attr('data-product-name');
            const price = $(this).attr('data-product-price');

            $('[name="product_name"]').val(name);
            $('[name="product_price"]').val(price);
            $('[data-form-name]').html(name);
            $('[data-form-price]').html(price);

        });

        $('[data-checkout-buy]').on('click', function () {

            const data = {
                user_name: $('[name="user_name"]').val(),
                email: $('[name="email"]').val(),
                phone: $('[name="phone"]').val(),
                currency: $('[name="currency"]').val(),
                product_name: $('[name="product_name"]').val(),
                product_price: $('[name="product_price"]').val(),
            };


            tgApi.send(data);

        });


        $('[data-checkout-close]').on('click', function () {
            $('[data-checkout-modal]').removeClass('active');
        });


    </script>

</body>

</html>