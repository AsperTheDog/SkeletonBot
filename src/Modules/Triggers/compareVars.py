from src.Modules.trigger import TriggerManager


@TriggerManager.triggerClass
class CompareVars:
    def __init__(self, args):
        self.comp = args['comp']
        self.var1 = args['var1']
        self.var2 = args['var2']

    def check(self, data, variables):
        if self.comp == '>':
            return variables[self.var1] > variables[self.var2]
        elif self.comp == '>=':
            return variables[self.var1] >= variables[self.var2]
        elif self.comp == '==':
            return variables[self.var1] == variables[self.var2]
        elif self.comp == '<=':
            return variables[self.var1] <= variables[self.var2]
        elif self.comp == '<':
            return variables[self.var1] < variables[self.var2]

    def serialize(self):
        return {
            'id': CompareVars.__name__,
            'args': {
                'const': self.const,
                'var1': self.var1,
                'var2': self.var2
            }
        }
