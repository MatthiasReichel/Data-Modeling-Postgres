import socket

def test_connection():
    """Test whether the postgres database is available. Usage:

        if "--offline" in sys.argv:
            os.environ['DJANGO_SETTINGS_MODULE'] = 'myapp.settings.offline'
        else:
            os.environ['DJANGO_SETTINGS_MODULE'] = 'myapp.settings.standard'
            from myapp.functions.connection import test_connection
            test_connection()
    """
    try:
        s = socket.create_connection(("localhost", 5432), 5)
        s.close()
        msg1 = """all good"""
        print(msg1)
    except socket.timeout:
        msg = """Can't detect the postgres server. If you're outside the
        intranet, you might need to turn the VPN on."""
        raise socket.timeout(msg)

test_connection()