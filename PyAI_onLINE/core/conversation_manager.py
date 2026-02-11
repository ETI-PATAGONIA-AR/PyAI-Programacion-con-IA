#==================================================================
# PyAI_v1\core\conversation_manager.py - ETI Patagonia - prof.martintorres@educ.ar
#==================================================================
#==================================================================
# PyAI_v1/core/conversation_manager.py
# Conversación + control simple de tokens (sin tiktoken)
#==================================================================

class ConversationManager:
    def __init__(self, ai_client, max_tokens=8000):
        self.ai = ai_client
        self.max_tokens = max_tokens
        self.used_tokens = 0
        self.history = []

    # -------------------------------------------------------------
    def send(self, user_text: str) -> str:
        messages = []

        for h in self.history:
            messages.append({"role": "user", "content": h["user"]})
            messages.append({"role": "assistant", "content": h["assistant"]})

        messages.append({"role": "user", "content": user_text})

        response = self.ai.ask(messages)

        self.history.append({
            "user": user_text,
            "assistant": response
        })

        self.used_tokens += self._estimate_tokens(user_text)
        self.used_tokens += self._estimate_tokens(response)

        return response

    # -------------------------------------------------------------
    def clear(self):
        self.history = []
        self.used_tokens = 0

    # -------------------------------------------------------------
    def tokens_remaining(self):
        return self.max_tokens - self.used_tokens

    # -------------------------------------------------------------
    def _estimate_tokens(self, text: str) -> int:
        return max(1, len(text) // 4)
