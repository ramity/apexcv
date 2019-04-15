class Config:
    projectPath = "/var/src/"

    def getProjectPath(self):
        return self.projectPath

    def setProjectPath(self, projectPath):
        self.projectPath = projectPath
        return self
