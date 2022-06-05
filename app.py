import datetime
from flask import Flask, render_template, request, url_for
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from datetime import datetime
from dateutil.relativedelta import relativedelta
# to get image size
from PIL import Image

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.utcnow())


@app.route('/hehe/')
def hehe():
    return render_template('hehe.html')

@app.route('/about/')
def about():
    return render_template('about.html')

    
@app.route('/comments/')
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments.html', comments=comments)

    
@app.route('/comments2/')
def comments2():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments2.html', comments=comments)

    
@app.route('/comments3/')
def comments3():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments3.html', comments=comments)


@app.route('/list/')
def building_list():
    return render_template('list.html')


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/reservations/')
def reservations():
    return render_template('reservations.html')



@app.route('/rooms/')
def rooms_empty():
    return 'not found'

@app.route('/rooms/<id>/<selected_floor_number>', methods=["GET", "POST"])
def rooms(id, selected_floor_number):
    class Room:
        def __init__(self, name, id, XYs, isFree = False):
            self.name = name
            self.id = id
            self.XYs = XYs
            self.isFree = isFree # jak jest zaznaczona godzina to to potrzebne, jak nie to nie zamierzam patrzyc


    if request.method == 'POST':
        print(str(request.form))


    class WybranaGodzina:
        def __init__(self, start_date, end_date):
            self.start_date = start_date
            self.end_date = end_date
    wybrana_godzina = None
    wybrana_godzina = WybranaGodzina(1, 2)


    chosen_room_id = 100
    chosen_room = 1
    if request.method == 'POST':
        try:
            chosen_room_id = request.form['room_id']
            chosen_room = Room('rum', 5, 'hehe wspolrzedne', True) # todo chosen room
            print("chosen room id 1: " + str(chosen_room_id))
        except:
            chosen_room_id = None
            chosen_room = None
            print("chosen room id 2: " + str(chosen_room_id))
    else:
        chosen_room_id = None
        chosen_room = None
        print("chosen room id 3: " + str(chosen_room_id))
    print("chosen room id 4: " + str(chosen_room_id))

    try:
        filename = f"{id}_{selected_floor_number}.png"
        im = Image.open(f"./static/{filename}")
    except:
        filename = f"{id}_{selected_floor_number}.jpg"
        im = Image.open(f"./static/{filename}")
    width, height = im.size
    print("width: " + str(width))
    print("height: " + str(height))
    print("filename: " + str(filename))
    print("id: " + str(id))

    class XY:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        # musialem zdefiniowac wyzej =P
    # class Room:
    #     def __init__(self, name, id, XYs, isFree = False):
    #         self.name = name
    #         self.id = id
    #         self.XYs = XYs
    #         self.isFree = isFree # jak jest zaznaczona godzina to to potrzebne, jak nie to nie zamierzam patrzyc

    class Floor:
        def __init__(self, building_id, number=0, rooms=None, image_size_x=width, image_size_y=height):#, image_size_x=781, image_size_y=879):
            self.building_id = building_id
            self.number = number
            self.rooms = rooms
            self.image_size_x = image_size_x
            self.image_size_y = image_size_y

    class Mock_Building:
        def __init__(self, name, id, floors):
            self.name = name
            self.id = id
            self.floors = floors

    mock_XYs = [XY(157, 112), XY(164, 112), XY(166, 128), XY(216, 122), XY(214, 101), XY(192, 101), XY(193, 92), XY(182, 92), XY(182, 100), XY(164, 103), XY(156, 104)]
    mock_room = Room('room1', 1, mock_XYs)
    mock_XYs_1_2 = [XY(169, 135), XY(158, 138), XY(159, 147), XY(169, 148), XY(169, 166), XY(158, 168), XY(160, 176), XY(169, 177), XY(171, 181), XY(220, 177), XY(220, 168), XY(224, 165), XY(224, 147), XY(218, 142), XY(217, 129)]
    mock_room_1_2 = Room('room1_2', 2, mock_XYs_1_2, True)
    mock_floor_1_1 = Floor(1, 1, [mock_room, mock_room_1_2])

    mock_XYs_2 = [XY(169, 135), XY(158, 138), XY(159, 147), XY(169, 148), XY(169, 166), XY(158, 168), XY(160, 176), XY(169, 177), XY(171, 181), XY(220, 177), XY(220, 168), XY(224, 165), XY(224, 147), XY(218, 142), XY(217, 129)]
    mock_room_2 = Room('room2', 2, mock_XYs_2)
    mock_floor_1_2 = Floor(1, 2, [mock_room_2])

    mock_XYs_3 = [XY(226, 317.0500030517578), XY(226, 341.0500030517578), XY(235, 343.0500030517578), XY(235, 370.6666717529297), XY(223, 373.6666717529297), XY(270, 483.6666717529297), XY(334, 621.6666870117188), XY(341, 616.6666870117188), XY(346, 625.6666870117188), XY(538, 585.6666870117188), XY(522, 223), XY(420, 213), XY(420, 220), XY(398, 218.5), XY(397, 211.5), XY(248, 201), XY(249, 297.6666717529297)]
    mock_room_3 = Room('room3', 3, mock_XYs_3)
    mock_floor_2_1 = Floor(1, 'parter kurde', [mock_room_3])

    if int(id) == 1:
        my_mock_building = Mock_Building('building1', id, [mock_floor_1_1, mock_floor_1_2])
    else:
        my_mock_building = Mock_Building('building2', id, [mock_floor_2_1])
    
    date = datetime.today()
    date_after_month = datetime.today() + relativedelta(months=1)

    return render_template('rooms.html', 
                            mock_building=my_mock_building, 
                            id=id, 
                            selected_floor_number=selected_floor_number, 
                            date=date.strftime("%Y-%m-%d"), 
                            date_after_month=date_after_month.strftime("%Y-%m-%d"),
                            filename=filename,
                            isTimeSet=(wybrana_godzina is not None),
                            chosen_room_id=chosen_room_id,
                            chosen_room=chosen_room
                            )


