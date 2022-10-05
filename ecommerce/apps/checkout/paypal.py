import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AYAnnRFroVDa-KNY7rCuG8BCuXUDp0OC_J3V4NOePNWeOaFKHSzUhLmzmQwISMruT90S-aq8nraCObfy"
        self.client_secret = "EPmhYUTYx3TI1FF-85Uhqat5qXlc_Yumy0qizUmOgVL-mG0PlMTYa91E7-gdsIrr73oDPjSC1TjQ__48"
        self.enviroment= SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client= PayPalHttpClient(self.enviroment)
