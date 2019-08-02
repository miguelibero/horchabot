import os
from flask import Flask, render_template, Response, jsonify, request
from horchabot.camera import VideoCamera


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.camera = None
    app.frame = None

    @app.route('/')
    def index():
        return render_template('index.html')

    def video_stream():
        if app.camera is None:
            app.camera = VideoCamera()
        
        while True:
            frame = app.camera.get_frame()

            if frame != None:
                app.frame = frame
            if not app.frame:
                raise Exception("no video frame")
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + app.frame + b'\r\n\r\n')

    @app.route('/video')
    def video():
        return Response(video_stream(),
                mimetype='multipart/x-mixed-replace; boundary=frame')
    

    return app
