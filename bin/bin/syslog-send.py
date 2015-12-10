#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Send test message to syslog server

Usage:
    syslog-send.py [--rfc3164 --rfc5424] [-s SERVER] [-p PORT]
                   [--hostname HOSTNAME] [--programname PROGRAMNAME]
                   [--app-name APPNAME]

Options:
    -1, --rfc3164               rfc3164 protocol: https://tools.ietf.org/html/rfc3164
    -2, --rfc5424               rfc5424 protocol: https://tools.ietf.org/html/rfc5424
    -s SERVER, --server SERVER  Remote syslog server                [default: localhost]
    -p PORT, --port PORT        Remote udp port                     [default: 514]
    --hostname HOSTNAME         HOSTNAME field for rfc3164, rfc5424 [default: myhostname]
    --programname PROGRAMNAME   PROGRAMNAME field for rfc3164       [default: myprogramname]
    --app-name APPNAME          APP-NAME field for rfc5424          [default: myappname]
"""

import logging
import logging.handlers
from datetime import datetime
from docopt import docopt

def send_log(template, config):
    message = template.format(**config)

    for k, v in config.items():
        print('  {0:10} {1}'.format(k, v))
    print('  {0:10} {1}'.format('Template', template))
    print('  {0:10} {1}'.format('Message', message))
    logging.info(message)

if __name__ == '__main__':
    args = docopt(__doc__)

    if not (args['--rfc3164'] or args['--rfc5424']):
        print(__doc__)
        exit(1)

    rootLogger = logging.getLogger('')
    rootLogger.setLevel(logging.DEBUG)
    socketHandler = logging.handlers.SysLogHandler(address=(args['--server'], int(args['--port'])))
    rootLogger.addHandler(socketHandler)

    if args['--rfc3164']:
        config_rfc3164 = {
            'DATE': datetime.strftime(datetime.now(), '%b %d %H:%M:%S'),
            'HOSTNAME': args['--hostname'],
            'TAG': '{0}[999]:'.format(args['--programname']),
            'MSG': 'rfc3164 test logger message',
            }
        template_rfc3164 = '{DATE} {HOSTNAME} {TAG} {MSG}'
        print('Send message with rfc3164 format')
        send_log(template_rfc3164, config_rfc3164)

    if args['--rfc5424']:
        config_rfc5424 = {
            'VERSION': '1',
            'DATE': datetime.strftime(datetime.now(), '%Y-%m-%dT%H:%M:%SZ'),
            'HOSTNAME': args['--hostname'],
            'APP-NAME': args['--app-name'],
            'PROCID': '999',
            'MSGID': 'MSGID',
            'MSG': 'rfc5424 test logger message в юникоде'
            }
        template_rfc5424 = '{VERSION} {DATE} {HOSTNAME} {APP-NAME} {PROCID} {MSGID} {MSG}'
        print('Send message with rfc5424')
        send_log(template_rfc5424, config_rfc5424)
