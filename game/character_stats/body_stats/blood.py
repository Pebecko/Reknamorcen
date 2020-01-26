class Blood:
    def __init__(self, body_mass):
        self.maximal_blood_amount = 0
        self.minimal_blood_amount = 0
        self.actual_blood_amount = 0

        self.setting_base_blood_levels(body_mass)

    def setting_base_blood_levels(self, body_mass):
        self.maximal_blood_amount = body_mass * 0.08
        self.actual_blood_amount = self.maximal_blood_amount
        self.minimal_blood_amount = self.maximal_blood_amount * 0.75
