from time import sleep

from gpiozero import PWMLED, Button
from random import randint

INCANTATION_OF_THE_IRON_SOUL = 1
LITANY_OF_THE_ELECTROMANCER = 2
CHANT_OF_THE_REMORSELESS_FIST = 3
SHROUDPSALM = 4
INVOCATION_OF_MACHINE_MIGHT = 5
BENEDICTION_OF_THE_OMNISSIAH = 6


class KillTeam:

    def __init__(self):
        self.plusButton = Button(17)
        self.minusButton = Button(27)
        self.okButton = Button(22)

        self.canticleLed1 = PWMLED(5)  # IncantationOfTheIronSoul
        self.canticleLed2 = PWMLED(6)  # LitanyOfTheElectromancer
        self.canticleLed3 = PWMLED(13)  # Chant of the Remorseless Fist
        self.canticleLed4 = PWMLED(19)  # Shroudpsalm
        self.canticleLed5 = PWMLED(26)  # Invocation of Machine Might
        self.canticleLed6 = PWMLED(21)  # Benediction of the Omnissiah

        self.initiativeLed = PWMLED(23)
        self.movementLed = PWMLED(24)
        self.psychicLed = PWMLED(25)
        self.shootingLed = PWMLED(12)
        self.meleeLed = PWMLED(16)
        self.moraleLed = PWMLED(20)

        self.selected_canticle = INCANTATION_OF_THE_IRON_SOUL
        self.canticle1Used = False
        self.canticle2Used = False
        self.canticle3Used = False
        self.canticle4Used = False
        self.canticle5Used = False
        self.canticle6Used = False

        self.continueGame = True

    def select_canticles(self):
        self.initiativeLed.off()
        self.movementLed.off()
        self.psychicLed.off()
        self.shootingLed.off()
        self.meleeLed.off()
        self.moraleLed.off()

        self.plusButton.when_pressed = self.canticle_plus_button
        self.minusButton.when_pressed = self.canticle_minus_button
        self.okButton.when_pressed = self.canticle_ok_button

        self.display_canticle()

        self.okButton.wait_for_press()

        self.plusButton.when_pressed = None
        self.minusButton.when_pressed = None
        self.okButton.when_pressed = None
        sleep(0.5)

    def canticle_plus_button(self):
        self.selected_canticle += 1
        if self.selected_canticle < 7:
            if self.selected_canticle == 8:
                self.selected_canticle = INCANTATION_OF_THE_IRON_SOUL
        self.display_canticle()

    def canticle_minus_button(self):
        self.selected_canticle -= 1
        if self.selected_canticle > 0 or self.selected_canticle == -1:
            if self.selected_canticle == -1:
                self.selected_canticle = BENEDICTION_OF_THE_OMNISSIAH
        self.display_canticle()

    def canticle_ok_button(self):
        if self.selected_canticle == 0 or self.selected_canticle == 7:
            self.selected_canticle = randint(1, 6)
        else:
            if self.selected_canticle == INCANTATION_OF_THE_IRON_SOUL:
                self.canticle1Used = True
            elif self.selected_canticle == LITANY_OF_THE_ELECTROMANCER:
                self.canticle2Used = True
            elif self.selected_canticle == CHANT_OF_THE_REMORSELESS_FIST:
                self.canticle3Used = True
            elif self.selected_canticle == SHROUDPSALM:
                self.canticle4Used = True
            elif self.selected_canticle == INVOCATION_OF_MACHINE_MIGHT:
                self.canticle5Used = True
            elif self.selected_canticle == BENEDICTION_OF_THE_OMNISSIAH:
                self.canticle6Used = True
        self.display_canticle(True)

    def initiative_phase(self):
        self.initiativeLed.on()
        self.movementLed.off()
        self.psychicLed.off()
        self.shootingLed.off()
        self.meleeLed.off()
        self.moraleLed.off()

        self.plusButton.when_pressed = None
        self.minusButton.when_pressed = None
        self.okButton.when_pressed = None
        self.okButton.wait_for_press()
        sleep(0.5)

    def movement_phase(self):
        self.initiativeLed.off()
        self.movementLed.on()
        self.psychicLed.off()
        self.shootingLed.off()
        self.meleeLed.off()
        self.moraleLed.off()

        self.plusButton.when_pressed = None
        self.minusButton.when_pressed = None
        self.okButton.when_pressed = None
        self.okButton.wait_for_press()

    def psychic_phase(self):
        self.initiativeLed.off()
        self.movementLed.off()
        self.psychicLed.on()
        self.shootingLed.off()
        self.meleeLed.off()
        self.moraleLed.off()

        self.plusButton.when_pressed = None
        self.minusButton.when_pressed = None
        self.okButton.when_pressed = None
        self.okButton.wait_for_press()
        sleep(0.5)

    def shooting_phase(self):
        self.initiativeLed.off()
        self.movementLed.off()
        self.psychicLed.off()
        self.shootingLed.on()
        self.meleeLed.off()
        self.moraleLed.off()

        if self.selected_canticle in [SHROUDPSALM,
                                      BENEDICTION_OF_THE_OMNISSIAH]:
            self.display_canticle(True, True)

        self.plusButton.when_pressed = None
        self.minusButton.when_pressed = None
        self.okButton.when_pressed = None
        self.okButton.wait_for_press()

        if self.selected_canticle in [SHROUDPSALM,
                                      BENEDICTION_OF_THE_OMNISSIAH]:
            self.display_canticle(True, False)
        sleep(0.5)

    def melee_phase(self):
        self.initiativeLed.off()
        self.movementLed.off()
        self.psychicLed.off()
        self.shootingLed.off()
        self.meleeLed.on()
        self.moraleLed.off()

        if self.selected_canticle in [LITANY_OF_THE_ELECTROMANCER,
                                      CHANT_OF_THE_REMORSELESS_FIST,
                                      INVOCATION_OF_MACHINE_MIGHT]:
            self.display_canticle(True, True)

        self.plusButton.when_pressed = None
        self.minusButton.when_pressed = None
        self.okButton.when_pressed = None
        self.okButton.wait_for_press()

        if self.selected_canticle in [LITANY_OF_THE_ELECTROMANCER,
                                      CHANT_OF_THE_REMORSELESS_FIST,
                                      INVOCATION_OF_MACHINE_MIGHT]:
            self.display_canticle(True, False)
        sleep(0.5)

    def morale_phase(self):
        self.initiativeLed.off()
        self.movementLed.off()
        self.psychicLed.off()
        self.shootingLed.off()
        self.meleeLed.off()
        self.moraleLed.on()

        if self.selected_canticle in [1]:
            self.display_canticle(True, True)

        self.plusButton.when_pressed = None
        self.minusButton.when_pressed = None
        self.okButton.when_pressed = None
        self.okButton.wait_for_press()

        if self.selected_canticle in [1]:
            self.display_canticle(True, False)
        sleep(0.5)

    def select_if_end_game(self):
        self.initiativeLed.pulse()
        self.movementLed.pulse()
        self.psychicLed.pulse()
        self.shootingLed.pulse()
        self.meleeLed.pulse()
        self.moraleLed.pulse()

        self.plusButton.when_pressed = None
        self.minusButton.when_pressed = self.end_game_select
        self.okButton.when_pressed = None

        self.okButton.wait_for_press()

        self.plusButton.when_pressed = None
        self.minusButton.when_pressed = None
        self.okButton.when_pressed = None
        sleep(0.5)

    def end_game_select(self):
        self.continueGame = not self.continueGame
        if self.continueGame:
            self.initiativeLed.pulse()
            self.movementLed.pulse()
            self.psychicLed.pulse()
            self.shootingLed.pulse()
            self.meleeLed.pulse()
            self.moraleLed.pulse()
        else:
            self.initiativeLed.off()
            self.movementLed.off()
            self.psychicLed.off()
            self.shootingLed.off()
            self.meleeLed.off()
            self.moraleLed.off()
            
    def close(self):
        self.initiativeLed.close()
        self.movementLed.close()
        self.psychicLed.close()
        self.shootingLed.close()
        self.meleeLed.close()
        self.moraleLed.close()
        self.canticleLed1.close()
        self.canticleLed2.close()
        self.canticleLed3.close()
        self.canticleLed4.close()
        self.canticleLed5.close()
        self.canticleLed6.close()
        self.plusButton.close()
        self.minusButton.close()
        self.okButton.close()

    def display_canticle(self, selected=False, blinking=False):
        if selected:
            self.canticleLed1.off()
            self.canticleLed2.off()
            self.canticleLed3.off()
            self.canticleLed4.off()
            self.canticleLed5.off()
            self.canticleLed6.off()
            if self.selected_canticle == 1:
                if blinking:
                    self.canticleLed1.pulse()
                else:
                    self.canticleLed1.on()
            elif self.selected_canticle == LITANY_OF_THE_ELECTROMANCER:
                if blinking:
                    self.canticleLed2.pulse()
                else:
                    self.canticleLed2.on()
            elif self.selected_canticle == CHANT_OF_THE_REMORSELESS_FIST:
                if blinking:
                    self.canticleLed3.pulse()
                else:
                    self.canticleLed3.on()
            elif self.selected_canticle == SHROUDPSALM:
                if blinking:
                    self.canticleLed4.pulse()
                else:
                    self.canticleLed4.on()
            elif self.selected_canticle == INVOCATION_OF_MACHINE_MIGHT:
                if blinking:
                    self.canticleLed5.pulse()
                else:
                    self.canticleLed5.on()
            elif self.selected_canticle == BENEDICTION_OF_THE_OMNISSIAH:
                if blinking:
                    self.canticleLed6.pulse()
                else:
                    self.canticleLed6.on()
        else:
            if not self.canticle1Used:
                self.canticleLed1.on()
            else:
                self.canticleLed1.off()
            if not self.canticle2Used:
                self.canticleLed2.on()
            else:
                self.canticleLed2.off()
            if not self.canticle3Used:
                self.canticleLed3.on()
            else:
                self.canticleLed3.off()
            if not self.canticle4Used:
                self.canticleLed4.on()
            else:
                self.canticleLed4.off()
            if not self.canticle5Used:
                self.canticleLed5.on()
            else:
                self.canticleLed5.off()
            if not self.canticle6Used:
                self.canticleLed6.on()
            else:
                self.canticleLed6.off()
            if self.selected_canticle == 1:
                self.canticleLed1.pulse()
            elif self.selected_canticle == LITANY_OF_THE_ELECTROMANCER:
                self.canticleLed2.pulse()
            elif self.selected_canticle == CHANT_OF_THE_REMORSELESS_FIST:
                self.canticleLed3.pulse()
            elif self.selected_canticle == SHROUDPSALM:
                self.canticleLed4.pulse()
            elif self.selected_canticle == INVOCATION_OF_MACHINE_MIGHT:
                self.canticleLed5.pulse()
            elif self.selected_canticle == BENEDICTION_OF_THE_OMNISSIAH:
                self.canticleLed6.pulse()
            else:
                self.canticleLed1.pulse()
                self.canticleLed2.pulse()
                self.canticleLed3.pulse()
                self.canticleLed4.pulse()
                self.canticleLed5.pulse()
                self.canticleLed6.pulse()


if __name__ == "__main__":
    killTeam = KillTeam()
    try:
        while killTeam.continueGame:
            killTeam.select_canticles()
            killTeam.initiative_phase()
            killTeam.movement_phase()
            killTeam.psychic_phase()
            killTeam.shooting_phase()
            killTeam.melee_phase()
            killTeam.morale_phase()
            killTeam.select_if_end_game()
    finally:
        killTeam.close()
