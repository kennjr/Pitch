from flask import render_template, url_for, session
from flask import request as req
from werkzeug.utils import redirect

from app.main import main


@main.route('/')
def index():
    """Render the index template"""
    global pitches_filter
    try:
        pitches_filter = session["pitches_filter"]
    except KeyError:
        session["pitches_filter"] = "all"
        pitches_filter = session["pitches_filter"]

    return render_template('index.html', title="", pitches_filter=pitches_filter)


@main.route("/comments/<pitch_id>")
def view_comments(pitch_id):
    title_str = f"Comments - {pitch_id}"
    return render_template('comments/comments_list.html', title=title_str, text=f"{pitch_id}")


@main.route('/new-pitch')
def new_pitch():
    pitch_txt = req.args.get("pitch_text")
    pitch_category = req.args.get("pitch_category")

    if pitch_txt:
        from app.utils import convert_category_to_num
        pitch_category = convert_category_to_num(pitch_category)
        print(f"The pitch is {pitch_txt} and the category is {pitch_category}")
        return redirect(url_for('main.index'))
    else:
        return render_template('forms/new_pitch.html')


@main.route('/users/<user_id>')
def go_to_profile(user_id):
    user = "Sth"
    return render_template('profile/profile.html', user=user, user_id=user_id)


@main.route('/category/<category_str>')
def go_to_pitches_category(category_str):

    if category_str == "interview_pitch":
        # todo Make a request for all the pitches with this category, after converting it to the db format
        return render_template('category_pitches.html', category=category_str)
    if category_str == "product_pitch":
        # todo Make a request for all the pitches with this category, after converting it to the db format
        return render_template('category_pitches.html', category=category_str)
    if category_str == "pickup_lines":
        # todo Make a request for all the pitches with this category, after converting it to the db format
        return render_template('category_pitches.html', category=category_str)
    if category_str == "promotion_pitch":
        # todo Make a request for all the pitches with this category, after converting it to the db format
        return render_template('category_pitches.html', category=category_str)
