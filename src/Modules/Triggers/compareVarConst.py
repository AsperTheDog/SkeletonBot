from src.Modules.trigger import TriggerManager


@TriggerManager.triggerClass
class CompareVarConst:
    def __init__(self, args):
        self.const = args['const']
        self.comp = args['comp']
        self.var = args['var']

    def check(self, data, variables):
        if self.comp == '>':
            return variables[self.var] > self.const
        elif self.comp == '>=':
            return variables[self.var] >= self.const
        elif self.comp == '==':
            return variables[self.var] == self.const
        elif self.comp == '<=':
            return variables[self.var] <= self.const
        elif self.comp == '<':
            return variables[self.var] < self.const

    def serialize(self):
        return {
            'id': CompareVarConst.__name__,
            'args': {
                'const': self.const,
                'comp': self.comp,
                'var': self.var
            }
        }
