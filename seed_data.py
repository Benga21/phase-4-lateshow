from datetime import datetime
from models import db, Episode, Guest, Appearance
from app import app

# Seed data for episodes and guests
seed_data = [
    {"year": 1999, "occupation": "Actor", "date": "1/11/99", "show_group": "Acting", "guest_name": "Michael J. Fox"},
    {"year": 1999, "occupation": "Comedian", "date": "1/12/99", "show_group": "Comedy", "guest_name": "Sandra Bernhard"},
    {"year": 1999, "occupation": "Television actress", "date": "1/13/99", "show_group": "Acting", "guest_name": "Tracey Ullman"},
    {"year": 1999, "occupation": "Film actress", "date": "1/14/99", "show_group": "Acting", "guest_name": "Gillian Anderson"},
    {"year": 1999, "occupation": "Actor", "date": "1/18/99", "show_group": "Acting", "guest_name": "David Alan Grier"},
    {"year": 1999, "occupation": "Actor", "date": "1/19/99", "show_group": "Acting", "guest_name": "William Baldwin"},
    {"year": 1999, "occupation": "Singer-lyricist", "date": "1/20/99", "show_group": "Musician", "guest_name": "Michael Stipe"},
    {"year": 1999, "occupation": "Model", "date": "1/21/99", "show_group": "Media", "guest_name": "Carmen Electra"},
    {"year": 1999, "occupation": "Actor", "date": "1/25/99", "show_group": "Acting", "guest_name": "Matthew Lillard"},
    {"year": 1999, "occupation": "Stand-up comedian", "date": "1/26/99", "show_group": "Comedy", "guest_name": "David Cross"},
    {"year": 1999, "occupation": "Actress", "date": "1/27/99", "show_group": "Acting", "guest_name": "Yasmine Bleeth"},
    {"year": 1999, "occupation": "Actor", "date": "1/28/99", "show_group": "Acting", "guest_name": "D. L. Hughley"},
    {"year": 1999, "occupation": "Television actress", "date": "10/18/99", "show_group": "Acting", "guest_name": "Rebecca Gayheart"},
    {"year": 1999, "occupation": "Comedian", "date": "10/19/99", "show_group": "Comedy", "guest_name": "Steven Wright"},
    {"year": 1999, "occupation": "Actress", "date": "10/20/99", "show_group": "Acting", "guest_name": "Amy Brenneman"},
    {"year": 1999, "occupation": "Actress", "date": "10/21/99", "show_group": "Acting", "guest_name": "Melissa Gilbert"},
    {"year": 1999, "occupation": "Actress", "date": "10/25/99", "show_group": "Acting", "guest_name": "Cathy Moriarty"},
    {"year": 1999, "occupation": "Comedian", "date": "10/26/99", "show_group": "Comedy", "guest_name": "Louie Anderson"},
    {"year": 1999, "occupation": "Actress", "date": "10/27/99", "show_group": "Acting", "guest_name": "Sarah Michelle Gellar"},
    {"year": 1999, "occupation": "Singer-songwriter", "date": "10/28/99", "show_group": "Musician", "guest_name": "Melanie C"},
    {"year": 1999, "occupation": "Actor", "date": "10/4/99", "show_group": "Acting", "guest_name": "Greg Proops"},
    {"year": 1999, "occupation": "Television personality", "date": "10/5/99", "show_group": "Media", "guest_name": "Maury Povich"},
    {"year": 1999, "occupation": "Actress", "date": "10/6/99", "show_group": "Acting", "guest_name": "Brooke Shields"},
    {"year": 1999, "occupation": "Comic", "date": "10/7/99", "show_group": "Comedy", "guest_name": "Molly Shannon"},
    {"year": 1999, "occupation": "Actor", "date": "11/1/99", "show_group": "Acting", "guest_name": "Chris O'Donnell"},
    {"year": 1999, "occupation": "Actress", "date": "11/15/99", "show_group": "Acting", "guest_name": "Christina Ricci"},
    {"year": 1999, "occupation": "Singer-songwriter", "date": "11/16/99", "show_group": "Musician", "guest_name": "Tori Amos"},
    {"year": 1999, "occupation": "Actress", "date": "11/17/99", "show_group": "Acting", "guest_name": "Yasmine Bleeth"},
    {"year": 1999, "occupation": "Comedian", "date": "11/18/99", "show_group": "Comedy", "guest_name": "Bill Maher"},
    {"year": 1999, "occupation": "Actress", "date": "11/2/99", "show_group": "Acting", "guest_name": "Jennifer Love Hewitt"},
    {"year": 1999, "occupation": "Rock band", "date": "11/29/99", "show_group": "Musician", "guest_name": "Goo Goo Dolls"},
    {"year": 1999, "occupation": "Musician", "date": "11/3/99", "show_group": "Musician", "guest_name": "Dave Grohl"}
]

# Create episode and guest objects from seed data
episodes = []
guests = []
appearances = []

for idx, data in enumerate(seed_data):
    # Create an episode
    episode = Episode(date=datetime.strptime(data['date'], '%m/%d/%y').date(), number=idx + 1)
    guest = Guest(name=data['guest_name'], occupation=data['occupation'])

    episodes.append(episode)
    guests.append(guest)

    # Link guest to episode with an appearance
    appearance = Appearance(rating=0, episode=episode, guest=guest)  
    appearances.append(appearance)

# Run the seeding process
with app.app_context():
    # Clear the existing data
    db.drop_all()
    db.create_all()

    # Add the new data to the session
    db.session.add_all(episodes)
    db.session.add_all(guests)
    db.session.add_all(appearances)

    # Commit the changes to the database
    db.session.commit()

print("Database seeded successfully!")
