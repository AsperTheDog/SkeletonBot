class TriggerManager:
    triggerList = {}

    @staticmethod
    def genTrigger(trType, args):
        cls = TriggerManager.triggerList[trType]
        return cls(args)

    @staticmethod
    def triggerClass(cl):
        TriggerManager.triggerList[cl.__name__] = cl
        return cl
