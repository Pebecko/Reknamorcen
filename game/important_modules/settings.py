class Settings:
    def __init__(self, difficulty="hard"):
        self.difficulty = difficulty  # easy, medium, hard, nightmare
        self.print_time = 0  # 0.005
        self.print_break = 0.1
        self.test = False


settings = Settings()
