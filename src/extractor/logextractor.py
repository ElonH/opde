from src.parser.logparser import LogParser
from src.lexer.logs import LogTokenException
from pathlib import Path
import json
import sys


class LogsExtractor:
    '''
    extract info from log dir
    '''

    def __init__(self, LogDir: Path):
        self._parser = LogParser()

        self.logsAst = []
        for LogFile in LogDir.rglob('*.txt'):
            # download time shouldn't be considered in cost
            if LogFile.name in ['clean.txt', 'download.txt', 'error.txt',
                    'dump.txt', 'check-compile.txt', 'check-prereq.txt']:
                continue
            print(LogFile)
            try:
                ast = self._parser.gen_ast(LogFile.read_text(encoding='utf-8', errors='ignore'))
                if ast['exit-code'] == 0:  # if build success, clear build log to reduce database
                    ast['detail'] = ""
                self.logsAst.append(ast)
            except LogTokenException as e:
                print('%s --- parse failure' % LogFile.as_posix() , file=sys.stderr)

    def toJson(self):
        return json.dumps(self.logsAst, indent=2, sort_keys=False)
