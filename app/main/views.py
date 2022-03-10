from flask import render_template, url_for, session
from flask import request as req
from werkzeug.utils import redirect
from flask_login import current_user

from app.main import main
from app.utils import format_pitches_array


@main.route('/')
def index():
    """Render the index template"""
    global pitches_filter
    try:
        pitches_filter = session["pitches_filter"]
    except KeyError:
        session["pitches_filter"] = "all"
        pitches_filter = session["pitches_filter"]
    from app.models import Pitch
    pitches = Pitch.query.all()
    formatted_pitches = format_pitches_array(pitches)
    return render_template('index.html', title="", pitches_filter=pitches_filter, pitches_list=formatted_pitches)


@main.route("/comments/<pitch_id>")
def view_comments(pitch_id):

    comment_txt = req.args.get("comment")

    if comment_txt:
        print(f"The comment is {comment_txt}")
        return render_template('comments/comments_list.html', title=f"Comments - {pitch_id}", text=f"{pitch_id}")
    else:
        return render_template('comments/comments_list.html', title=f"Comments - {pitch_id}", text=f"{pitch_id}")


@main.route('/new-pitch')
def new_pitch():
    pitch_txt = req.args.get("pitch_text")
    pitch_category = req.args.get("pitch_category")
    if pitch_txt:
        from app.utils import convert_category_to_num
        # pitch_category = convert_category_to_num(pitch_category)
        #
        if pitch_txt is not None and pitch_category is not None:
            from app.models import Pitch
            from datetime import datetime

            now = datetime.now()
            pitch = Pitch(pitch_txt=pitch_txt, creator_id=current_user.id, pitch_category=pitch_category,
                          comments="", upvt="", dwnvt="", timestamp=now.timestamp())
            from app import db
            db.session.add(pitch)
            db.session.commit()
            return redirect(url_for('main.index'))
        return redirect(url_for('main.index'))
    else:
        return render_template('forms/new_pitch.html')


@main.route('/users/<user_id>')
def go_to_profile(user_id):
    from app.models import User
    user = User.query.filter_by(id=user_id).first()
    return render_template('profile/profile.html', user=user, user_id=user_id)


@main.route('/category/<category_str>')
def go_to_pitches_category(category_str):

    if category_str == "interview_pitch":
        # todo Make a request for all the pitches with this category, after converting it to the db format
        return render_template('category_pitches.html', category=current_user.email)
    if category_str == "product_pitch":
        # todo Make a request for all the pitches with this category, after converting it to the db format
        return render_template('category_pitches.html', category=current_user)
    if category_str == "pickup_lines":
        # todo Make a request for all the pitches with this category, after converting it to the db format
        return render_template('category_pitches.html', category=current_user)
    if category_str == "promotion_pitch":
        # todo Make a request for all the pitches with this category, after converting it to the db format
        return render_template('category_pitches.html', category=current_user)
