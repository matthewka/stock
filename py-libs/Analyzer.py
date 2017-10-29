import sys
sys.path.append("./py-libs/analyzers")
import talib as ta
from AnalyzerA import AnalyzerA

class Analyzer(object):
    def run(self):
        analyzer = AnalyzerA()
        analyzer.analyze()

