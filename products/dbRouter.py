class App2DBRouter(object): 
    def db_for_read(self, model, **hints):
        "Point all operations on products models to 'db_products'"
        if model._meta.app_label == 'Product':
            return 'db_products'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on products models to 'db_products'"
        if model._meta.app_label == 'Product':
            return 'db_products'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in products app"
        if obj1._meta.app_label == 'Product' and obj2._meta.app_label == 'Product':
            return True
        # Allow if neither is products app
        elif 'Product' not in [obj1._meta.app_label, obj2._meta.app_label]: 
            return True
        return False
    
    def allow_syncdb(self, db, model):
        if db == 'db_product' or model._meta.app_label == "Product":
            return False # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return True