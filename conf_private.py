## PRIVATE CALDAV SERVER(S) TO RUN TESTS TOWARDS
## Make a list of your own servers/accounts that you'd like to run the
## test towards.  Running the test suite towards a personal account
## should generally be safe, it should not mess up with content there
## and it should clean up after itself, but don't sue me if anything
## goes wrong ...

caldav_servers = [
    {
        ## This is all that is really needed - url, username and
        ## password.  The username and password may also be passed in
        ## the URL itself (like
        ## https://sam_i_am:hunter2@server.example.ccom/)
	'url': 'https://mail.tueit.de/SOGo/dav',
        'username': 'marius.widmann@tueit.de',
        'password': '2f4bEc7N2h8nO2PgNVL1',

	## skip ssl cert verification, for self-signed certificates
	## (sort of moot nowadays with letsencrypt freely available)
        #'ssl_cert_verify': False

	## There are some boolean options that may be passed i.e. to
	## skip tests (many CalDAV server features are marked as
	## optional in the RFC, for one thing), to skip verifying SSL
	## certificate, etc.  Leave the list blank on first attempt, then
	## add things as needed (see also compatibility_issues.py)
	#'nocalendarnotfound': True,
	#'nodefaultcalendar: True,
	#'nodisplayname: True,
	#'noproxy': True,
        #'nojournal': True,
	#'nofreebusy': True.
	#'notodo': True,
	#'nopropfind': True,
	#'norecurring': True,
	#'norecurringexpandation': True,
	#'noexpand': True,
	#'calendarcolor': True
	#'calendarorder': True
    }]

## MASTER SWITCHES FOR TEST SERVER SETUP
## With those configuration switches, pre-configured test servers in conf.py
## can be turned on or off

## test_public_test_servers - Use the list of common public test
## servers from conf.py.  This has proven to be unreliable and
## fragile, hence the default has now been flipped to False.  It's
## very important to run through all the different server
## implementations and try to figure out of all breakages before any
## major release - and it ought to be done before any minor release as well.
test_public_test_servers = False

## test_private_test_servers - test using the list configured above in this file.
test_private_test_servers = True

## test_xandikos - since the xandikos caldav server implementation is
## written in python and can be instantiated quite easily, this will
## be the default caldav implementation to test towards ... but, unfortunately
## it works only with python 3.4 and higher
test_xandikos = True

## DEPRECATED - only_private is superceded by test_public_servers,
## left here for backward-compatibility.
#only_private=False
