from app import app
from models import db, Bakery, BakedGood

with app.app_context():
    db.drop_all()
    db.create_all()
    
    # Create bakeries
    delightful_donuts = Bakery(name="Delightful donuts")
    incredible_crullers = Bakery(name="Incredible crullers")
    
    db.session.add_all([delightful_donuts, incredible_crullers])
    db.session.commit()
    
    # Create baked goods for Delightful donuts
    chocolate_donut = BakedGood(name="Chocolate dipped donut", price=2.75, bakery_id=delightful_donuts.id)
    apple_donut = BakedGood(name="Apple-spice filled donut", price=3.5, bakery_id=delightful_donuts.id)
    
    # Create baked goods for Incredible crullers
    honey_cruller = BakedGood(name="Glazed honey cruller", price=3.25, bakery_id=incredible_crullers.id)
    chocolate_cruller = BakedGood(name="Chocolate cruller", price=3.4, bakery_id=incredible_crullers.id)
    
    db.session.add_all([chocolate_donut, apple_donut, honey_cruller, chocolate_cruller])
    db.session.commit()
    
    print("Database seeded successfully!")

