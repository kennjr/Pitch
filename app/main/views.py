from flask import render_template, url_for, session
from flask import request as req
from werkzeug.utils import redirect
from flask_login import current_user

from app.main import main
from app.utils import format_pitches_array, convert_lowercase_category_to_num, format_comments_array


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
        from app.models import Comment
        if comment_txt is not None:
            from datetime import datetime

            now = datetime.now()
            comment = Comment(comment_txt=comment_txt, creator_id=current_user.id, pitch_id=pitch_id,
                              timestamp=now.timestamp())
            from app.models import Pitch

            from app import db
            db.session.add(comment)
            # pitch = Pitch.query().filter(Pitch.id == pitch_id).first()
            pitch = Pitch.query.filter_by(id=pitch_id).first()
            setattr(pitch, 'comments', Pitch.comments + ",1")
            db.session.commit()

        # comments = Comment.query.filter_by(pitch_id=pitch_id)
        # comments_list = format_comments_array(comments)
        return redirect(url_for('main.view_comments', pitch_id=pitch_id))
        # return render_template('comments/comments_list.html', title=f"Comments - {pitch_id}", comments_list=comments_list)
    else:
        from app.models import Comment
        comments = Comment.query.filter_by(pitch_id=pitch_id)
        comments_list = format_comments_array(comments)
        return render_template('comments/comments_list.html', title=f"Comments - {pitch_id}", comments_list=comments_list)


@main.route('/new-pitch')
def new_pitch():
    pitch_txt = req.args.get("pitch_text")
    pitch_category = req.args.get("pitch_category")
    if pitch_txt:
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
        from app.models import Pitch
        formatted_category = convert_lowercase_category_to_num(category_str)
        pitches = Pitch.query.filter_by(pitch_category=formatted_category)
        formatted_pitches = format_pitches_array(pitches)

        return render_template('category_pitches.html', category=current_user.email, pitches_list=formatted_pitches)
    if category_str == "product_pitch":
        from app.models import Pitch
        formatted_category = convert_lowercase_category_to_num(category_str)
        pitches = Pitch.query.filter_by(pitch_category=formatted_category)
        formatted_pitches = format_pitches_array(pitches)

        return render_template('category_pitches.html', category=current_user.email, pitches_list=formatted_pitches)
    if category_str == "pickup_lines":
        from app.models import Pitch
        formatted_category = convert_lowercase_category_to_num(category_str)
        pitches = Pitch.query.filter_by(pitch_category=formatted_category)
        formatted_pitches = format_pitches_array(pitches)

        return render_template('category_pitches.html', category=current_user.email, pitches_list=formatted_pitches)
    if category_str == "promotion_pitch":
        from app.models import Pitch
        formatted_category = convert_lowercase_category_to_num(category_str)
        pitches = Pitch.query.filter_by(pitch_category=formatted_category)
        formatted_pitches = format_pitches_array(pitches)

        return render_template('category_pitches.html', category=current_user.email, pitches_list=formatted_pitches)
