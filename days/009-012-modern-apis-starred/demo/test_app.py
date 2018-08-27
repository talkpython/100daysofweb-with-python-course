from apistar import test

from app import app, cars, CAR_NOT_FOUND

client = test.TestClient(app)


def test_list_cars():
    response = client.get('/')
    assert response.status_code == 200

    json_resp = response.json()
    assert len(json_resp) == 1000

    expected = {'id': 1, 'manufacturer': 'Mercedes-Benz',
                'model': '500SEC', 'year': 1993,
                'vin': '1FTEW1CM9CF529793'}
    assert json_resp[0] == expected


def test_create_car():
    data = {'manufacturer': 'Honda',
            'model': 'some_model',
            'year': 2018}

    response = client.post('/', data=data)
    assert response.status_code == 201
    assert len(cars) == 1001

    response = client.get('/1001/')
    expected = {'id': 1001, 'manufacturer': 'Honda',
                'model': 'some_model', 'year': 2018, 'vin': ''}
    assert response.json() == expected

    data = {'manufacturer': 'Lotus',
            'model': 'some_other_model',
            'year': 2019,
            'vin': 123}
    response = client.post('/', data=data)
    assert response.status_code == 201
    expected = {'id': 1002, 'manufacturer': 'Lotus',
                'model': 'some_other_model', 'year': 2019,
                'vin': '123'}

    response = client.get('/1002/')
    assert response.json() == expected
    assert len(cars) == 1002


def test_create_car_missing_fields():
    data = {'key': 1}
    response = client.post('/', data=data)
    assert response.status_code == 400

    errors = response.json()
    assert errors['manufacturer'] == 'The "manufacturer" field is required.'
    assert errors['model'] == 'The "model" field is required.'
    assert errors['year'] == 'The "year" field is required.'


def test_create_car_field_validation():
    data = {'manufacturer': 'Opel',
            'model': 'x'*51,
            'year': 2051}
    response = client.post('/', data=data)
    assert response.status_code == 400

    errors = response.json()
    assert "Must be one of" in errors['manufacturer']
    assert errors['model'] == 'Must have no more than 50 characters.'
    assert errors['year'] == 'Must be less than or equal to 2050.'


def test_get_car():
    response = client.get('/777/')
    assert response.status_code == 200

    expected = {'id': 777, 'manufacturer': 'Ford',
                'model': 'Crown Victoria', 'year': 2004,
                'vin': '1G6DG577890380184'}
    assert response.json() == expected


def test_get_car_notfound():
    response = client.get('/11111/')
    assert response.status_code == 404
    assert response.json() == {'error': CAR_NOT_FOUND}


def test_update_car():
    data = {'manufacturer': 'Honda',
            'model': 'some_model',
            'year': 2018}
    response = client.put('/777/', data=data)
    assert response.status_code == 200

    # test put response
    expected = {'id': 777, 'manufacturer': 'Honda',
                'model': 'some_model', 'year': 2018, 'vin': ''}
    assert response.json() == expected

    # check if data persisted == wiped out previous data car 777
    response = client.get('/777/')
    assert response.json() == expected


def test_update_car_notfound():
    data = {'manufacturer': 'Honda',
            'model': 'some_model',
            'year': 2018}
    response = client.put('/11111/', data=data)

    assert response.status_code == 404
    assert response.json() == {'error': CAR_NOT_FOUND}


def test_update_car_validation():
    data = {'manufacturer': 'nonsense',
            'model': 's' * 51,
            'year': 1899}
    response = client.put('/777/', data=data)
    assert response.status_code == 400

    errors = response.json()
    assert "Must be one of" in errors['manufacturer']
    assert errors['year'] == 'Must be greater than or equal to 1900.'
    assert errors['model'] == 'Must have no more than 50 characters.'


def test_delete_car():
    car_count = len(cars)

    for i in (11, 22, 33):
        response = client.delete(f'/{i}/')
        assert response.status_code == 204

        response = client.get(f'/{i}/')
        assert response.status_code == 404  # car gone

    assert len(cars) == car_count - 3