@app.route('/mapa/', methods=["GET", "POST"])
def mapa():
    if request.method == 'POST':
        print(str(request.form))


    class WybranaGodzina:
        def __init__(self, start_date, end_date):
            self.start_date = start_date
            self.end_date = end_date
    wybrana_godzina = None
    
    class Node:
        def __init__(self, name, id, lat, lon):
            self.name = name
            self.id = id
            self.lat = lat
            self.lon = lon

    # if request.method == "POST":
    if wybrana_godzina is None: # wszystkie budynki
        mock_nodes = [
            Node("budynek 1", 1, 50.05439045165468, 19.93637152232552),
            Node("Katedra Wawelska / budynek 2", 2, 50.054686658718666, 19.935633914868227)
        ]
    else: # te budynki co maja cos w danych godzinach
        mock_nodes = [
            Node("budynek 1", 1, 50.05439045165468, 19.93637152232552)
        ]

    # Initialize variables
    id_counter = 0
    markers = ''
    for node in mock_nodes:
        # Create unique ID for each marker
        idd = 'budynek' + str(id_counter)
        id_counter += 1

        # Check if shops have name and website in OSM
        try:
            name = node.name
        except:
            name = 'null'

        try:
            id = node.id
        except:
            id = 'null'


        # # Create the marker and its pop-up for each shop
        # markers += "var {idd} = L.marker([{latitude}, {longitude}]);\
        #             {idd}.addTo(map).bindPopup('{brand}<br>{website}');".format(idd=idd, latitude=node.lat,\
        #                                                                             longitude=node.lon,
        #                                                                             brand=name,\
        #                                                                             website=url_for('building_list'))#id)

        # Create the marker and its pop-up for each shop
        markers += "var {idd} = L.marker([{latitude}, {longitude}]);\
                    {idd}.addTo(map).bindPopup('{brand}<br><a href=\"{website}\">rezerwuj</a>');".format(idd=idd, latitude=node.lat,\
                                                                                    longitude=node.lon,
                                                                                    brand=name,\
                                                                                    website=url_for('rooms', id=id, selected_floor_number=1)
                                                                                    )


    # The code here determines what happens after sumbitting the form
    
    date = datetime.today()
    date_after_month = datetime.today() + relativedelta(months=1)

    return render_template('/mapa.html', markers=markers, lat=request.form.get('lat'), lon=request.form.get('lon'), date=date.strftime("%Y-%m-%d"), date_after_month=date_after_month.strftime("%Y-%m-%d"))
    # else:
    #     # Render the input form
    #     return render_template('/tak/input.html')



class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)