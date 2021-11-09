r"""Command-line tool to validate and pretty-print Dict

Usage::

    $ echo '{"feapson":"obj"}' | python -m feapson.tool
    {
        "feapson": "obj"
    }
    $ echo '{ 1.2:3.4}' | python -m feapson.tool
    Expecting property name enclosed in double quotes: line 1 column 3 (char 2)

"""
import argparse
import feapson
import sys


def main():
    prog = 'python -m feapson.tool'
    description = ('A simple command line interface for feapson module '
                   'to validate and pretty-print Dict objects.')
    parser = argparse.ArgumentParser(prog=prog, description=description)
    parser.add_argument('infile', nargs='?',
                        type=argparse.FileType(encoding="utf-8"),
                        help='a Dict file to be validated or pretty-printed',
                        default=sys.stdin)
    parser.add_argument('outfile', nargs='?',
                        type=argparse.FileType('w', encoding="utf-8"),
                        help='write the output of infile to outfile',
                        default=sys.stdout)
    parser.add_argument('--sort-keys', action='store_true', default=False,
                        help='sort the output of dictionaries alphabetically by key')
    parser.add_argument('--no-ensure-ascii', dest='ensure_ascii', action='store_false',
                        help='disable escaping of non-ASCII characters')
    parser.add_argument('--feapson-lines', action='store_true', default=False,
                        help='parse input using the Dict Lines format. '
                        'Use with --no-indent or --compact to produce valid Dict Lines output.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--indent', default=4, type=int,
                       help='separate items with newlines and use this number '
                       'of spaces for indentation')
    group.add_argument('--tab', action='store_const', dest='indent',
                       const='\t', help='separate items with newlines and use '
                       'tabs for indentation')
    group.add_argument('--no-indent', action='store_const', dest='indent',
                       const=None,
                       help='separate items with spaces rather than newlines')
    group.add_argument('--compact', action='store_true',
                       help='suppress all whitespace separation (most compact)')
    options = parser.parse_args()

    dump_args = {
        'sort_keys': options.sort_keys,
        'indent': options.indent,
        'ensure_ascii': options.ensure_ascii,
    }
    if options.compact:
        dump_args['indent'] = None
        dump_args['separators'] = ',', ':'

    with options.infile as infile, options.outfile as outfile:
        try:
            if options.json_lines:
                objs = (feapson.loads(line) for line in infile)
            else:
                objs = (feapson.load(infile),)
            for obj in objs:
                feapson.dump(obj, outfile, **dump_args)
                outfile.write('\n')
        except ValueError as e:
            raise SystemExit(e)


if __name__ == '__main__':
    try:
        main()
    except BrokenPipeError as exc:
        sys.exit(exc.errno)
