from src.Modules.action import ActionManager


@ActionManager.actionClass
class ConstToVar:
    def __init__(self, args, bot):
        self.var1 = args['var1']
        self.varTo = args['varTo']
        self.const = args['const']
        self.comp = args['comp']

    async def execute(self, data):
        if self.comp == '+':
            return {self.varTo: data['vars'][self.var1] + self.const}
        if self.comp == '-':
            return {self.varTo: data['vars'][self.var1] - self.const}
        if self.comp == '/':
            return {self.varTo: data['vars'][self.var1] / self.const}
        if self.comp == '*':
            return {self.varTo: data['vars'][self.var1] * self.const}
        if self.comp == '^':
            return {self.varTo: data['vars'][self.var1] ** self.const}

    def serialize(self):
        return {
            'id': ConstToVar.__name__,
            'args': {
                'var1': self.var1,
                'varTo': self.varTo,
                'const': self.const,
                'comp': self.comp
            }
        }