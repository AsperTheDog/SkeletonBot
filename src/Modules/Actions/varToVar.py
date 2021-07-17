from src.Modules.action import ActionManager


@ActionManager.actionClass
class VarToVar:
    def __init__(self, args, bot):
        self.var1 = args['var1']
        self.var2 = args['var2']
        self.varTo = args['varTo']
        self.comp = args['comp']

    async def execute(self, data):
        if self.comp == '+':
            return {self.varTo: data['vars'][self.var1] + data['vars'][self.var2]}
        if self.comp == '-':
            return {self.varTo: data['vars'][self.var1] - data['vars'][self.var2]}
        if self.comp == '/':
            return {self.varTo: data['vars'][self.var1] / data['vars'][self.var2]}
        if self.comp == '*':
            return {self.varTo: data['vars'][self.var1] * data['vars'][self.var2]}
        if self.comp == '^':
            return {self.varTo: data['vars'][self.var1] ** data['vars'][self.var2]}

    def serialize(self):
        return {
            'id': VarToVar.__name__,
            'args': {
                'varTo': self.varTo,
                'var1': self.var1,
                'var2': self.var2,
                'comp': self.comp
            }
        }