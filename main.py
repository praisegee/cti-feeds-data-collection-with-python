import sys

from decouple import config

import core.server as server
from core.database import Base, engine

from core.feeds.open_source.abuse_ch import AbuseCH


def usage():
    info = """
    Usage: python main.py [feeds | server]
    
    feeds:
        - Fetch data from CTI feeds and store it into database.
    
    server: 
        - Start Flask App server.
    
    example:
        `python main.py feeds`
        `python main.py server`
           
    """
    return info


def main(args: list[str]):

    if not args:
        sys.stderr.write(usage())
        sys.exit(1)

    # Create all tables defined by the models
    Base.metadata.create_all(engine)

    match args[0]:
        # handles arguments passed
        case "server":
            # env vars
            host = config("SERVER_HOST", default="localhost")
            port = config("SERVER_PORT", default=8000)
            debug = config("DEBUG", default=True, cast=bool)

            # Run Flask Server with the default port
            server.app.run(host=host, port=port, debug=debug)

        case "feeds":
            # TODO: handles the api fetching from CTI feeds
            ...
            # AbuseCH().save_to_db()

        case _:
            sys.stderr.write(usage())
            sys.exit(1)


if __name__ == "__main__":
    # print(sys.argv[1:])
    main(sys.argv[1:])
