class Task:  # TODO: 增加任务归属用户属性
    def __init__(self, status='has not started', description='None', priority='normal', deadline='None'):
        self.status = status
        self.content = []
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.label = None

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def set_content(self, content):
        self.content = content

    def get_content(self):
        return self.content

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_priority(self, priority):
        self.priority = priority

    def get_priority(self):
        return self.priority

    def set_deadline(self, deadline):
        self.deadline = deadline

    def get_deadline(self):
        return self.deadline

    def set_label(self, label):
        self.label = label

    def get_label(self):
        return self.label

    def get_info(self):
        return {'status': self.status, 'content': self.content, 'description': self.description,
                'priority': self.priority, 'deadline': self.deadline, "label": self.label}

    def get_data(self):
        return[self.status, self.content, self.description, self.priority, self.deadline, self.label]