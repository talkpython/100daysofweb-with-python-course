# Days 81 - 84 Unit testing web applications

In this your-turn, you'll jump back to the original app we built part way through our unit testing journey where the view models have been created but before any tests were written. You will add unit tests to the three levels of our app: view models (data exchange and validation), views (the actual view methods directly), and function (the app as a whole).

## Day 1: Watch the video lessons

The first day of this 4-day block is to watch the videos. Feel free to play around with the sample code and other projects while going through the videos. There is a lot of content here but we want to spend one day per type of test for the remaining three days so try to get through it in one here.

## Day 2: Test the view models with `unittest` and `mock.patch` 

Begin by loading and configuring the project in:

```
./billtracker_with_viewmodels/billtracker
```

This is the Pyramid web project as it was immediately before we started adding tests in the video. To configure it you'll need to.

1. Create a virtual environment in `./billtracker_with_viewmodels/billtracker` folder (`python3 -m venv venv` and activate it)
2. Install the requirements: `pip install -r requirements.txt`
3. Setup the project for development: `python setup.py develop`
4. Run it to see it's working well: `pserve development.ini`

Now that you have the site up and running, it's time to organize your tests and add the view model tests. Having a single `tests.py` file is a good start but is no where near enough. Create a tests folder, within there, a default folder. Put two test files in there, one for `index_viewmodel` and one for `bill_details_viewmodel` view models.

Write a couple of tests for each view model. Here is a rough example of what that might look like.

```python
class ViewModelTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_index_viewmodel(self):
        # AAA's

        # Arrange
        request: Request = testing.DummyRequest()
        test_user = User()
        test_user.id = 1
        test_user.bills = [Bill(), Bill(), Bill()]

        # Act
        with unittest.mock.patch('billtracker.data.repository.get_user_by_id',
                                 return_value=test_user):
            vm = IndexViewModel(request, user_id=1)

        # Assert
        self.assertIsNone(vm.error)
        self.assertIsNotNone(vm.user)
```

Remember that without the `mock.patch`, we would have to setup the database and use it during testing (not a great idea).

## Day 3: View tests

Now that you have done the view model tests, you are close to done with the view tests already. After all, they mostly just use the view models for their magic. 

But there are things to validate in the views. For example:

1. Requesting a bill detail that doesn't belong to user (user with ID 1 as we have it working, say bill 700), is a 404
2. Adding a payment to an open bill (e.g. bill 755) calls the `repository.add_payment` function with the correct values.

Here is an example of a view test (it's very similar to view models):


```
class HomeViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_details_get(self):
        from billtracker.views.default import details_get

        request: Request = testing.DummyRequest()
        user_id = 72
        request.matchdict['bill_id'] = 700

        mock_user = User()
        mock_user.id = user_id
        mock_user.bills = [Bill(), Bill(), Bill()]
        for b in mock_user.bills:
            b.user_id = user_id

        p1 = unittest.mock.patch('billtracker.data.repository.get_user_by_id',
                                 return_value=mock_user)
        p2 = unittest.mock.patch('billtracker.data.repository.get_bill_by_id',
                                 return_value=mock_user.bills[0])

        with p1, p2:
            info = details_get(request)

        self.assertIsNotNone(info['user'])
        self.assertGreater(len(info['user'].bills), 0)
```

Implement a few view tests (the cases laid out above would be good ones) for the views in our stater app.

## Day 4: Functional (end to end) tests

Final day is to do some functional tests. We'll leave it up to you on what you should test, but here is an example of a functional test. Keep in mind this IS using the database and the rest of the full web app to run the tests so may make changes over repeated runs.

Don't forget to install `webtest` if it's not already installed (`pip install webtest`).

```
# An example of a functional web test

class SiteTests(unittest.TestCase):
    def setUp(self):
        from billtracker import main
        app = main({})
        from webtest import TestApp
        self.app = TestApp(app)

    def test_root(self):
        res = self.app.get('/', status=200)
        self.assertTrue(b'Dannie Easom' in res.body)
        self.assertTrue(b'Unpaid bills' in res.body)
```

### Time to share what you've accomplished!

Be sure to share your last couple of days work on Twitter or Facebook. Use the hashtag **#100DaysOfWeb**. 

Here are [some examples](https://twitter.com/search?q=%23100DaysOfCode) to inspire you. Consider including [@talkpython](https://twitter.com/talkpython) and [@pybites](https://twitter.com/pybites) in your tweets.

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/100daysofweb-with-python-course/issues) or fix it and [submit a PR](https://github.com/talkpython/100daysofweb-with-python-course/pulls).*
