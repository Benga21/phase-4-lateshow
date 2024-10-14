from flask import Blueprint, request, jsonify, redirect, url_for
from models import db, Episode

main_routes = Blueprint('main', __name__)

# Home page: return a list of episodes
@main_routes.route('/')
def home():
    episodes = Episode.query.all()
    episode_list = [{
        'id': episode.id,
        'date': episode.date,
        'number': episode.number
    } for episode in episodes]
    
    return jsonify(episode_list)

# Add a new episode
@main_routes.route('/add_episode', methods=['POST'])
def add_episode():
    date = request.form['date']
    number = request.form['number']

    new_episode = Episode(date=date, number=int(number))
    db.session.add(new_episode)
    db.session.commit()

    return redirect(url_for('main.home'))

# Update an existing episode
@main_routes.route('/update_episode', methods=['POST'])
def update_episode():
    episode_id = request.form['id']
    new_date = request.form['date']
    new_number = request.form['number']

    episode = Episode.query.get(episode_id)
    if episode:
        episode.date = new_date
        episode.number = int(new_number)
        db.session.commit()

    return redirect(url_for('main.home'))

# View details of a specific episode
@main_routes.route('/episode/<int:id>')
def episode_details(id):
    episode = Episode.query.get(id)

    if episode:
        episode_data = {
            'id': episode.id,
            'date': episode.date,
            'number': episode.number
        }
        return jsonify(episode_data)
    else:
        return jsonify({"error": "Episode not found"}), 404
