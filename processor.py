import config

class MessageProcessor:
    def __init__(self, wechat_manager, ai_manager):
        """
        Initialize the processor with WeChat and AI managers.
        
        Args:
            wechat_manager: Instance of WeChatManager to send replies.
            ai_manager: Instance of AIManager to generate replies.
        """
        self.wx = wechat_manager
        self.ai = ai_manager
        
        # Simple in-memory history storage
        # Structure: { "user_id": [ {"role": "user", "content": "msg"}, ... ] }
        self.chat_history = {}

    def _update_history(self, user_id, role, content):
        """Update chat history for a user, keeping it within limits."""
        if user_id not in self.chat_history:
            self.chat_history[user_id] = []
        
        self.chat_history[user_id].append({"role": role, "content": content})
        
        # Trim history if too long
        if len(self.chat_history[user_id]) > config.MAX_HISTORY_LENGTH:
            self.chat_history[user_id] = self.chat_history[user_id][-config.MAX_HISTORY_LENGTH:]

    def handle_message(self, msg, chat_session=None):
        """
        Callback function to handle incoming messages.
        """
        try:
            # 1. Parse Message
            sender = chat_session.who if chat_session else "Unknown"
            content = getattr(msg, 'content', str(msg))
            msg_type = getattr(msg, 'type', 'unknown')

            # Filter: Only handle text messages for now
            # Note: wxautox4 message types might be integers or strings depending on version.
            # Usually type 1 is text. Assuming 'friend' type for now or checking content.
            # We will proceed assuming it's a valid message if content is string.
            
            if not isinstance(content, str):
                print(f"[{sender}] Ignored non-text message type: {msg_type}")
                return

            print(f"[{sender}] Received: {content}")

            # 2. Check for self-sent messages (optional, to avoid loops)
            if msg_type == 'sys': # Example check, adjust based on actual msg object
                return

            # 3. Get AI Response
            # Retrieve history
            history = self.chat_history.get(sender, [])
            
            print(f"[{sender}] Thinking...")
            reply = self.ai.get_response(content, history)
            print(f"[{sender}] Reply: {reply}")

            # 4. Send Reply
            self.wx.send_text(sender, reply)

            # 5. Update History
            self._update_history(sender, "user", content)
            self._update_history(sender, "assistant", reply)

        except Exception as e:
            print(f"Error processing message from {sender}: {e}")
            # Optionally send an error message back
            # self.wx.send_text(sender, "抱歉，我遇到了一点问题。")
