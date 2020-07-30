from src.parser.logparser import LogParser
from pathlib import Path
import json


class LogsExtractor:
    '''
    extract info from log dir
    '''

    def __init__(self, LogDir: Path):
        self._parser = LogParser()

        self.logsAst = []
        for LogFile in LogDir.rglob('*.txt'):
            # download time shouldn't be considered in cost
            if LogFile.name in ['clean.txt', 'download.txt']:
                continue
            print(LogFile)
            ast = self._parser.gen_ast(LogFile.read_text())
            del ast['detail']  # for debug
            self.logsAst.append(ast)

    def toJson(self):
        return json.dumps(self.logsAst, indent=2, sort_keys=False)
