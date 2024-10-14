from flask import Flask, request, jsonify
from models import db, Episode, Guest, Appearance
from routes import main_routes

# Initializes the Flask application
app = Flask(__name__)

# Configurations for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///late_show.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializes the database
db.init_app(app)

# Registers the blueprint for web routes
app.register_blueprint(main_routes)

# Creates tables 
with app.app_context():
    db.create_all()

# Roots endpoints for API Documentation
@app.route('/', methods=['GET'])
def api_documentation():
    return jsonify({
        "message": "WELCOME TO THE LATE SHOW EPISODES API! USE THE FOLLOWING ENDPOINTS TO ACCESS DATA.",
        "endpoints": {
            "GET /episodes": "Retrieves a list of all episodes.",
            "GET /episodes/<int:id>": "Retrieves a specific episode by its ID.",
            "GET /guests": "Retrieves a list of all guests.",
            "GET /guests/<int:id>": "Retrieves a specific guest by their ID.",  
            "GET /appearances": "Retrieves a list of all appearances.",
            "GET /appearances/<int:id>": "Retrieves a specific appearance by its ID.",  
            "POST /appearances": "Creates a new appearance for a guest in a specific episode."
        }
    }), 200

# Route to get all episodes
@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes]), 200

# Route to get a specific episode by ID
@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = db.session.get(Episode, id)  
    if episode:
        return jsonify(episode.to_dict()), 200
    return jsonify({"error": "Episode not found"}), 404

# Route to get all guests
@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests]), 200

# Route to get a specific guest by ID
@app.route('/guests/<int:id>', methods=['GET'])  
def get_guest(id):
    guest = db.session.get(Guest, id)  
    if guest:
        return jsonify(guest.to_dict()), 200
    return jsonify({"error": "Guest not found"}), 404

# Route to get all appearances
@app.route('/appearances', methods=['GET'])
def get_appearances():
    appearances = Appearance.query.all()
    return jsonify([appearance.to_dict() for appearance in appearances]), 200

# Route to get a specific appearance by ID
@app.route('/appearances/<int:id>', methods=['GET'])  
def get_appearance(id):
    appearance = db.session.get(Appearance, id)  
    if appearance:
        return jsonify(appearance.to_dict()), 200
    return jsonify({"error": "Appearance not found"}), 404

# Route to create a new appearance
@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()

    # Validate input
    if 'rating' not in data or 'episode_id' not in data or 'guest_id' not in data:
        return jsonify({"errors": ["Validation errors"]}), 400

    # Ensure rating is between 1 and 5
    if not (1 <= data['rating'] <= 5):
        return jsonify({"errors": ["Rating must be between 1 and 5"]}), 400

    # Create the new appearance
    new_appearance = Appearance(
        rating=data['rating'],
        episode_id=data['episode_id'],
        guest_id=data['guest_id']
    )

    db.session.add(new_appearance)
    
    try:
        db.session.commit()  
    except Exception as e:
        db.session.rollback()  
        return jsonify({"error": str(e)}), 500  

    return jsonify(new_appearance.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)  
