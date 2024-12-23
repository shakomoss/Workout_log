from flask import Flask, render_template, request, redirect, url_for
from models import db, Workout
from dotenv import load_dotenv
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost:5432/Workout_log')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    workouts =  Workout.query.all()
    return render_template('index.html', workouts=workouts)

@app.route('/add', methods=['GET','POST'])
def add_workout():
    if request.method == 'POST':
        workout_type = request.form['type']
        duration = int(request.form['duration'])
        calories = int(request.form['calories'])
        user_id = int(request.form['user_id'])
        exercise = request.form['exercise']
        currentstat = int(request.form['currentstat'])
        new_workout = Workout(type=workout_type,exercise=exercise,currentstat=currentstat, duration=duration, calories=calories,user_id=user_id)
        db.session.add(new_workout)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_workout.html')

@app.route('/delete_workout/<int:id>', methods=['GET','POST'])
def delete_workout(id):
    workout = Workout.query.get_or_404(id)
    db.session.delete(workout)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

try:
    db.session.commit()
except Exception as e:
    db.session.rollback()
    print(f"Error: {e}")
            