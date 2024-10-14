from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)  # Changed to Date type
    number = db.Column(db.Integer, nullable=False)

    # Define relationship with Appearance
    appearances = db.relationship('Appearance', backref='episode', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date.strftime("%m/%d/%y"),  # Format date as string
            "number": self.number,
            # List of appearances, transformed to dict format
            "appearances": [appearance.to_dict() for appearance in self.appearances]
        }

class Guest(db.Model):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)

    # Define relationship with Appearance
    appearances = db.relationship('Appearance', backref='guest', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "occupation": self.occupation
        }

class Appearance(db.Model):
    __tablename__ = 'appearances'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)  # Add validation elsewhere (1-5)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "episode_id": self.episode_id,
            "guest_id": self.guest_id,
            # Safeguard against missing episode or guest (e.g., due to database changes)
            "episode": {
                "id": self.episode.id if self.episode else None,
                "date": self.episode.date.strftime("%m/%d/%y") if self.episode else None,
                "number": self.episode.number if self.episode else None
            } if self.episode else None,
            "guest": {
                "id": self.guest.id if self.guest else None,
                "name": self.guest.name if self.guest else None,
                "occupation": self.guest.occupation if self.guest else None
            } if self.guest else None
        }
