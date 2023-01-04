"""
Model classes for the paralympic cycling app.
"""
from datetime import datetime


class Competition:
    def __init__(self, comp_name: str, start_date: datetime, end_date: datetime, comp_type: str, data: list):
        """

        :param comp_name: Name or reference for the competition
        :param start_date: When the competition allows entries
        :param end_date: When the competition closes so no further entries allowed
        :param comp_type: Type of competition (Country, Event Medallists, Participant Performance)
        :param data: The details of the competition TODO: These details are not yet known, likely to be separate params
        """
        self.comp_name = comp_name
        self.start_date = start_date
        self.end_date = end_date
        self.comp_type = comp_type
        self.data = [data]
        self.entries = []

    def __repr__(self):
        """
        Returns the attributes of the competition as a string
        :returns str
        """
        return f'Competition name: {self.comp_name}, start: {self.start_date}, end: {self.end_date},' \
               f' type: {self.comp_type}, data: {str(self.data)}'


class Entry:
    def __init__(self, entry_data: list):
        """
        A competition entry

        :param entry_data: The actual data will depend on the competition that has been created
        """
        self.entry_data = [entry_data]
        self._is_winner = False

    def __repr__(self):
        """
        Returns the attributes of an Entry as a string
        :returns str
        """
        return f'Entry data: {str(self.entry_data)}, is winner? {self._is_winner}'

    @property
    def is_winner(self):
        return self._is_winner

    @is_winner.setter
    def is_winner(self, has_won: bool):
        """
        If this entry is a winning entry, change _is_winner to True
        :param has_won:
        :return: self._is_winner=True
        """
        self._is_winner = True

    def db_create(self):
        """
        Creates a new record in the database.
        Note: we won't do it this way when we use Flask-SQLAlchemy, this is just to give use some methods to test
        """
        return print('Saved to the database')

    def db_read(self):
        """
        Reads a new record from the database.
        Note: we won't do it this way when we use Flask-SQLAlchemy, this is just to give use some methods to test
        """
        return print('Entry updated in the database')

    def db_update(self):
        """
        Creates a new record in the database.
        Note: we won't do it this way when we use Flask-SQLAlchemy, this is just to give us some methods to test
        """
        return print('Entry updated in the database')

    def db_delete(self):
        """
        Deletes a new record in the database.
        Note: we won't do it this way when we use Flask-SQLAlchemy, this is just to give us some methods to test
        """
        return print('Entry deleted from the database')


class User:
    def __init__(self, username: str, password: str, role='public'):
        """

        :param username: Provided by the user
        :param password: Provided by the user
        :param role: Set by default to public, should be set as marketing for marketing staff
        """
        self.username = username
        self.password = password
        self.role = role
        self._is_logged_in = False

    def __repr__(self):
        """
        Returns the attributes of an User as a string (except password)
        :returns str
        """
        return f'User with username {self.username}, role {self.role}, and is_logged_in = {self._is_logged_in}'

    @property
    def is_logged_in(self):
        return self._is_logged_in

    @is_logged_in.setter
    def is_logged_in(self, status: bool):
        """
        If the user is not logged in, log them in, otherwise log them out
        Note: this is not how we will implement login functionality for Flask but will suffice for this example
        :param status: Boolean
        :return: sets _is_logged_in to either True or False depending on the value passed
        """
        self._is_logged_in = status

    def login(self, username, password):
        """
        Query the database and check if the username and password match, if they do then the status changes to logged in
        Note: This is not how to handle login for Flask! Added here just to provide code for the unit testing activity
        """
        # Database query logic here, for now assume the userid and password are valid
        self.is_logged_in = True

    def logout(self):
        """
        Logs out a user if they are logged in
        Note: This is not how to handle logout for Flask! Added here just to provide code for the unit testing activity
        """
        self.is_logged_in = True


class GeneralPublic(User):
    def __init__(self, username: str, password: str, email: str, phone: str):
        super().__init__(username, password)
        self.email = email
        self.phone = phone

    def __repr__(self):
        """
        Returns the attributes of an General Public user as a string (except password)
        :returns str
        """
        return f'GeneralPublic with username {self.username}, role {self.role}, is logged in ' \
               f'= {self._is_logged_in}, ' \
               f'email {self.email}, phone {self.phone}'

    def enter_Competition(self, data, competition: Competition):
        """
        Creates an entry object and adds it to the entries for the competition
        TODO: Probably a route controller rather than a class method (entry does not require an account!)
        The code is not implemented correctly, this is just placeholder code to give something to test.
        :param competition: The competition to which the entry is for
        :param data: Entry data (varies depending on the competition)

        """
        e_d = [data]
        e = Entry(entry_data=e_d)
        c = competition
        c.entries.append(e)
        e.db_create()
