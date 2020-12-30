"""
__main__.py
Used to call jupydocs as a CLI tool. For example:

python -m jupydocs build

Inspiration was taken from spaCy
https://github.com/explosion/spaCy/blob/master/spacy/__main__.py
"""


if __name__ == "__main__":
    import sys
    import plac
    from wasabi import msg
    from jupydocs.cli import build
    
    commands = {
        'build': build
    }
    
    if len(sys.argv) == 1:
        msg.info("Available commands", ", ".join(commands), exits=1)
    command = sys.argv.pop(1)
    sys.argv[0] = "spacy %s" % command
    if command in commands:
        plac.call(commands[command], sys.argv[1:])
    else:
        available = "Available: {}".format(", ".join(commands))
        msg.fail("Unknown command: {}".format(command), available, exits=1)
    