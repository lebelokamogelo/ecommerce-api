from rest_framework.test import APITestCase

from .models import (Review, Addres, Cart,
                     CartItem, Supplier, Profile,
                     Product, Categorie, User)


class TestModel(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@example.com",
                                        username="test",
                                        password="test1234")
        self.address = Addres.objects.create(street="address",
                                             city="city", zip_code="000")
        self.supplier = Supplier.objects.create(name="supplier",
                                                email="supplier@email.com",
                                                phone="0987654321")
        self.category = Categorie.objects.create(name="category")
        self.product = Product.objects.create(name="product",
                                              description="Product "
                                                          "description",
                                              price="20",
                                              quantity="20",
                                              category=self.category,
                                              supplier=self.supplier)
        self.review = Review.objects.create(user=self.user,
                                            product=self.product,
                                            rating=2,
                                            comment='Review')

        self.cart = Cart.objects.create(user=self.user)
        self.cartItems = CartItem.objects.create(cart=self.cart,
                                                 product=self.product)
        self.profile = Profile.objects.create(user=self.user,
                                              address=self.address)

    def test_address(self):
        self.assertEqual(str(self.address), 'city')

    def test_supplier(self):
        self.assertEqual(str(self.supplier), 'supplier')

    def test_category(self):
        self.assertEqual(str(self.category), 'category')

    def test_review(self):
        self.assertEqual(str(self.review), 'Review')

    def test_cart(self):
        self.assertEqual(str(self.cart), f'Cart {self.cart.id}')

    def test_cart_item(self):
        self.assertEqual(str(self.cartItems), f'Cart {self.cart.id} '
                                              f'{self.cart.user.username}')

    def test_products(self):
        self.assertEqual(str(self.product), 'product')

    def test_profile(self):
        self.assertEqual(str(self.profile), 'test')

    def test_review_truncate(self):
        review = Review.objects.create(user=self.user,
                                       product=self.product,
                                       rating=2,
                                       comment='This is a Review '
                                               'that will be truncated')
        self.assertEqual(str(review), "This is a Review that...")
