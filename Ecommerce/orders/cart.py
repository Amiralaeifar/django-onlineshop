
CART_SESSION_ID = 'cart'


class Cart:
    
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart 
        
        
    def add(self, product, quantity):
        product_id = str(product.id)
        if product not in self.card:
            self.card[product_id] = {'quantity': 0, 'price': product.price}
        self.card[product_id]['quantity'] += quantity
        self.save()
        
        
    def save(self):
        self.session.modified = True 