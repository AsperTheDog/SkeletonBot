class ActionManager:
    actionList = {}

    @staticmethod
    def genAction(acType, args, bot):
        cls = ActionManager.actionList[acType]
        return cls(args, bot)

    @staticmethod
    def actionClass(cl):
        ActionManager.actionList[cl.__name__] = cl
        return cl
