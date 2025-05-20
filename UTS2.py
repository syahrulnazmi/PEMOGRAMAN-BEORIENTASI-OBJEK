class speaker:
    brand = "JBL"
    def __init__(self, model, color,):
        self.model = model
        self.color = color

speaker_one = speaker("JBL Charge 5", "Black")
speaker_two = speaker("JBL Flip 5", "Blue")
print(speaker_one.color, speaker_two.model)